# Quality gates (hard requirements)

Use this as an execution checklist. If you cannot satisfy a gate, you must explicitly write the constraint and lower confidence.

## Gate 0 — Traceability (always)
- Thesis/framework/each segment claim has >=1 **direct quote**.

## Gate 1 — Context-first (always)
- `context` is explicit (or assumptions are explicit).
- `term_grounding` exists for key/value terms and is quote-backed.

## Gate 2 — Descriptive vs normative (when relevant)
- `descriptive_vs_normative` is set at least for `thesis`.
- Set it for segments that are prescriptive (“should/must/recommend”) or value-loaded.

## Gate 3 — Ambiguity (conditional-mandatory)
- `ambiguity.check` is present.
- If `ambiguity.check.detected=true`:
  - `interpretation_set` has >=2 interpretations
  - each interpretation is quote-backed
  - each has `applies_when` (collapse conditions)

## Gate 4 — ModeB/ModeC external validation (only when in ModeB/ModeC)
- Provide sources (>=3 independent when feasible).
- Record agreements and disagreements.
- Explain how disagreements change confidence.

## Gate 5 — Non-commutativity (only when tested/triggered)
- Record A→B and B→A summaries and a concrete delta.

## Gate 6 — Conflict taxonomy (when conflicts appear)
- Classify conflicts as `intra_paradigm` vs `inter_paradigm`.
- Do not “resolve” an inter-paradigm conflict as if it were an error.

