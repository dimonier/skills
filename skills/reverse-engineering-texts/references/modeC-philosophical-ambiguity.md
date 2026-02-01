# Example (ModeC): Philosophical-ish mini text (ambiguity triggered)

**TextArtifact**

> Freedom is not the absence of constraints; it is the ability to choose which constraints to accept.
> A society that promises unlimited choice often produces anxiety, not liberation.
> Therefore, the goal is not to remove rules, but to make them legible and negotiable.

**TeardownBlueprint (YAML)**

```yaml
blueprint_version: 2

source:
  title: "Freedom note"
  medium: "essay_fragment"
  audience: "general"
  intent: "reframe a concept and argue for a policy attitude"

method:
  paradigm:
    label: "hermeneutic"
    assumptions:
      - "Key terms are context-bound and may carry multiple valid readings."
    failure_modes:
      intra_paradigm_error: "interpretation not quote-backed or ignores internal tensions"
      inter_paradigm_conflict: "a pragmatic lens yields a different, still coherent mapping"
  mode: "ModeC_Hybrid"
  genre_profile: "philosophical"

context:
  audience: "general"
  intent: "reframe a concept and argue for a policy attitude"
  setting: "essay fragment"
  speaker_role: "essayist"
  genre: "essay_fragment"
  stakes: "medium"
  evidence:
    - quote: "Therefore, the goal is not to remove rules"
      note: "Signals normative policy attitude."
  confidence: medium

term_grounding:
  - term: "freedom"
    meaning_in_context: "A capacity to choose constraints, not the elimination of constraints."
    evidence:
      - quote: "Freedom is not the absence of constraints; it is the ability to choose which constraints to accept."
        note: "Explicit definition."
    confidence: high
  - term: "rules"
    meaning_in_context: "Constraints that can be made legible and negotiable."
    evidence:
      - quote: "make them legible and negotiable."
        note: "Defines desired properties of rules."
    confidence: medium

thesis:
  statement: "Freedom should be understood as selecting constraints; rules should be negotiable."
  descriptive_vs_normative: "mixed"
  evidence:
    - quote: "it is the ability to choose which constraints to accept."
      note: "Reframing freedom."
    - quote: "the goal is not to remove rules, but to make them legible and negotiable."
      note: "Normative conclusion."
  confidence: medium

hook:
  type: bold_claim
  target_emotion: "curiosity"
  mechanism: "counter-intuitive definition"
  evidence:
    - quote: "Freedom is not the absence of constraints"
      note: "Provocative reframing."

framework:
  label: problem_solution
  markers:
    - quote: "often produces anxiety, not liberation."
      stage: "problem"
      note: "Consequence framing."
    - quote: "the goal is not to remove rules, but to make them legible and negotiable."
      stage: "solution"
      note: "Proposed resolution."
  confidence: medium
  alternatives:
    - label: narrative_arc
      rationale: "setup (definition) → tension (anxiety) → resolution (legible rules)."

ambiguity:
  check:
    detected: true
    triggers:
      - "value_term"
      - "multiple_intents"
    evidence:
      - quote: "Freedom is not the absence of constraints"
        note: "Key value term is being redefined."
  interpretation_set:
    - id: i1
      interpretation: "Political reading: 'freedom' as institutional design; rules must be renegotiable."
      applies_when: "goal=policy_design OR audience=political_theory"
      evidence:
        - quote: "the goal is not to remove rules, but to make them legible and negotiable."
          note: "Explicitly about rules as a social artifact."
      confidence: medium
    - id: i2
      interpretation: "Psychological reading: 'freedom' as personal agency; anxiety arises from unlimited choice."
      applies_when: "goal=self_help OR audience=psychology"
      evidence:
        - quote: "promises unlimited choice often produces anxiety"
          note: "Framed as emotional consequence."
      confidence: medium

segments:
  - id: s1
    intent: "Define freedom via constraints."
    summary: ""
    claim: "Freedom is choosing constraints, not eliminating them."
    descriptive_vs_normative: "mixed"
    evidence_type: definition
    relation_to_prev: none
    rhetoric: { ethos: "", pathos: "curiosity", logos: "definition" }
    evidence:
      - quote: "it is the ability to choose which constraints to accept."
        note: "Definition core."
    confidence: high
  - id: s2
    intent: "Warn about unlimited choice."
    summary: ""
    claim: "Unlimited choice can produce anxiety."
    descriptive_vs_normative: "descriptive"
    evidence_type: mechanism
    relation_to_prev: adds_detail
    rhetoric: { ethos: "", pathos: "caution", logos: "cause-effect" }
    evidence:
      - quote: "often produces anxiety, not liberation."
        note: "Consequence claim."
    confidence: medium
  - id: s3
    intent: "Conclude with a stance on rules."
    summary: ""
    claim: "Rules should be legible and negotiable rather than removed."
    descriptive_vs_normative: "normative"
    evidence_type: mechanism
    relation_to_prev: concludes
    rhetoric: { ethos: "", pathos: "", logos: "therefore" }
    evidence:
      - quote: "Therefore, the goal is not to remove rules, but to make them legible and negotiable."
        note: "Normative conclusion."
    confidence: high

rhetoric_summary:
  ethos: []
  pathos:
    - quote: "produces anxiety"
      note: "Affective consequence."
  logos:
    - quote: "Therefore,"
      note: "Explicit inferential marker."

external_validation:
  sources:
    - citation: "PLACEHOLDER: external sources if provided / available"
      url: ""
      note: "ModeC expects external validation when feasible."
  agreements: []
  disagreements: []
  constraints: "Example only: no real sources included."
  confidence: low

non_commutativity:
  tested: true
  runs:
    - order: "A_then_B"
      note: "Interpretation-first, then external framing."
    - order: "B_then_A"
      note: "External framing-first, then reinterpret the text."
  detected: true
  delta_summary: "Order changes which reading becomes 'primary' (political vs psychological)."

conflicts:
  - id: c1
    kind: "inter_paradigm"
    severity: ""
    statement: "Is this primarily a political argument or a psychological one?"
    evidence:
      - quote: "unlimited choice often produces anxiety"
        note: "Psychological cue."
      - quote: "make them legible and negotiable"
        note: "Institutional cue."
    note: "Not an error; requires boundary/context selection."

pattern_library:
  - name: "ReframeValueTermThenConsequenceThenNormativeStance"
    description: "Redefine a value term, show a consequence of the naive view, then propose a stance."
    evidence:
      - quote: "Freedom is not..."
        note: "Reframing."
      - quote: "produces anxiety"
        note: "Consequence."
      - quote: "the goal is not..."
        note: "Stance."

reconstructed_outline:
  - "Counter-intuitive definition."
  - "Consequence of naive interpretation."
  - "Normative conclusion."

audit:
  coverage_notes: "All 3 sentences covered; ambiguity handled via interpretation_set."
  unresolved_questions:
    - "What is the intended domain: policy or personal agency?"
  confidence_overall: medium
```

