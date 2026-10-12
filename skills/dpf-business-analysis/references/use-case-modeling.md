---
id: BAR.UseCaseModeling
title: Моделирование вариантов использования
status: seed
keywords: [use-case, actor, goal, extension, ui-neutrality]
dependencies:
  builds_on: [C.22.2, A.2]
  coordinates_with: [A.2.1, A.21, C.25, C.27]
---

## BAR.UseCaseModeling - Моделирование вариантов использования

> **Trigger:** Use cases пишутся как «пользователь нажимает кнопку X, система показывает экран Y» — UI-спецификация, а не описание цели пользователя; альтернативные потоки пропущены.

---

### BAR.UseCaseModeling:1 - Problem frame

Use this pattern where use-case modelling is the specification technique for functional
requirements: write each use case as a goal-driven contract of actor behaviour, not as
a screen-flow description.

**ScopeCut** — use case modelling как техника спецификации функциональных требований
через цели акторов; **не** охватывает UML-нотацию как таковую, генерацию кода,
сценарное тестирование.

### BAR.UseCaseModeling:2 - Problem

**ProblemSignal** — use cases пишутся как «нажимает кнопку X, показывает экран Y»;
альтернативные потоки пропущены; pre/post-conditions не проверяемы; use case не
отвечает «какую цель достигает actor?».

**SymptomDetection** — «пользователь выбирает из выпадающего списка» (UI-деталь);
extension «если что-то пошло не так» без specific failure condition; post-condition
без проверяемых критериев; 40% сценариев не описаны.

**ProblemHypothesis** — use case modelling = описание UI-навигации вместо goal-driven
technique: аналитик не начинает с «какую цель преследует актор?».

### BAR.UseCaseModeling:3 - Forces

| Force | Settlement |
|---|---|
| UI-описание vs цель актора | Goal statement; запрет UI-деталей |
| Счастливый путь vs failure modes | Обязательные extension scenarios |
| «Напишем как получится» vs структура Кокбёрна | Проверяемые pre/post-conditions |

### BAR.UseCaseModeling:4 - Solution

**EntityOfConcern** — use case как goal-driven эпистемический артефакт: описание
поведения системы, приводящего к observable result of value для актора; не
UI-спецификация.

**AcceptanceCriterion** — (1) goal statement: «Actor X достигает цели Y»; (2)
pre-conditions проверяемы; (3) post-conditions проверяемы и различны для main/extension;
(4) main success на уровне «actor intention → system responsibility»; (5) для каждого
шага — extension conditions; (6) extensions покрывают бизнес-правила, отказы, таймауты;
(7) use case без UI-деталей.

**MandatoryConstraints** — запрещено описывать use case как UI-действия; запрещён use
case без extension scenarios; запрещены pre/post-conditions без проверяемых критериев;
запрещено смешивать цели разных акторов.

**CharacterizationRelation** — goal clarity, extension completeness, UI-neutrality,
actor-goal uniqueness, post-condition verifiability.

### BAR.UseCaseModeling:5 - Archetypal Grounding

**Show.** Страховая компания, актор «Андеррайтер». Goal-driven use case «Рассчитать
тариф»: goal — тариф за ≤30 сек; pre-condition — заявка укомплектована; post-condition —
тариф рассчитан и сохранён. Актор запросил «экран сравнения тарифов» — аналитик
проверил: цель «сравнить» не заявлена бизнесом и не меняет решение. Use case не
расширен под UI-желание; разработка ненужного экрана предотвращена.

### BAR.UseCaseModeling:6 - Bias-Annotation

**NotWishReason** — «Use case — это просто текстовое описание»: без структуры
Кокбёрна, goal-driven подхода и проверяемых pre/post-conditions.

**Near-Miss (boundary, not this pattern).** Use case «Оформить полис» без UI-деталей;
скоринг возвращает три уровня риска, а не «да/нет» — для среднего требуется ручное
согласование. Это не misuse UseCaseModeling, а дефект `BAR.RequirementElicitation`
(бизнес-правило скоринга не выявлено).

### BAR.UseCaseModeling:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.UCM-1` | Goal statement: «Actor X достигает цели Y» | Goal-driven подход |
| `CC-BAR.UCM-2` | Без UI-деталей; «actor intention → system responsibility» | UI-neutrality |
| `CC-BAR.UCM-3` | Extension conditions для каждого шага main success | Extension completeness |
| `CC-BAR.UCM-4` | Тестировщик пишет test cases по use case без разъяснений | Testability через use case |

### BAR.UseCaseModeling:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Use case как UI flow** | Последовательность экранов без цели актора | Goal statement + actor intention → system responsibility |
| **Счастливый путь без extensions** | Extension «если ошибка — показать сообщение» без failure condition | Extension scenarios; до 40% сценариев не покрыто |

### BAR.UseCaseModeling:9 - Consequences

**ImprovementCheck** — каждый use case имеет primary actor, измеримый post-condition,
extension scenarios, UI-neutrality; альтернативы покрывают ≥90% failure modes.

**ValidationBoundary** — тестировщик пишет test cases для main + extensions без
разъяснений; refresh при изменении процесса или новом акторе.

**FreshnessOrExpiry** — `stale` при изменении процесса, затрагивающего цель актора.
**ReadinessDisposition** — `P2W-ready` для передачи в разработку, тестирование, приёмку.

### BAR.UseCaseModeling:10 - Rationale

Устранить ошибку «use case = UI specification» до того, как она приведёт к
непокрытым сценариям и переделкам.

### BAR.UseCaseModeling:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 10.50 (Use Cases and Scenarios) | Extended | Goal-driven структура + запрет UI-flow | Reopen on BABOK v4 |
| Cockburn, Writing Effective Use Cases (2000) | Adopt | MandatoryConstraints воспроизводят структуру | Reopen on source revision |

### BAR.UseCaseModeling:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.UseCaseModeling:End