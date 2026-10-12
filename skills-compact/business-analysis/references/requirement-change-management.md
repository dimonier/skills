# BAR.RequirementChangeManagement — Managing requirement changes

> **Trigger:** New requirements are added "by phone call" without impact assessment; scope creep untracked — the project does 2x more while key functionality is not ready.

```episteme id="BAR.RequirementChangeManagement" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: C.22.2, A.21
  coordinates_with: A.10, C.32.ADR, G.5, G.11, G.9, C.28, C.27
UseThisWhen:
  project in active development >3 months with >=2 stakeholders supplying changes
  not when contract or budgeting management is needed
Result:
  change control via gate decision: change request -> impact analysis -> decision (accept/defer/reject) -> baseline update + traceability
  scope creep stopped
Solution:
  every change: capture (source, reason) -> impact analysis (requirements/design/code/tests) -> cost/benefit -> gate decision with rationale -> baseline update + traceability refresh
  NOT: changing the baseline without a CR; accepting a CR without impact analysis; rejecting without rationale; updating the baseline without related artifacts
Stop:
  impact analysis matches actual effort within +/-30%; baseline synchronized with reality
Checks:
  CR with id/source/description; impact analysis signed by a developer; explicit decision with rationale; baseline updated (version, date, changes)
Antipatterns:
  Change by phone call — "add field X", no CR, no impact assessment
  All changes accepted — automatic approve without trade-off, backlog bloats
Continues:
  full cycle: re-elicit, re-spec, re-validate, re-prioritize, re-trace
Reopen:
  CR implemented and baseline updated; CR rejected/deferred and its relevance window expired (stale)
```