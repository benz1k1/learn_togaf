"""
The one place that talks to Claude (learn_togaf.md §1.5), over the official ``anthropic`` SDK
(1.4.0 in ``api/.venv``). Model, effort, batch size and max tokens come from the env YAML.

SDK parameters, as read from the installed SDK (``anthropic.resources.messages.Messages.create``):

- thinking: ``{"type": "adaptive"}`` (``ThinkingConfigAdaptiveParam``). ``budget_tokens`` is the
  pre-4.6 shape and is rejected by claude-opus-5; adaptive is the current parameter.
- effort and structured output both live in ``output_config`` (``OutputConfigParam``):
  ``{"effort": "high", "format": {"type": "json_schema", "schema": {...}}}``
  (``JSONOutputFormatParam``). The older top-level ``output_format`` is deprecated.
- prompt caching: the section text is a system block carrying ``cache_control: {"type": "ephemeral"}``
  (the stage prompt precedes it, so the cached prefix is stable across items of one stage).
- streaming: ``client.messages.stream(...)`` + ``get_final_message()`` for every call, so a long
  lesson never trips the HTTP timeout.
- batches: ``client.messages.batches.create(requests=[Request(custom_id, params=MessageCreateParamsNonStreaming(...))])``,
  polled with ``batches.retrieve`` until ``processing_status == "ended"``, collected with
  ``batches.results`` keyed by ``custom_id`` (results come back in any order).

Stages call :func:`complete` / :func:`complete_many`; the test-suite monkeypatches
:func:`complete` with a fake that replays recorded responses — no live call ever runs there.
"""

import time
from dataclasses import dataclass, field
from typing import Any, cast

import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request as BatchRequest
from loguru import logger

from learn_togaf import config

BATCH_POLL_SECONDS = 30


@dataclass
class Request:
    stage: str
    system: list[dict[str, Any]]
    user: str | list[dict[str, Any]]
    schema: dict[str, Any] | None = None
    max_tokens: int | None = None
    custom_id: str = ""
    section_ids: list[str] = field(default_factory=list)

    def params(self) -> dict[str, Any]:
        output_config: dict[str, Any] = {"effort": config.ANTHROPIC_EFFORT}
        if self.schema is not None:
            output_config["format"] = {"type": "json_schema", "schema": self.schema}
        return {
            "model": config.ANTHROPIC_MODEL,
            "max_tokens": self.max_tokens or config.ANTHROPIC_MAX_TOKENS,
            "system": self.system,
            "messages": [{"role": "user", "content": self.user}],
            "thinking": {"type": "adaptive"},
            "output_config": output_config,
        }

    def describe(self) -> str:
        """What ``--dry-run`` prints: the prompt, the section ids, the user turn."""
        user = (
            self.user
            if isinstance(self.user, str)
            else "\n".join(block.get("text", f"<{block.get('type')} block>") for block in self.user)
        )
        return (
            f"=== {self.stage} {self.custom_id}\n"
            f"--- model={config.ANTHROPIC_MODEL} effort={config.ANTHROPIC_EFFORT} thinking=adaptive "
            f"structured={'yes' if self.schema else 'no'}\n"
            f"--- input section ids: {', '.join(self.section_ids) or '(none)'}\n"
            f"--- system[0] (stage prompt):\n{self.system[0]['text']}\n"
            f"--- system[1] (cached sections): {len(self.system[1]['text'])} chars\n"
            f"--- user:\n{user}\n"
        )


_client: anthropic.Anthropic | None = None


def _get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=config.anthropic_api_key())
    return _client


def _text_of(message: anthropic.types.Message) -> str:
    if message.stop_reason == "refusal":
        raise RuntimeError(f"the model refused the request: {message.stop_details}")
    if message.stop_reason == "max_tokens":
        raise RuntimeError("the response hit max_tokens; raise anthropic.max_tokens in the env YAML")
    return "".join(block.text for block in message.content if block.type == "text")


def complete(request: Request) -> str:
    """One streamed call. Returns the text (JSON text when a schema was given)."""
    with _get_client().messages.stream(**request.params()) as stream:
        message = stream.get_final_message()
    usage = message.usage
    logger.info(
        f"{request.stage} {request.custom_id}: in={usage.input_tokens} cached={usage.cache_read_input_tokens} "
        f"out={usage.output_tokens}"
    )
    return _text_of(message)


def complete_batch(requests: list[Request]) -> dict[str, str]:
    """Submit one Message Batch (half price, no latency need), poll, collect by custom_id."""
    client = _get_client()
    batch = client.messages.batches.create(
        requests=[
            BatchRequest(
                custom_id=request.custom_id, params=cast(MessageCreateParamsNonStreaming, request.params())
            )
            for request in requests
        ]
    )
    logger.info(f"batch {batch.id} submitted with {len(requests)} requests")
    while True:
        batch = client.messages.batches.retrieve(batch.id)
        if batch.processing_status == "ended":
            break
        logger.info(
            f"batch {batch.id}: {batch.processing_status}, processing={batch.request_counts.processing}"
        )
        time.sleep(BATCH_POLL_SECONDS)
    results: dict[str, str] = {}
    failures: list[str] = []
    for result in client.messages.batches.results(batch.id):
        if result.result.type == "succeeded":
            results[result.custom_id] = _text_of(result.result.message)
        else:
            failures.append(f"{result.custom_id}: {result.result.type}")
    if failures:
        logger.warning(f"batch {batch.id}: {len(failures)} request(s) did not succeed: {failures}")
    return results


def complete_many(requests: list[Request], batch: bool) -> dict[str, str]:
    """Every request's text by custom_id; the Batches API in chunks of ``anthropic.batch_size``
    when ``batch`` is set, else one streamed call after another."""
    if not batch:
        return {request.custom_id: complete(request) for request in requests}
    results: dict[str, str] = {}
    size = config.ANTHROPIC_BATCH_SIZE
    for start in range(0, len(requests), size):
        results.update(complete_batch(requests[start : start + size]))
    return results
