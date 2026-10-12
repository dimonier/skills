# BAR.RequirementElicitation — Eliciting requirements

> **Trigger:** Stakeholders cannot articulate what they need; tacit requirements are not surfaced because the stakeholder treats them as "obvious."

```episteme id="BAR.RequirementElicitation" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: A.3.4, A.10
  coordinates_with: A.2.1, A.15, A.3.2, B.3
UseThisWhen:
  elicitation phase: initial collection of material from stakeholders, documents, legacy systems
  not when specification or validation is needed
Result:
  structured requirements material: for each — source, technique, date, context; tacit requirements surfaced
  ready input for specification
Solution:
  choose the technique to match the source type and requirement class
  cross-validate high-risk requirements against an independent source
  surface tacit ones via observation/prototyping/T-shirt sizing
  NOT: relying on a single technique (interviews only)
Stop:
  every requirement class has a source and technique; contradictions surfaced before specification; another analyst recovers a comparable set
Checks:
  source/technique/date/context recorded; >=2 techniques; high-risk cross-validated; tacit recorded
Antipatterns:
  Interview monoculture — interviews for every class, NFRs from words without measurement
  Tacit knowledge extraction theatre — "observe for 2 hours" without probing WHY
Continues:
  BAR.ProblemVsSolutionSeparation, BAR.RequirementSpecification
Reopen:
  change in source (stakeholder departure, regulatory document update) (stale)
```