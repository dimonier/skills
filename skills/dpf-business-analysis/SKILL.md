---
name: dpf-business-analysis
description: |
  Business Analysis & Requirements Engineering. Use when: identifying stakeholders,
  eliciting or specifying requirements, prioritizing, validating, tracing, or managing
  requirements changes. Depends on fpf-core.
---

# DPF: Business Analysis & Requirements Engineering

**Depends on:** `fpf-core`
**Bounded context:** Business Analysis in engineering projects — the problem-side
of eliciting, specifying, prioritizing, validating, tracing and changing requirements.
**Single surface:** `references/` is the canonical source of every pattern body.
There is no `assets/` monolith and no separate reader-facing publication form.
**Consumer surface:** a runtime reader is obliged to read only this `SKILL.md` plus
the single `references/*.md` card the routing table names. `INDEX.md`,
`relations.md`, and the source/edition citation are reference-only
(authoring/verification material), not consumer obligations.

## When to load each pattern

| Situation | Load |
|---|---|
| Требования собираются только от «громких» стейкхолдеров; holders constraints пропущены | `references/stakeholder-identification.md` |
| Стейкхолдер формулирует решение («постройте кнопку X»), а не проблему | `references/problem-vs-solution.md` |
| Скрытые (tacit) требования не выявляются; техники выбираются бессистемно | `references/requirement-elicitation.md` |
| Требование нельзя проверить; разные читатели понимают его по-разному | `references/requirement-specification.md` |
| Backlog из 200+ «критичных» требований; приоритет решает голосование | `references/requirement-prioritization.md` |
| На демо стейкхолдер: «это не то, что я имел в виду»; feasibility не проверен | `references/requirement-validation.md` |
| Нельзя ответить «почему мы это делаем?»; impact analysis невозможен | `references/requirement-traceability.md` |
| Изменения вносятся «по звонку»; scope creep не отслеживается | `references/requirement-change-management.md` |
| Модель процесса «лежит на полке» без traceability до требований | `references/business-process-modeling.md` |
| Use case = UI-спецификация; extensions пропущены | `references/use-case-modeling.md` |
| Требования к данным = перечень полей без правил валидации и privacy | `references/data-requirements.md` |
| Требования безопасности сводятся к «авторизации» без threat model | `references/security-requirements.md` |

## Navigation rule

The dominant reading chain follows the requirements life cycle:
`stakeholder-identification` → `requirement-elicitation` → `problem-vs-solution` →
`requirement-specification` → (`requirement-prioritization`, `requirement-validation`,
`requirement-traceability`) → `requirement-change-management`. Four source-of-requirements
techniques branch before specification: `business-process-modeling`, `use-case-modeling`,
`data-requirements`, `security-requirements`. Load the single card a situation names in the
table above; each card's `:6 Bias-Annotation` names the neighbour pattern when the failure
turns out to belong to another card.

## references/ status

**Readiness mode (collective, whole package): `source-faithful`** — faithful to the
approved sources (BABOK v3, IREB CPRE FL, Wiegers/Beatty, Pohl, ISO/IEC/IEEE 29148,
ГОСТ 34, DAMA-DMBOK2, ISO 25012, Mead/OWASP) and to FPF Core. **Not `case-validated`:**
the package has no heterogeneous-case evaluation (`E.21`) yet. Each card's `status`
names only the level — all twelve cards are `seed` until they pass the package's
declared threshold. There is no separate monolith; `references/` is the single surface.