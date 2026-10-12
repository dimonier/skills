---
id: BAR.RequirementValidation
title: Валидация требований
status: seed
keywords: [validation, verification, feasibility, testability, sign-off]
dependencies:
  builds_on: [A.7, C.22.2]
  coordinates_with: [C.24, A.21, C.16, C.25]
---

## BAR.RequirementValidation - Валидация требований

> **Trigger:** На демо стейкхолдер говорит «это не то, что я имел в виду»; разработка обнаруживает нереализуемое ограничение через месяц.

---

### BAR.RequirementValidation:1 - Problem frame

Use this pattern to check requirements for correctness, completeness, feasibility and
testability **before** they go to development — validation («are we building the right
system?»), distinct from verification («are we building the system right?»).

**ScopeCut** — валидация требований; **не** охватывает приёмочное тестирование
(верификацию реализации).

### BAR.RequirementValidation:2 - Problem

**ProblemSignal** — спринт потрачен на реализацию, а на демо стейкхолдер: «это не
то, что я имел в виду»; требование задокументировано, но не проверено на
выполнимость — нереализуемое ограничение вскрывается через месяц; acceptance
criteria не тестируемы.

**SymptomDetection** — стейкхолдер отклоняет реализованное на demo/review; требование
содержит contradicting constraints («доступна 24/7» и «профилактика каждую ночь в
3:00»); «это нельзя сделать заявленным способом» через 3 недели.

**ProblemHypothesis** — валидация не систематична: команда полагается на устное «да,
всё верно» без structured validation (walkthrough, inspection, prototyping, test-case
derivation).

### BAR.RequirementValidation:3 - Forces

| Force | Settlement |
|---|---|
| «Записали со слов заказчика — значит верно» vs signed off criteria | Acceptance criteria signed off стейкхолдером |
| Валидация аналитиком vs реализуемость | Feasibility check с implementer role |
| Демо прототипа vs structured validation | Проверка problem statement + testability + consistency, не only approval wireframe |

### BAR.RequirementValidation:4 - Solution

**EntityOfConcern** — валидированный набор требований: прошедший проверку на
stakeholder agreement, feasibility, testability, consistency, completeness.

**AcceptanceCriterion** — для каждого требования: (1) stakeholder signed off problem
statement и acceptance criteria, (2) feasibility check пройден (architecture spike при
высоком риске), (3) test-case derivation выполнен, (4) consistency check с зависимыми
требованиями пройден; для набора — отсутствуют неразрешённые конфликты.

**MandatoryConstraints** — запрещено передавать в разработку без signed-off acceptance
criteria; запрещено пропускать feasibility check для высокорисковых требований;
запрещена валидация без implementer role (разработчик/архитектор).

**CharacterizationRelation** — stakeholder agreement rate, feasibility risk coverage,
testability rate, consistency conflicts found (до vs после реализации).

### BAR.RequirementValidation:5 - Archetypal Grounding

**Show.** Логистическая компания, требование «растаможивание в реальном времени с
откликом ≤ 5 секунд». Feasibility spike до фиксации в бэклоге: архитектор за 2 дня
обнаруживает, что таможенный API отвечает 12–18 секунд под нагрузкой. Требование
пересогласовано на «асинхронное растаможивание с уведомлением в течение 5 секунд
после ответа API». Три месяца wasted development предотвращены.

### BAR.RequirementValidation:6 - Bias-Annotation

**NotWishReason** — «Мы записали требования со слов заказчика, значит, они
правильные»: отказ от валидации под видом «заказчик всегда прав».

**Near-Miss (boundary, not this pattern).** Стейкхолдер отверг функциональность:
ожидал локального сохранения, система отправляла на сервер. Criteria были signed
off, feasibility проверен — скрытое ожидание не выявлено при elicitation → паттерн
валидации не защищает от требований, отсутствующих в спецификации.

### BAR.RequirementValidation:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.VAL-1` | Acceptance criteria signed off стейкхолдером | Предотвращает «это не то, что я имел в виду» |
| `CC-BAR.VAL-2` | Feasibility check пройден; spike при высоком риске | Предотвращает нереализуемое через недели разработки |
| `CC-BAR.VAL-3` | Test-case derivation без разъяснений | Предотвращает «нетестируемые» требования |
| `CC-BAR.VAL-4` | Валидация с участием implementer role | Предотвращает «валидацию без разработчика» |

### BAR.RequirementValidation:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Валидация = демо прототипа** | «Выглядит хорошо» → валидировано, без проверки criteria/feasibility | Structured validation, не approval wireframe |
| **Валидация без разработчика** | Через 2 недели: «невыполнимо на текущем стеке» | Feasibility с implementer role |

### BAR.RequirementValidation:9 - Consequences

**ImprovementCheck** — каждое требование проходит checklist: stakeholder confirm,
feasibility, testability, consistency.

**ValidationBoundary** — доля требований с переделкой из-за validation defect; refresh
при изменении требований.

**FreshnessOrExpiry** — `stale` если требование изменено без повторной валидации.
**ReadinessDisposition** — `P2W-ready` (gate: requirement accepted for implementation).

### BAR.RequirementValidation:10 - Rationale

Устранить validation defects до того, как их стоимость станет неприемлемой: gate
decision до инвестиций в реализацию.

### BAR.RequirementValidation:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 5 (Validate Requirements) — alignment, feasibility, testability | Adopt | AcceptanceCriterion | Reopen on BABOK v4 |
| IREB CPRE FL, ch. 8 — validation vs verification | Adopt | ScopeCut: strict distinction | Reopen on CPRE FL update |
| Pohl 2010 / Boehm 1981 — «right system» vs «system right» | Adopt as-is | ScopeCut + governing cues | Reopen on source revision |

### BAR.RequirementValidation:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.RequirementValidation:End