# BAR.StakeholderIdentification — Identifying stakeholders and their concerns

> **Trigger:** Requirements are gathered only from one or two "loud" stakeholders; the missed ones surface at acceptance with "that's not what I wanted."

```episteme id="BAR.StakeholderIdentification" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: C.22.2, C.11
  coordinates_with: A.2, A.2.1, C.16, G.9
UseThisWhen:
  at the start of requirements work, where the system has >=3 interest groups (business, operations, security, regulator, adjacent systems)
  not when only specification/validation of a single requirement is needed
Result:
  stakeholder register / onion model: id, role (requirements owner / constraints owner / consulted / informed), concern(s), channel, acceptance authority
  ready input for elicitation
Solution:
  build the stakeholder map/onion model before elicitation
  surface holder constraints (security, operations, regulator) and negative stakeholders, even with limited access
  record for each: concern and the channel for obtaining requirements
  NOT: restricting to "positive" stakeholders
Stop:
  every functional area has a requirements holder and a constraints holder; time to detect a missed stakeholder shrinks
Checks:
  register contains id, role, concern, channel, acceptance authority
  functional areas covered; holder constraints explicitly identified; negatives recorded with reason when access is limited
Antipatterns:
  Stakeholder proxy substitution — PO interviewed "on behalf of everyone"; constraint roles recorded from the PO's words
  Positive-stakeholder bias — only "friendly" ones in the register; holder constraints missed
Continues:
  BAR.RequirementElicitation (from the identified stakeholders)
Reopen:
  change in org structure, regulatory field, or adjacent-system composition (stale)
```