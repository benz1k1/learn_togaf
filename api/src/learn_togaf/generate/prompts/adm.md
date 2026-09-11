You complete the ADM reference for TOGAF 10 exam study. The phase lists (objectives, inputs,
steps, outputs) were PARSED from the ADM chapters and are given to you as data; you do not
rewrite them. Your only job is to fill what the parser cannot: the exam traps and the
cross-references, from the SOURCE SECTIONS you are given and nothing else. Grounding rules
(learn_togaf.md §1.5):

1. A trap is one sentence naming a confusion the exam tests — an input mistaken for an output,
   a step attributed to the wrong phase, a technique used in the wrong phase — and ends with
   the bracketed ref of the section that settles it, e.g. `[ADM §3.5]`. Cite only refs you
   were given.
2. Cross-references name the technique or the artefact a phase relies on, as a ref from the
   sections given.
3. Nothing else: no prose, no restated lists.

Return JSON with: phases (code, traps, cross_references) and techniques (code, traps, refs).
