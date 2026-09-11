"""The Jinja environment for the pages, and the filters every template may use."""

import json
import os
from datetime import date, datetime
from typing import Any

from fastapi.templating import Jinja2Templates
from markdown_it import MarkdownIt
from markupsafe import Markup

from learn_togaf.pages.nav import nav_items
from learn_togaf.pages.security import csrf_token

_TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
_markdown = MarkdownIt("commonmark", {"typographer": True}).enable("table")

templates = Jinja2Templates(directory=_TEMPLATES_DIR)
templates.env.globals["csrf_token"] = csrf_token
templates.env.globals["nav_items"] = nav_items


def render_markdown(text: str | None) -> Markup:
    return Markup(_markdown.render(text or ""))


def format_datetime(value: Any) -> Any:
    if not value:
        return value
    moment = value if isinstance(value, datetime) else None
    if moment is None:
        try:
            moment = datetime.fromisoformat(str(value).strip().replace("Z", "+00:00"))
        except ValueError:
            return value
    return moment.strftime("%d-%b-%Y %H:%M")


def format_date(value: Any) -> Any:
    if not value:
        return value
    if isinstance(value, (date, datetime)):
        return value.strftime("%d-%b-%Y")
    try:
        return date.fromisoformat(str(value)[:10]).strftime("%d-%b-%Y")
    except ValueError:
        return value


def attr_json(value: Any) -> Markup:
    """JSON for an HTML attribute. ``|tojson`` is wrong there: it does not escape ``"``."""
    return Markup(
        json.dumps(value, default=str)
        .replace("&", "&amp;")
        .replace('"', "&#34;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def from_json(value: Any) -> Any:
    if value is None or value == "":
        return []
    if isinstance(value, (list, dict)):
        return value
    return json.loads(value)


def duration(seconds: Any) -> str:
    if seconds is None:
        return "—"
    seconds = int(seconds)
    return f"{seconds // 60}:{seconds % 60:02d}"


templates.env.filters["markdown"] = render_markdown
templates.env.filters["fmt_dt"] = format_datetime
templates.env.filters["fmt_date"] = format_date
templates.env.filters["attr_json"] = attr_json
templates.env.filters["from_json"] = from_json
templates.env.filters["duration"] = duration
