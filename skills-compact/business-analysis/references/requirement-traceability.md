# BAR.RequirementTraceability — Tracing requirements

> **Trigger:** Impossible to answer "why are we doing this?" for a given requirement; a change cannot determine the affected components and tests.

```episteme id="BAR.RequirementTraceability" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: A.10, C.16
  coordinates_with: C.2.1, C.32.ADR, E.17, A.6.P, G.11
UseThisWhen:
  artifact chain need -> requirement -> design -> implementation -> test; regulative traceability requirements
  not when automating tracing with a tool
Result:
  traceability matrix: forward trace (requirement -> design -> implementation -> test) and backward trace (test -> requirement -> need)
  ready input for change management
Solution:
  establish trace links for every requirement (design, code, tests) and every test (requirement)
  for safety-critical/regulated domains — traceability to the test case is mandatory
  NOT: "floating" requirements without a trace to the source; "floating" tests without a trace to a requirement
Stop:
  impact analysis of a typical change runs in <=15 minutes; a random change finds all affected artifacts
Checks:
  forward trace to design and tests; backward trace from tests; regulated: 100% coverage confirmed
Antipatterns:
  Tracing in Excel for audits — links not updated, impact analysis impossible
  Forward-only tracing — no backward links, coverage/root-cause cannot be checked
Continues:
  BAR.RequirementChangeManagement (traceability is the precondition for impact analysis)
Reopen:
  requirement/design/test changed without updating links (stale)
```