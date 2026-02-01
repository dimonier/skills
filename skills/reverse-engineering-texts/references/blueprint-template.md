# TeardownBlueprint Template

Use this template to produce a **traceable** reverse-engineering result: every key field should include at least one short quote from the text.

## Template (YAML)

```yaml
blueprint_version: 1

source:
  title: ""            # optional
  medium: ""           # e.g., blog_post, spec, email, thread, script
  audience: ""         # optional
  intent: ""           # optional

thesis:
  statement: ""        # 1 sentence
  evidence:
    - quote: ""
      note: ""         # why this supports the thesis
  confidence: high     # high|medium|low

hook:
  type: ""             # story|question|statistic|bold_claim|pain_point|curiosity_gap|analogy|other
  target_emotion: ""   # e.g., curiosity, urgency, fear, hope, validation
  mechanism: ""        # optional: what's the "gap" or tension
  evidence:
    - quote: ""
      note: ""

framework:
  label: ""            # AIDA|PAS|PASTOR|BAB|problem_solution|narrative_arc|other
  markers:
    - quote: ""        # key markers that justify the mapping
      stage: ""        # e.g., AIDA: attention|interest|desire|action
      note: ""
  confidence: medium   # high|medium|low
  alternatives:
    - label: ""        # if ambiguous, list plausible alternatives
      rationale: ""

segments:
  - id: s1
    intent: ""         # one-line intent of this block
    summary: ""        # 1–2 sentences, optional
    claim: ""          # what the block asserts
    evidence_type: ""  # example|data|authority|analogy|definition|experience|mechanism|benefit|other
    relation_to_prev: ""  # supports|contrasts|adds_detail|reframes|concludes|other
    rhetoric:
      ethos: ""        # optional: credibility move in this segment
      pathos: ""       # optional: emotional move
      logos: ""        # optional: reasoning move
    evidence:
      - quote: ""
        note: ""
    confidence: high

rhetoric_summary:
  ethos:
    - quote: ""
      note: ""
  pathos:
    - quote: ""
      note: ""
  logos:
    - quote: ""
      note: ""

pattern_library:
  - name: ""           # short label, e.g. "DefinitionThenAnalogyThenApplication"
    description: ""    # what it does and when to reuse
    evidence:
      - quote: ""
        note: ""

reconstructed_outline:
  - ""                 # forward outline bullets (thesis → hook → outline → arguments)

audit:
  coverage_notes: ""   # what's missing/unclear
  unresolved_questions:
    - ""
  confidence_overall: medium
```

## Evidence rules (non-negotiable)
- Prefer **direct quotes** over paraphrase for thesis/framework/claims.
- Quotes can be short; use multiple quotes if needed.
- If you infer something that is not directly supported, keep it, but set `confidence: low` and write an alternative hypothesis.

## Minimal acceptance check
- Thesis, hook, framework each have evidence quotes.
- Every segment has (intent, claim, evidence_type, relation_to_prev) plus at least one quote.
