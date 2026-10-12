---
id: BAR.BusinessProcessModeling
title: Моделирование бизнес-процессов как источник требований
status: seed
keywords: [process-modeling, bpmn, as-is, to-be, traceability]
dependencies:
  builds_on: [A.3.4, E.17]
  coordinates_with: [C.27, A.10, C.30, C.16]
---

## BAR.BusinessProcessModeling - Моделирование бизнес-процессов как источник требований

> **Trigger:** Бизнес-процессы моделируются как самоцель: диаграммы «лежат на полке»; модель процесса не содержит ссылок на требования; процесс и спецификация — в разных «мирах».

---

### BAR.BusinessProcessModeling:1 - Problem frame

Use this pattern in an automation/digitalization project where the business process is
the main source of functional requirements: treat the process model as a structured
input for requirement elicitation, not as a self-sufficient artifact.

**ScopeCut** — моделирование процесса (BPMN/EPC/UML Activity) как техника выявления
и обоснования требований; **не** охватывает BPM-автоматизацию (BPMS), имитационное
моделирование, организационный дизайн.

### BAR.BusinessProcessModeling:2 - Problem

**ProblemSignal** — процессы моделируются как самоцель: as-is/to-be диаграммы «лежат
на полке»; модель не содержит ссылок на требования; изменение процесса не вызывает
обновления требований.

**SymptomDetection** — аналитик рисует BPMN, но не может показать, какое требование
вытекает из конкретного activity; при изменении процесса разработчики не знают
затронутые требования; to-be описан, но система автоматизирует as-is.

**ProblemHypothesis** — моделирование не интегрировано в работу с требованиями:
диаграмма создаётся «для галочки», а не как structured input для elicitation.

### BAR.BusinessProcessModeling:3 - Forces

| Force | Settlement |
|---|---|
| «Нарисуем BPMN — требования появятся сами» vs методика извлечения | Связь каждого элемента с требованием |
| To-be сразу vs as-is baseline | Запрет to-be без as-is baseline и problem statement |
| Модель как артефакт vs модель как источник | Traceability link «элемент процесса → требование» |

### BAR.BusinessProcessModeling:4 - Solution

**EntityOfConcern** — модель бизнес-процесса как эпистемический артефакт, из которого
извлекаются требования: процесс не самоцель, а carrier требований к автоматизирующей
системе.

**AcceptanceCriterion** — (1) для каждого системо-взаимодействующего элемента — ≥1
требование; (2) для каждого gateway — бизнес-правило; (3) связь «элемент → требование»
задокументирована; (4) изменение процесса даёт список затронутых требований за ≤30
минут; (5) as-is зафиксирован как baseline; to-be содержит rationale каждого изменения.

**MandatoryConstraints** — запрещено моделировать to-be без as-is baseline; запрещена
модель без traceability links до требований; запрещено «оптимизировать процесс»
(to-be) без problem statement.

**CharacterizationRelation** — process-to-requirement coverage, model granularity
adequacy, freshness, requirement derivation velocity.

### BAR.BusinessProcessModeling:5 - Archetypal Grounding

**Show.** Розничный банк: as-is модель процесса «выдача кредита» выявила 40% ручных
шагов (переключение АБС/CRM, ручная сверка с БКИ, бумажное согласование). Каждый
ручной шаг стал источником требования (интеграция с БКИ, электронный маршрут
согласования). Связь «элемент → требование» в traceability matrix позволила при
изменении регламента ЦБ за ≤30 минут определить затронутые требования.

### BAR.BusinessProcessModeling:6 - Bias-Annotation

**NotWishReason** — «Нарисуем процесс в BPMN — и требования появятся сами»: без
методики извлечения требований и связи элементов модели с требованиями.

**Near-Miss (boundary, not this pattern).** BPMN закупок нарисована, требования
извлечены, но 30% заявок возвращаются — номенклатурный справочник не синхронизирован.
Это не misuse процесса, а дефект `BAR.DataRequirements` (master data не выявлены).

### BAR.BusinessProcessModeling:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.BPM-1` | Для системо-взаимодействующего элемента ≥1 traceability link до требования | Процесс как источник требований |
| `CC-BAR.BPM-2` | As-is baseline; to-be с rationale каждого изменения | Запрет to-be без as-is |
| `CC-BAR.BPM-3` | Изменение процесса даёт затронутые требования за ≤30 минут | Impact analysis через процесс |
| `CC-BAR.BPM-4` | Другой аналитик восстанавливает сопоставимый набор требований | Модель как воспроизводимый источник |

### BAR.BusinessProcessModeling:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **BPMN как самоцель** | Два месяца диаграмм; требований нет, links нет | Traceability link для каждого элемента |
| **To-be без as-is baseline** | «Целевой» процесс без проблематизации as-is | Запрет to-be без as-is baseline и problem statement |

### BAR.BusinessProcessModeling:9 - Consequences

**ImprovementCheck** — каждый элемент процесса прослеживается до требования;
изменение процесса идентифицирует затронутые требования.

**ValidationBoundary** — другой аналитик по модели восстанавливает требования;
refresh при изменении регламента/оргструктуры/системы.

**FreshnessOrExpiry** — `stale` при изменении процесса без обновления модели и
требований. **ReadinessDisposition** — `P2W-ready` как structured input для elicitation.

### BAR.BusinessProcessModeling:10 - Rationale

Связать моделирование процесса и требования, чтобы изменение процесса не вызывало
«слепых» изменений в системе.

### BAR.BusinessProcessModeling:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 10.35 (Process Modeling) | Extended | Mandatory traceability + запрет to-be без as-is | Reopen on BABOK v4 |
| Silver, BPMN Method and Style (уровни моделирования) | Adapt | Уровни как carrier; problem-side framing | Reopen on source revision |

### BAR.BusinessProcessModeling:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.BusinessProcessModeling:End