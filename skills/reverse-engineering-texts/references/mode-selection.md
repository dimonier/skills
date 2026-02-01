# Mode selection (decision rules)

Goal: pick the **minimum mode** that satisfies the task.

## Decision tree

### Step 1 — Is external validation required?
- If the task requires using external sources (fact-checking, scientific validation, “cite sources”, compare against literature) → **ModeB_Transcendent**.

### Step 2 — Do you need both internal teardown and external validation?
- If you must both (a) reconstruct internal logic/structure and (b) validate/critique with sources → **ModeC_Hybrid**.

### Otherwise
- Default to **ModeA_Immanent** (internal teardown only).

## Always-on overlays (not modes)

### Context-first (always)
Before framework labeling, fill `context` and `term_grounding` using quotes.

### Ambiguity (conditional-mandatory)
Run `ambiguity.check`. If `detected=true` you must output `interpretation_set` (>=2), each with evidence quotes and `applies_when`.

### Non-commutativity (triggered)
If you suspect order effects (A→B vs B→A could change the “primary” reading), test non-commutativity and record deltas.

