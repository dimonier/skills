---
name: dpf-business-analysis
description: |
  Business Analysis & Requirements Engineering. Use when: identifying stakeholders,
  eliciting or specifying requirements, prioritizing, validating, tracing, or managing
  requirements changes. Depends on fpf-core.
---

# DPF: Business Analysis & Requirements Engineering

**Depends on:** `fpf-core`
**Bounded context:** Business Analysis in engineering projects
**Source of truth:** `assets/BABusinessAnalysis-dpf.md`

## When to load each pattern

| Situation | Load | Governing cues → fpf-core |
|---|---|---|
| Stakeholder identification | `references/stakeholder-identification.md` | C.22.2, C.11 |
| Separating problem and solution | `references/problem-vs-solution.md` | A.16, C.22.2 |
| Requirements elicitation | `references/requirement-elicitation.md` | C.22.2, A.10 |
| Requirements specification | `references/requirement-specification.md` | E.8, A.19 |
| Requirements prioritization | `references/requirement-prioritization.md` | A.19, C.18 |
| Requirements validation | `references/requirement-validation.md` | A.10, B.3 |
| Requirements traceability | `references/requirement-traceability.md` | A.10, E.4.PFR |
| Requirements change management | `references/requirement-change-management.md` | E.23, G.2 |
| Business process modeling | `references/business-process-modeling.md` | E.17, C.30 |
| Use case modeling | `references/use-case-modeling.md` | E.17, E.8 |
| Data requirements | `references/data-requirements.md` | A.19, A.10 |
| Security requirements | `references/security-requirements.md` | B.3, A.20 |

## Source for agent vs human

- **Agent**: always use `references/`. DO NOT read `assets/BABusinessAnalysis-dpf.md`.
- **Human**: read and edit the canonical monolith `assets/BABusinessAnalysis-dpf.md`. After edits — rebuild `references/`.

## references/ status

**Ready** — 12 problem cards + INDEX + relations.
