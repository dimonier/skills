# BAR.RequirementPrioritization — Prioritizing requirements

> **Trigger:** The product backlog holds 200+ requirements, all marked "critical"; each stakeholder pushes "their" requirements as the highest priority.

```episteme id="BAR.RequirementPrioritization" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: C.25, G.9
  coordinates_with: G.0, G.4, G.5, C.16
UseThisWhen:
  resources are constrained and >=3 stakeholders compete for them within a release/iteration
  not when portfolio or strategic planning is needed
Result:
  prioritized backlog: an ordered set of requirements by explicit, agreed criteria
  ready input for iteration/release planning
Solution:
  assess each requirement by: value, cost, risk, dependency/architectural significance, time-criticality
  agree criteria with stakeholders BEFORE ranking; record rejected criteria
  prioritize with the holders of resource constraints (development, operations)
  NOT: declaring everything "critical"; voting instead of quantified trade-off
Stop:
  stakeholders accept the trade-off (REQ-42 over REQ-17); overlap of priority and delivered >= 80%
Checks:
  value quantified/ranked; cost estimated by a developer; criteria agreed before ranking; resource-constraint holders involved
Antipatterns:
  Priority by voting — political weight wins, not value
  Prioritization without developers — top-5 unimplementable without a feasibility/cost estimate
Continues:
  BAR.RequirementChangeManagement (priorities set the threshold for change requests)
Reopen:
  release/iteration completion; change in business priorities (stale)
```