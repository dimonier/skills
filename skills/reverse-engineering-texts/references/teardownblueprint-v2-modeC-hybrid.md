# TeardownBlueprint v2 — ModeC_Hybrid (Template)

Use this when you need **ModeA + ModeB** and an explicit integration step.

```yaml
blueprint_version: 2

source:
  title: ""
  medium: ""
  audience: ""
  intent: ""

method:
  paradigm:
    label: "descriptive_structural"
    assumptions: []
    failure_modes:
      intra_paradigm_error: "integration makes claims that neither A nor B supports"
      inter_paradigm_conflict: "A and B disagree due to paradigm mismatch"
  mode: "ModeC_Hybrid"
  genre_profile: ""    # scientific|philosophical|literary|other

context:
  audience: ""
  intent: ""
  setting: ""
  speaker_role: ""
  genre: ""
  stakes: ""
  evidence:
    - quote: ""
      note: ""
  confidence: medium

term_grounding:
  - term: ""
    meaning_in_context: ""
    evidence:
      - quote: ""
        note: ""
    confidence: medium

thesis:
  statement: ""
  descriptive_vs_normative: ""  # descriptive|normative|mixed
  evidence:
    - quote: ""
      note: ""
  confidence: medium

hook:
  type: ""
  target_emotion: ""
  mechanism: ""
  evidence:
    - quote: ""
      note: ""

framework:
  label: ""
  markers:
    - quote: ""
      stage: ""
      note: ""
  confidence: medium
  alternatives:
    - label: ""
      rationale: ""

ambiguity:
  check:
    detected: false
    triggers:
      - ""
    evidence:
      - quote: ""
        note: ""
  interpretation_set:
    - id: i1
      interpretation: ""
      applies_when: ""
      evidence:
        - quote: ""
          note: ""
      confidence: medium

segments:
  - id: s1
    intent: ""
    summary: ""
    claim: ""
    descriptive_vs_normative: ""
    evidence_type: ""
    relation_to_prev: ""
    rhetoric:
      ethos: ""
      pathos: ""
      logos: ""
    evidence:
      - quote: ""
        note: ""
    confidence: medium

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

external_validation:
  sources:
    - citation: ""
      url: ""
      note: ""
  agreements:
    - ""
  disagreements:
    - ""
  constraints: ""
  confidence: medium

non_commutativity:
  tested: false
  runs:
    - order: "A_then_B"
      note: ""
    - order: "B_then_A"
      note: ""
  detected: false
  delta_summary: ""

conflicts:
  - id: c1
    kind: ""           # intra_paradigm|inter_paradigm
    severity: ""       # critical|significant|minor (for intra_paradigm)
    statement: ""
    evidence:
      - quote: ""
        note: ""
    note: ""

pattern_library:
  - name: ""
    description: ""
    evidence:
      - quote: ""
        note: ""

reconstructed_outline:
  - ""

audit:
  coverage_notes: ""
  unresolved_questions:
    - ""
  confidence_overall: medium
```

