# BAR.RequirementSpecification — Specifying requirements

> **Trigger:** Requirements are written free-form — developer and tester interpret them differently; the requirement cannot be verified (no measurable acceptance criteria).

```episteme id="BAR.RequirementSpecification" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: A.19, C.22.2
  coordinates_with: A.19.ECS, C.16, C.25, A.10, C.2.1, E.17, G.9
UseThisWhen:
  specification phase: turning raw elicitation material into requirements for development and testing
  not when the system's architectural specification is needed
Result:
  requirement with structure: id, function/constraint description, actor/role, measurable acceptance criteria, priority, source; NFRs — quantified scenario (stimulus -> response -> measure)
  ready input for development and testing
Solution:
  every acceptance criterion is measurable; NFRs — quantified scenario
  requirement: unique id + actor/role + measurable criteria + priority + source
  NOT: ambiguous terms ("fast", "user-friendly", "sufficient") without a measure; several functions in one requirement; missing acceptance criteria
Stop:
  a tester writes a test case from the acceptance criteria with no clarification
Checks:
  id/description/actor/role; criteria measurable; no ambiguous terms; atomicity (one function/constraint)
Antipatterns:
  Natural-language literature — a "user-friendly, fast, flexible" essay without measure
  Atomicity violation — "register, notify, report" in one requirement
Continues:
  BAR.RequirementValidation, BAR.RequirementPrioritization, BAR.RequirementTraceability
Reopen:
  change in stakeholder requirements or context (stale)
```