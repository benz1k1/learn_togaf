You build a glossary for TOGAF 10 exam study from the SOURCE SECTIONS you are given — the
Definitions chapter and the sections that define a term — and nothing else. Grounding rules
(learn_togaf.md §1.5):

1. One entry per defined term. The definition is a paraphrase in your own words; do not copy
   the standard's sentence. Put the sentence you paraphrased in `source_sentence` — it is kept
   beside the entry for review and never shipped.
2. `document` is the document code and `section` the ref of the one section the definition is
   traceable to, exactly as given in the SOURCE SECTIONS header (e.g. document `ADM`, section
   `ADM §3.3`). Cite only refs you were given.
3. `confusable_with` lists the ids of other terms in this same output that candidates mix up
   with this one (artifact / deliverable / building block; Architecture Vision / Architecture
   Definition Document; Enterprise Continuum / Architecture Repository). Ids are lowercase
   slugs with underscores.

Return JSON with: terms (id, term, definition, document, section, confusable_with,
source_sentence).
