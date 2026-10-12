# BAR.BusinessProcessModeling — Modeling business processes as a requirements source

> **Trigger:** Business processes are modeled as an end in itself: diagrams "sit on the shelf"; the process model has no links to requirements; process and specification live in different "worlds."

```episteme id="BAR.BusinessProcessModeling" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: A.3.4, E.17
  coordinates_with: C.27, A.10, C.30, C.16
UseThisWhen:
  automation project where the business process is the main source of functional requirements
  not when BPM automation (BPMS), simulation modeling, or org design is needed
Result:
  process model as structured input: every system-interacting element traces to a requirement
  ready input for elicitation and specification
Solution:
  for each system-interacting element — >=1 requirement; for a gateway — a business rule
  document the "process element -> requirement" traceability link
  record the as-is baseline; to-be — with a rationale for every change
  NOT: to-be without an as-is baseline; a model without traceability links; "optimization" without a problem statement
Stop:
  a process change yields the list of affected requirements in <=30 minutes; another analyst recovers the requirement set
Checks:
  traceability link for system-interacting elements; as-is baseline; to-be rationale; requirement reproducibility
Antipatterns:
  BPMN as an end in itself — diagrams without requirements and links
  To-be without an as-is baseline — a "target" process without problematizing the as-is
Continues:
  BAR.RequirementElicitation, BAR.RequirementTraceability
Reopen:
  change in process/regulation/org structure/system without updating the model (stale)
```