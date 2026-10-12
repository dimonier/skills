---
id: BAR.RequirementChangeManagement
title: Управление изменениями требований
status: seed
keywords: [change-management, change-request, impact-analysis, baseline, scope-creep]
dependencies:
  builds_on: [C.22.2, A.21]
  coordinates_with: [A.10, C.32.ADR, G.5, G.11, G.9, C.28, C.27]
---

## BAR.RequirementChangeManagement - Управление изменениями требований

> **Trigger:** Новые требования добавляются «по звонку» без оценки влияния; scope creep не отслеживается — проект делает в 2× больше, а ключевая функциональность не готова.

---

### BAR.RequirementChangeManagement:1 - Problem frame

Use this pattern when a project is in active development (>3 months) with ≥2
stakeholders supplying new and changed requirements: route every change through an
explicit change-control gate rather than ad-hoc mutation.

**ScopeCut** — управление изменениями отдельного требования или группы связанных
требований; **не** охватывает управление контрактом и бюджетирование.

### BAR.RequirementChangeManagement:2 - Problem

**ProblemSignal** — требования добавляются «по звонку» без оценки влияния; scope
creep не отслеживается; изменение не сопровождается change impact analysis.

**SymptomDetection** — заказчик просит «небольшое изменение» — затронуты 5 модулей и
20 тестов; baseline требований отсутствует; объём незавершённых изменений растёт
быстрее, чем закрываются.

**ProblemHypothesis** — отсутствует formal change control process: изменения
принимаются ad-hoc, без impact analysis, traceability update и пересмотра приоритетов.

### BAR.RequirementChangeManagement:3 - Forces

| Force | Settlement |
|---|---|
| «Мы agile — изменения приветствуются» vs cost-of-change | Изменение принимается, но с оценкой стоимости и влияния |
| Принять всё vs gate decision | Explicit decision (accept/defer/reject) с rationale |
| Изменить baseline vs синхронизировать артефакты | Нельзя обновлять baseline без обновления design/test |

### BAR.RequirementChangeManagement:4 - Solution

**EntityOfConcern** — change request как problem card особого типа: сигнал о
необходимости изменения, проходящий gate decision до принятия в работу.

**AcceptanceCriterion** — для каждого CR: идентификатор, источник, описание, причина,
impacted artifacts, оценка усилий, решение (accepted/deferred/rejected) с rationale,
статус; baseline обновлён; traceability links актуализированы; инициатор
проинформирован.

**MandatoryConstraints** — запрещено вносить изменение в baseline без change request;
запрещён CR без impact analysis; запрещено отказывать без rationale; запрещено
обновлять baseline без обновления связанных артефактов.

**CharacterizationRelation** — change request throughput, impact analysis accuracy,
baseline stability, scope creep rate.

### BAR.RequirementChangeManagement:5 - Archetypal Grounding

**Show.** Телеком мигрирует биллинг под регуляторный дедлайн. За 30 дней до запуска
директор требует «real-time уведомления о расходах» (оценка: 4 недели). Change
control: `CR-77` зафиксирован, impact analysis выявляет 3 модуля и конфликт с
регуляторной отчётностью, gate decision: deferred с rationale. Миграция укладывается
в дедлайн; уведомления доставлены пост-релизом без срыва compliance.

### BAR.RequirementChangeManagement:6 - Bias-Annotation

**NotWishReason** — «Мы agile — изменения приветствуются»: без оценки cost-of-change и
проверки, не ломает ли изменение работающую функциональность.

**Near-Miss (boundary, not this pattern).** CR оформлен, impact analysis (1 модуль, 3
теста), но библиотека PDF конфликтует с лицензией продукта — изменение rejected.
Change control сработал; проблема — неполнота стейкхолдеров (юрдепартамент не
идентифицирован как holder constraint) → `BAR.StakeholderIdentification`.

### BAR.RequirementChangeManagement:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.CHM-1` | Изменение baseline оформлено как CR с идентификатором | Предотвращает «изменения по звонку» |
| `CC-BAR.CHM-2` | CR содержит impact analysis, подписанный разработчиком | Предотвращает слепые изменения |
| `CC-BAR.CHM-3` | Explicit решение с documented rationale | Предотвращает «все изменения принимаются» |
| `CC-BAR.CHM-4` | Baseline обновлён: версия, дата, список изменений | Предотвращает расхождение baseline и реальности |

### BAR.RequirementChangeManagement:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Изменение по звонку** | «Добавь поле X», CR не оформлен; через месяц никто не помнит почему | Запрет mutation baseline без CR |
| **Все изменения принимаются** | Automatic approve; backlog разбухает | Gate decision с reject/defer и rationale |

### BAR.RequirementChangeManagement:9 - Consequences

**ImprovementCheck** — каждое изменение проходит: capture → impact analysis →
cost/benefit → gate decision → baseline update + traceability refresh.

**ValidationBoundary** — impact analysis соответствует фактическим усилиям с точностью
`±30%`; refresh при каждом изменении baseline.

**FreshnessOrExpiry** — `stale` если CR реализован и baseline обновлён; `stale` если
CR rejected/deferred и истёк срок актуальности. **ReadinessDisposition** — `P2W-ready`
для внедрения change control.

### BAR.RequirementChangeManagement:10 - Rationale

Остановить неконтролируемый scope creep до того, как он сделает проект
неуправляемым по срокам и стоимости.

### BAR.RequirementChangeManagement:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 5 (Manage Changes) — capture → impact → gate → baseline | Adopt | AcceptanceCriterion воспроизводит flow | Reopen on BABOK v4 |
| BABOK v3, ch. 6 (Scope Management) — baseline как анти-scope-creep | Adopt | SolvabilityBand: feasible при baseline | Reopen on BABOK v4 |
| IREB CPRE FL, ch. 9 (Management) — lifecycle CR, синхронизация артефактов | Adopt | Traceability refresh при изменении baseline | Reopen on CPRE FL update |

### BAR.RequirementChangeManagement:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.RequirementChangeManagement:End