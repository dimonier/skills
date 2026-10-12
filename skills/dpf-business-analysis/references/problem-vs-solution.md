---
id: BAR.ProblemVsSolutionSeparation
title: Разделение проблемы и решения
status: seed
keywords: [problem, solution, framing, requirement, solution-neutrality]
dependencies:
  builds_on: [C.22.2, A.7]
  coordinates_with: [A.0, C.2.1, G.9]
---

## BAR.ProblemVsSolutionSeparation - Разделение проблемы и решения

> **Trigger:** Стейкхолдер формулирует требование как «постройте мне кнопку X» (решение), а не «я не могу сделать Y за Z минут» (проблема).

---

### BAR.ProblemVsSolutionSeparation:1 - Problem frame

Use this pattern at the entry to a project/iteration: turn stakeholder input into
requirements by separating problem description from solution description, before
anything goes to design.

**ContextGrounding** — работа бизнес-аналитика на входе в проект/итерацию:
получение входа от стейкхолдеров и превращение его в требования, пригодные для
передачи в разработку.

**ScopeCut** — разделение problem description и solution description на этапе
elicitation и analysis; **не** охватывает архитектурное проектирование решения.

### BAR.ProblemVsSolutionSeparation:2 - Problem

**ProblemSignal** — стейкхолдер формулирует требование как «постройте мне кнопку X»
(решение), а не «я не могу сделать Y за Z минут» (проблема); команда начинает
проектировать и реализовывать решение, не поняв проблему; реализованное решение
не решает действительную проблему стейкхолдера.

**SymptomDetection** — стейкхолдер говорит «добавьте поле X на форму Y» (решение);
бизнес-аналитик не спрашивает «какую задачу вы решаете с помощью поля X?»; команда
спорит о средствах (стек, фреймворк), а не о целях.

**ProblemHypothesis** — бизнес-аналитик не проводит problem framing: принимает
solution-shaped request как requirement, пропуская шаг «какая потребность/проблема
стоит за этим решением».

### BAR.ProblemVsSolutionSeparation:3 - Forces

| Force | Settlement |
|---|---|
| «Заказчик сказал — делаем» vs обязанность понять проблему | Solution-shaped request не принимается за требование без problem context |
| Полнота анализа vs бесконечный five-whys | Достаточно одного уровня problem context; это не стратегический консалтинг |
| Скорость передачи в разработку vs цена «сделали не то» | Problem framing до проектирования; цель — устранить самый дорогой дефект |

### BAR.ProblemVsSolutionSeparation:4 - Solution

**EntityOfConcern** — требование как эпистемический артефакт: описание потребности
или ограничения, из которого выводимы критерии приёмки, **не** описание реализации.

**AcceptanceCriterion** — для требования зафиксированы: (1) problem statement
(наблюдаемая проблема или потребность), (2) кто и в какой ситуации её испытывает,
(3) как измеряется наличие проблемы сейчас, (4) что считается её решением
(acceptance criteria), (5) rejected alternatives с причинами отклонения.

**MandatoryConstraints** — запрещено принимать solution-shaped request за требование
без problem context; запрещено фиксировать requirement как «реализовать
функциональность F» без указания, какую потребность F удовлетворяет.

**CharacterizationRelation** — problem clarity (сторонний читатель восстанавливает
проблему из требования), solution neutrality (свобода от предписанного решения),
testability (выводимость критериев приёмки).

### BAR.ProblemVsSolutionSeparation:5 - Archetypal Grounding

**Show.** В fintech-проекте стейкхолдер запросил «кнопку экспорта в Excel с фильтрацией
и группировкой». Problem framing вскрыл: менеджер тратит 3 часа в неделю на ручную
сверку данных из трёх систем. Отделённая от решения проблема — противоречивость
данных, а не отсутствие экспорта — привела к scheduled reconciliation pipeline:
время сверки сокращено с 3 часов до 5 минут.

### BAR.ProblemVsSolutionSeparation:6 - Bias-Annotation

**NotWishReason** — «Заказчик сказал — делаем»: принятие solution-shaped request как
требования без анализа проблемы.

**Near-Miss (boundary, not this pattern).** Problem statement записан и подтверждён,
но выяснилось: проблема не в отсутствии экспорта, а в противоречивости данных. Это
не ошибка problem framing, а ошибка elicitation — не выявлен root cause → применяется
`BAR.RequirementElicitation`.

### BAR.ProblemVsSolutionSeparation:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.PVS-1` | Зафиксирован problem statement: наблюдаемая проблема, кто испытывает, как измеряется сейчас | AcceptanceCriterion пп. (1)-(3) |
| `CC-BAR.PVS-2` | Зафиксировано, что считается решением (acceptance criteria) | AcceptanceCriterion п. (4) |
| `CC-BAR.PVS-3` | Зафиксированы rejected alternatives с причинами отклонения | AcceptanceCriterion п. (5) |
| `CC-BAR.PVS-4` | Ни одно требование не зафиксировано как «реализовать F» без потребности | MandatoryConstraints |

### BAR.ProblemVsSolutionSeparation:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Specification disguised as problem statement** | Problem statement: «время отклика ≤ 2 сек» — спецификация под видом framing | AcceptanceCriterion требует наблюдаемую проблему + субъекта + текущее состояние |
| **Problem framing as infinite regress** | Цепочка «five whys» до стратегии компании; спецификация задерживается неделями | ScopeCut: один уровень problem context, не стратегический консалтинг |

### BAR.ProblemVsSolutionSeparation:9 - Consequences

**ImprovementCheck** — каждое требование имеет problem context; стейкхолдер
подтверждает problem description; rejected alternatives зафиксированы.

**ValidationBoundary** — проверка на `≥3` требованиях из разных областей; refresh
при обнаружении, что принятое решение не решает проблему.

**FreshnessOrExpiry** — `stale` при изменении бизнес-процесса или потребностей,
делающем problem statement неактуальным. **ReadinessDisposition** — `P2W-ready` для
передачи в спецификацию и проектирование.

### BAR.ProblemVsSolutionSeparation:10 - Rationale

Предотвратить самый дорогой дефект — «сделали не то» (решение правильное, проблема
— не та): стоимость перепроектирования решения выше стоимости любого дефекта
формулировки.

### BAR.ProblemVsSolutionSeparation:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 6 (Strategy Analysis) — framing до solution design | Adopt | AcceptanceCriterion требует problem statement раньше solution description | Reopen on BABOK v4 |
| BABOK v3, ch. 7 (Analysis & Design) — need ≠ solution | Adopt | MandatoryConstraints запрещают solution-shaped request | Reopen on BABOK v4 |
| IREB CPRE FL, ch. 3 (Elicitation) — problem analysis vs solution design | Adopt | ScopeCut воспроизводит разделение этапов | Reopen on CPRE FL update |

### BAR.ProblemVsSolutionSeparation:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.ProblemVsSolutionSeparation:End