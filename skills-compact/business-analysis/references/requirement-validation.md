# BAR.RequirementValidation — Validating requirements

> **Trigger:** At the demo the stakeholder says "that's not what I meant"; development discovers an infeasible constraint a month later.

```episteme id="BAR.RequirementValidation" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: A.7, C.22.2
  coordinates_with: C.24, A.21, C.16, C.25
UseThisWhen:
  checking requirements for correctness/completeness/feasibility/testability BEFORE development
  not when acceptance testing (verifying the implementation) is needed
Result:
  validated requirement set: stakeholder agreement + feasibility + testability + consistency
  gate: requirement accepted for implementation
Solution:
  stakeholder signs off the problem statement and acceptance criteria
  feasibility check (architecture spike under high risk); test-case derivation; consistency with dependent requirements
  NOT: handing to development without signed-off criteria; skipping feasibility for high-risk ones; validating without the implementer role
Stop:
  all conflicts among requirements resolved; a tester writes a test case with no clarification
Checks:
  criteria signed off; feasibility passed (spike under risk); test-case derivation; implementer role involved
Antipatterns:
  Validation = prototype demo — "looks good" without checking criteria/feasibility
  Validation without a developer — "infeasible on the stack" two weeks later
Continues:
  BAR.RequirementTraceability (a validated requirement triggers traceability)
Reopen:
  a requirement changed without re-validation (stale)
```