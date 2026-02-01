# Example (ModeA): Scientific-ish mini text (scientific profile)

**TextArtifact**

> In our tests, caching reduced median latency from 120ms to 35ms.
> The improvement comes from avoiding repeated database queries.
> However, cache invalidation increased code complexity and caused two production incidents.
> We recommend caching only for endpoints with stable data and high read volume.

**TeardownBlueprint (YAML)**

```yaml
blueprint_version: 2

source:
  title: "Caching note"
  medium: "memo"
  audience: "engineers"
  intent: "report a result and recommend a constrained policy"

method:
  paradigm:
    label: "descriptive_structural"
    assumptions: []
    failure_modes:
      intra_paradigm_error: "numbers/causal claims not supported by quotes"
      inter_paradigm_conflict: "alternative lens changes what 'recommend' optimizes for"
  mode: "ModeA_Immanent"
  genre_profile: "scientific"

context:
  audience: "engineers"
  intent: "report a result and recommend a constrained policy"
  setting: "internal memo"
  speaker_role: "engineer"
  genre: "memo"
  stakes: "medium"
  evidence:
    - quote: "We recommend caching only for endpoints with stable data and high read volume."
      note: "Shows policy intent."
  confidence: medium

term_grounding:
  - term: "caching"
    meaning_in_context: "Avoid repeated database queries by reusing stored responses."
    evidence:
      - quote: "avoiding repeated database queries"
        note: "Defines mechanism."
    confidence: high

thesis:
  statement: "Caching improves latency but introduces risk/complexity; use it selectively."
  descriptive_vs_normative: "mixed"
  evidence:
    - quote: "caching reduced median latency from 120ms to 35ms."
      note: "Benefit."
    - quote: "cache invalidation increased code complexity and caused two production incidents."
      note: "Cost/risk."
    - quote: "We recommend caching only for endpoints with stable data and high read volume."
      note: "Selective policy."
  confidence: high

hook:
  type: statistic
  target_emotion: "urgency"
  mechanism: "quantified impact"
  evidence:
    - quote: "reduced median latency from 120ms to 35ms."
      note: "Numeric hook."

framework:
  label: problem_solution
  markers:
    - quote: "However, cache invalidation increased code complexity"
      stage: "problem"
      note: "Introduces downside."
    - quote: "We recommend caching only for endpoints..."
      stage: "solution"
      note: "Recommendation as solution."
  confidence: medium
  alternatives:
    - label: other
      rationale: "Short empirical claim + policy; not a full marketing arc."

ambiguity:
  check:
    detected: false
    triggers: []
    evidence: []
  interpretation_set: []

segments:
  - id: s1
    intent: "State the performance result."
    summary: ""
    claim: "Caching reduced median latency substantially."
    descriptive_vs_normative: "descriptive"
    evidence_type: data
    relation_to_prev: none
    rhetoric: { ethos: "", pathos: "", logos: "measurement" }
    evidence:
      - quote: "caching reduced median latency from 120ms to 35ms."
        note: "Measurement claim."
    confidence: high
  - id: s2
    intent: "Explain the mechanism."
    summary: ""
    claim: "The improvement is due to fewer repeated DB queries."
    descriptive_vs_normative: "descriptive"
    evidence_type: mechanism
    relation_to_prev: adds_detail
    rhetoric: { ethos: "", pathos: "", logos: "cause-effect" }
    evidence:
      - quote: "The improvement comes from avoiding repeated database queries."
        note: "Causal explanation."
    confidence: high
  - id: s3
    intent: "State downsides."
    summary: ""
    claim: "Caching increased complexity and contributed to incidents."
    descriptive_vs_normative: "descriptive"
    evidence_type: experience
    relation_to_prev: contrasts
    rhetoric: { ethos: "", pathos: "caution", logos: "tradeoff" }
    evidence:
      - quote: "increased code complexity and caused two production incidents."
        note: "Risk claim."
    confidence: medium
  - id: s4
    intent: "Conclude with bounded recommendation."
    summary: ""
    claim: "Cache only stable, high-read endpoints."
    descriptive_vs_normative: "normative"
    evidence_type: mechanism
    relation_to_prev: concludes
    rhetoric: { ethos: "", pathos: "", logos: "policy" }
    evidence:
      - quote: "We recommend caching only for endpoints with stable data and high read volume."
        note: "Recommendation."
    confidence: high

rhetoric_summary:
  ethos: []
  pathos:
    - quote: "caused two production incidents."
      note: "Caution via risk."
  logos:
    - quote: "reduced median latency from 120ms to 35ms."
      note: "Quantified claim."

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
  - name: "MeasureThenMechanismThenTradeoffThenPolicy"
    description: "Open with a metric, explain mechanism, acknowledge tradeoffs, end with bounded recommendation."
    evidence:
      - quote: "reduced median latency from 120ms to 35ms."
        note: "Measure."
      - quote: "The improvement comes from avoiding repeated database queries."
        note: "Mechanism."
      - quote: "However, cache invalidation increased code complexity"
        note: "Tradeoff."
      - quote: "We recommend caching only for endpoints..."
        note: "Policy."

reconstructed_outline:
  - "State measured impact."
  - "Explain mechanism."
  - "Acknowledge downsides."
  - "Give bounded recommendation."

audit:
  coverage_notes: "All statements covered."
  unresolved_questions:
    - "What was the sample size and workload shape?"
  confidence_overall: medium
```

