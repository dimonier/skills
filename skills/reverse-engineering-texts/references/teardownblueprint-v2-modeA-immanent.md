# TeardownBlueprint v2 — ModeA_Immanent (Template)

Use this when you do **internal** reverse-engineering only (no outside sources).

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
      intra_paradigm_error: "internal contradiction or unquoted inference"
      inter_paradigm_conflict: "another lens yields a different but coherent reading"
  mode: "ModeA_Immanent"
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
  type: ""             # story|question|statistic|bold_claim|pain_point|curiosity_gap|analogy|other
  target_emotion: ""
  mechanism: ""
  evidence:
    - quote: ""
      note: ""

framework:
  label: ""            # AIDA|PAS|PASTOR|BAB|problem_solution|narrative_arc|other
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
    evidence_type: ""   # example|data|authority|analogy|definition|experience|mechanism|benefit|other
    relation_to_prev: ""  # supports|contrasts|adds_detail|reframes|concludes|other
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
  sources: []
  agreements: []
  disagreements: []
  constraints: "ModeA: no external validation."
  confidence: medium

non_commutativity:
  tested: false
  runs: []
  detected: false
  delta_summary: ""

conflicts: []

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

