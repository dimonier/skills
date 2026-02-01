# Examples

## Example 1: Short teardown (mini text)

**TextArtifact**

> Reverse engineering software means taking a finished program and reconstructing how it works.
> You can do the same with writing: take a finished text and rebuild its blueprint.
> Start by finding the thesis, then the hook, then the argument blocks and the rhetoric.
> The result is a reusable structure you can apply to your own content.

**TeardownBlueprint (YAML)**

```yaml
blueprint_version: 1

source:
  title: "Mini example"
  medium: "note"
  audience: "writers/builders"
  intent: "explain the concept and why it is useful"

thesis:
  statement: "Any finished text can be reverse-engineered into a reusable blueprint."
  evidence:
    - quote: "take a finished text and rebuild its blueprint."
      note: "Directly states the core claim."
  confidence: high

hook:
  type: analogy
  target_emotion: curiosity
  mechanism: "Transfer a known concept (software RE) to writing."
  evidence:
    - quote: "Reverse engineering software means taking a finished program and reconstructing how it works."
      note: "Sets the analogy base."
    - quote: "You can do the same with writing"
      note: "Bridges analogy to domain."

framework:
  label: problem_solution
  markers:
    - quote: "Start by finding the thesis, then the hook, then the argument blocks and the rhetoric."
      stage: "solution"
      note: "Procedure-as-solution."
  confidence: medium
  alternatives:
    - label: AIDA
      rationale: "There is attention via analogy and an implicit 'action' (start by...), but it is not a full CTA."

segments:
  - id: s1
    intent: "Define reverse engineering via software analogy."
    claim: "Reverse engineering reconstructs how a finished artifact works."
    evidence_type: definition
    relation_to_prev: none
    rhetoric:
      ethos: ""
      pathos: "curiosity"
      logos: "definition"
    evidence:
      - quote: "Reverse engineering software means taking a finished program and reconstructing how it works."
        note: "Definition."
    confidence: high

  - id: s2
    intent: "Transfer the analogy to writing."
    claim: "Writing can be reverse-engineered into a blueprint."
    evidence_type: analogy
    relation_to_prev: reframes
    rhetoric:
      ethos: ""
      pathos: "curiosity"
      logos: "analogy mapping"
    evidence:
      - quote: "You can do the same with writing"
        note: "Explicit mapping."
      - quote: "rebuild its blueprint."
        note: "Names the target artifact."
    confidence: high

  - id: s3
    intent: "Provide the decomposition procedure."
    claim: "The blueprint can be extracted via thesis/hook/arguments/rhetoric."
    evidence_type: mechanism
    relation_to_prev: adds_detail
    rhetoric:
      ethos: ""
      pathos: ""
      logos: "enumeration"
    evidence:
      - quote: "Start by finding the thesis, then the hook, then the argument blocks and the rhetoric."
        note: "Ordered method."
    confidence: high

  - id: s4
    intent: "State the payoff."
    claim: "The extracted structure is reusable for creating new content."
    evidence_type: benefit
    relation_to_prev: concludes
    rhetoric:
      ethos: ""
      pathos: "hope"
      logos: "utility claim"
    evidence:
      - quote: "The result is a reusable structure you can apply to your own content."
        note: "Direct benefit statement."
    confidence: high

rhetoric_summary:
  ethos: []
  pathos:
    - quote: "You can do the same with writing"
      note: "Invites participation; curiosity framing."
  logos:
    - quote: "Start by finding the thesis, then the hook..."
      note: "Procedural/logical scaffold."

pattern_library:
  - name: "KnownDomainAnalogyToNewDomain"
    description: "Use a familiar domain definition, then explicitly map it to the target domain."
    evidence:
      - quote: "Reverse engineering software means..."
        note: "Known domain."
      - quote: "You can do the same with writing"
        note: "Mapping."

reconstructed_outline:
  - "Define reverse engineering via software analogy."
  - "Map the concept to writing (text → blueprint)."
  - "Give a quick decomposition procedure (thesis/hook/arguments/rhetoric)."
  - "State payoff: reuse the structure for new content."

audit:
  coverage_notes: "All 4 sentences represented as segments with quotes."
  unresolved_questions: []
  confidence_overall: high
```

## Prompt: generate a draft from a blueprint (structure-first)

```text
You are a writing system. Generate a new draft from the provided TeardownBlueprint.

Rules:
- Follow the reconstructed_outline and framework stages if present.
- Reuse the pattern_library moves where applicable.
- Do NOT copy phrases from evidence quotes; only reuse structure.
- Keep tone appropriate for the source audience/intent.

Input (TeardownBlueprint YAML):
<blueprint>
...
</blueprint>
```
