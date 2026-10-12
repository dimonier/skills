# BAR.UseCaseModeling — Modeling use cases

> **Trigger:** Use cases are written as "the user presses button X, the system shows screen Y" — a UI spec, not a description of the user's goal; alternative flows omitted.

```episteme id="BAR.UseCaseModeling" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: C.22.2, A.2
  coordinates_with: A.2.1, A.21, C.25, C.27
UseThisWhen:
  use case modeling as a technique for specifying functional requirements; >=3 actor types
  not when UML notation, code generation, or scenario testing is needed
Result:
  goal-driven use case: goal statement, verifiable pre/post-conditions, extensions, without UI details
  ready input for development, testing, acceptance
Solution:
  start from the goal statement: "Actor X achieves goal Y"; steps in "actor intention -> system responsibility" form
  extensions for every step (business rules, failures, timeouts); verifiable and distinct pre/post-conditions
  NOT: describing as UI actions; a use case without extensions; pre/post-conditions without criteria; mixing actor goals
Stop:
  a tester writes test cases for main + extensions with no clarification; extensions cover >=90% of failure modes
Checks:
  goal statement; UI-neutrality; extension conditions for every step; testability without clarification
Antipatterns:
  Use case as UI flow — a sequence of screens without the actor's goal
  Happy path without extensions — "if an error occurs, show a message" without a failure condition
Continues:
  BAR.RequirementSpecification, BAR.RequirementValidation
Reopen:
  change in process affecting the actor's goal (stale)
```