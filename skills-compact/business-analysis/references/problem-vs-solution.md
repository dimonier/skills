# BAR.ProblemVsSolutionSeparation — Separating problem and solution

> **Trigger:** A stakeholder states the requirement as "build me button X" (a solution) rather than "I can't do Y within Z minutes" (a problem).

```episteme id="BAR.ProblemVsSolutionSeparation" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: C.22.2, A.7
  coordinates_with: A.0, C.2.1, G.9
UseThisWhen:
  at project/iteration entry: turning stakeholder input into requirements for development
  not when solution architecture design is needed
Result:
  requirement with problem context: problem statement (the problem, who and in what situation, how it is measured now), acceptance criteria, rejected alternatives
  ready input for specification
Solution:
  separate the problem description from the solution description
  record: (1) problem statement, (2) who experiences it, (3) current measure, (4) what counts as solved, (5) rejected alternatives with reasons
  NOT: accepting a solution-shaped request as a requirement without problem context; recording "implement F" without a need
  one level of problem context is enough — not strategic consulting
Stop:
  an outside reader reconstructs the problem from the requirement; acceptance criteria are derivable from it
Checks:
  problem statement + acceptance criteria + rejected alternatives recorded
  no requirement is written as "implement F" without a need
Antipatterns:
  Specification disguised as problem statement — "response time <= 2 s" under the guise of problem framing
  Problem framing as infinite regress — five-whys to strategy, specification delayed for weeks
Continues:
  BAR.RequirementSpecification, BAR.RequirementPrioritization
Reopen:
  change in business process/needs making the problem statement stale
```