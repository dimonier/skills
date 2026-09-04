---
id: PV.Agenda
title: "Повестка следующей встречи: топ-вопросы, блокеры, противоречия, риски, слоты решений"
status: seed
readiness: source-faithful
keywords: [agenda, meeting, open-questions, blockers, revisit, deferred]
dependencies:
  builds_on:
    - E.9
    - E.23
  coordinates_with:
    - A.15.2
---

## PV.Agenda - Повестка следующей встречи: топ-вопросы, блокеры, противоречия, риски, слоты решений

> **Trigger:** Когда владелец просит подготовить повестку следующей встречи (`project-vault/agenda-next.md`).
> **Governing FPF patterns:**
>   → E.9 (DRR — возврат `proposed`/`deferred` к решению)
>   → E.23 (цикл улучшения — возврат к открытым пунктам)
> **Skill dependencies:**
>   → нет

---

### PV.Agenda:1 - Problem frame

Use this pattern to assemble the next-meeting agenda from the vault's open items:
top questions, blockers, contradictions, risks, and decision slots from
`proposed`/`deferred` decisions with approaching `revisit_by`.

### PV.Agenda:2 - Problem

Повестка, собранная «из головы», пропускает открытые пункты хранилища: открытые
вопросы, противоречия, риски, отложенные решения с подходящим `revisit_by`.
Повестка должна выводиться из vault, а не сочиняться.

### PV.Agenda:3 - Forces

| Force | Settlement |
|---|---|
| Выводимость vs сочинение | Повестка собирается из открытых сущностей vault. |
| Пусто vs заполнено | Нет открытых пунктов → только слот «0–5 Goal» + «agenda empty — no open items». |
| Off-limits vs запрос | Повестка — только по явному запросу владельца. |

### PV.Agenda:4 - Solution

Обновить `project-vault/agenda-next.md` по шаблону `templates/agenda.md`: топ
вопросов, блокеры, противоречия, риски; слоты из `project-vault/decisions/`
(закрыть `proposed`, вернуть `deferred` с приближающимся `revisit_by`).

**Когда блокировано:**
- `agenda-next.md` ещё нет → создать из шаблона.
- Нет открытых вопросов/рисков/противоречий → заполнить только слот «0–5 Goal»
  и пометить «agenda empty — no open items».

### PV.Agenda:5 - Archetypal Grounding

**Show.** Повестка в этом проекте собирается по запросу из открытых Q/RISK/CON и
слотов `proposed`/`deferred` решений, а не сочиняется вручную.

### PV.Agenda:6 - Bias-Annotation

Соблазн — готовить повестку заранее «на всякий случай», даже без запроса, и
соблазн — дополнять её пунктами, которых нет в хранилище. Противовесы: повестка
off-limits без запроса и выводится из vault.

### PV.Agenda:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-AG.1 | Повестка создаётся/обновляется только по явному запросу. |
| CC-AG.2 | Пункты выводятся из открытых сущностей vault (Q/RISK/CON + слоты решений). |
| CC-AG.3 | Пустая повестка — только слот «0–5 Goal» + «agenda empty». |

### PV.Agenda:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Повестка без запроса | Не создавать/не обновлять. |
| Пункты не из vault | Выводить из открытых сущностей. |

### PV.Agenda:9 - Consequences

Повестка всегда соответствует текущему состоянию хранилища, но требует явного
запроса и выводимости открытых пунктов. Возврат `deferred`/`proposed` решений —
механизм `E.9` (revisit).

### PV.Agenda:10 - Rationale

`E.9` — решения с `revisit_by` возвращаются в повестку для подтверждения/отмены;
`E.23` — цикл возврата к открытым пунктам. Отсюда — повестка как проекция
открытого состояния vault, а не отдельный сочинённый документ.

### PV.Agenda:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.9` (DRR revisit) | Adopt | Слоты `proposed`/`deferred` с `revisit_by` | Reopen при ревизии `E.9` |
| FPF `E.23` (цикл возврата) | Adopt | Повестка из открытых пунктов | Reopen при ревизии `E.23` |

Best-known line: повестка как проекция открытого состояния. Rejected rival:
«сочинённая заранее повестка» — отброшена.

### PV.Agenda:12 - Relations

- **Builds on:** `E.9` (revisit решений), `E.23` (возврат к открытым пунктам).
- **Coordinates with:** `A.15.2` (планирование).
- **Specialized by:** `PV.StateUpdate` (закрытие proposed/deferred), `PV.VaultSchema` (agenda-next.md как файл).

### PV.Agenda:End
