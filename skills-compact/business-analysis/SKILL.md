---
name: dpf-business-analysis
description: |
  Business Analysis & Requirements Engineering (compacted runtime projection). Use when:
  identifying stakeholders, eliciting or specifying requirements, prioritizing, validating,
  tracing, or managing requirements changes. Depends on fpf-core.
---

# DPF: Business Analysis & Requirements Engineering (compacted)

**Depends on:** `fpf-core`
**Bounded context:** Business Analysis in engineering projects — the problem-side of
eliciting, specifying, prioritizing, validating, tracing and changing requirements.
**Readiness mode (collective, whole package):** `source-faithful` — read against the
compacted threshold (runtime allow-list + LEAK/DROP-free split + complete routing +
`Grounding (FPF)` slot per card + canonical-source citation). No card has passed `E.21`;
this package is **not** `case-validated`.

## When to load which pattern

| Situation | Load |
|---|---|
| Requirements gathered only from "loud" stakeholders; holder constraints missed | `references/stakeholder-identification.md` |
| Stakeholder states a solution ("build button X"), not a problem | `references/problem-vs-solution.md` |
| Tacit requirements not surfaced; techniques chosen unsystematically | `references/requirement-elicitation.md` |
| A requirement cannot be verified; different readers interpret it differently | `references/requirement-specification.md` |
| Backlog of 200+ "critical" requirements; priority decided by voting | `references/requirement-prioritization.md` |
| At demo the stakeholder: "that's not what I meant"; feasibility unchecked | `references/requirement-validation.md` |
| Cannot answer "why are we doing this?"; impact analysis impossible | `references/requirement-traceability.md` |
| Changes made "by phone call"; scope creep untracked | `references/requirement-change-management.md` |
| Process model "shelved" with no traceability to requirements | `references/business-process-modeling.md` |
| Use case = UI spec; extensions omitted | `references/use-case-modeling.md` |
| Data requirements = field list without validation rules and privacy | `references/data-requirements.md` |
| Security requirements reduced to "authorization" without a threat model | `references/security-requirements.md` |

## Navigation rule

Start from the working difficulty, not from file order. Load the matching card, then
follow `Continues`/`Reopen` lines in its body. The dominant chain follows the requirements
life cycle: `stakeholder-identification` → `requirement-elicitation` →
`problem-vs-solution` → `requirement-specification` → (`requirement-prioritization`,
`requirement-validation`, `requirement-traceability`) → `requirement-change-management`;
four source-of-requirements techniques branch before specification:
`business-process-modeling`, `use-case-modeling`, `data-requirements`, `security-requirements`.
