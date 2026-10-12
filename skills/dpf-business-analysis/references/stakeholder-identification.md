---
id: BAR.StakeholderIdentification
title: Идентификация стейкхолдеров и их concerns
status: seed
keywords: [stakeholder, concern, identification, onion-model, constraint-holder]
dependencies:
  builds_on: [C.22.2, C.11]
  coordinates_with: [A.2, A.2.1, C.16, G.9]
---

## BAR.StakeholderIdentification - Идентификация стейкхолдеров и их concerns

> **Trigger:** Требования собираются только от одного-двух «громких» стейкхолдеров; упущенные выходят на приёмке с «это не то».

---

### BAR.StakeholderIdentification:1 - Problem frame

Use this pattern at the start of any requirements effort, before elicitation:
identify and classify every stakeholder and their concern(s), so that elicitation
draws on the complete set of interest groups rather than the convenient few.

**ContextGrounding** — проект создания/модификации системы с `≥3` группами
интересов: бизнес-пользователи, эксплуатация, безопасность, регулятор, интеграция
со смежными системами.

**ScopeCut** — идентификация и классификация стейкхолдеров на старте работы с
требованиями; **не** охватывает управление ожиданиями на всём жизненном цикле.

### BAR.StakeholderIdentification:2 - Problem

**ProblemSignal** — требования собираются только от одного-двух «громких»
стейкхолдеров; упущенные стейкхолдеры выходят на этапе приёмки с «это не то, что
нам нужно»; носители ключевых constraints (безопасник, эксплуатация, регулятор)
не опрошены.

**SymptomDetection** — новое требование появляется поздно (late requirement);
приёмка блокируется неожиданным стейкхолдером; требование «X критично» оспорено
другим стейкхолдером с «X не нужно, нужно Y».

**ProblemHypothesis** — не проведён систематический stakeholder identification:
команда работает с «удобными» стейкхолдерами, пропуская holders constraints,
регулирующих и негативных стейкхолдеров.

### BAR.StakeholderIdentification:3 - Forces

| Force | Settlement |
|---|---|
| Позитивные стейкхолдеры достаточны vs держатели constraints обязательны | Выявлять и constraint-holders (безопасность, эксплуатация, регулятор), и негативных стейкхолдеров |
| Скорее начать elicitation vs полнота покрытия | Идентификация строго **до** elicitation, с coverage-проверкой по функциональным областям |
| «Мы и так всех знаем» vs необнаружимый пропуск | Stakeholder map необязателен только пока не случился late requirement — после этого пропуск неотличим от отсутствия карты |

### BAR.StakeholderIdentification:4 - Solution

**EntityOfConcern** — стейкхолдер (stakeholder): лицо / роль / организация / внешняя
система, имеющая concern (интерес, требование, ограничение, риск) в отношении
целевой системы.

Build a stakeholder register / onion model where each entry records: идентификатор,
роль в проекте, concern(ы), канал коммуникации, полномочия по приёмке.

**AcceptanceCriterion** — register/onion model содержит: идентификатор стейкхолдера,
роль (владелец требований, владелец constraints, консультант, информируемый),
concern(ы), канал коммуникации, полномочия по приёмке.

**MandatoryConstraints** — нельзя ограничиваться «позитивными» стейкхолдерами:
holders constraints (безопасность, эксплуатация, регулятор) обязательны к
выявлению; негативные стейкхолдеры (конкуренты, регулятор-запретитель) должны
быть идентифицированы даже при ограниченном доступе.

**CharacterizationRelation** — полнота покрытия (доля типов стейкхолдеров, для
которых есть представитель), своевременность идентификации (elapsed time от старта
до идентификации), разнообразие concerns (не сведены ли все к «удобству
использования»).

### BAR.StakeholderIdentification:5 - Archetypal Grounding

**Show.** В проекте внедрения ERP бизнес-аналитик на старте построил stakeholder
onion model (4 слоя: core team, direct users, constraint holders, external).
Идентифицировал инженера эксплуатации ЦОД (constraint holder) и офицера ИБ — роли,
которые заказчик не назвал при первых интервью. При попытке добавить серверный
компонент эксплуатация указала: «физического места в стойке нет, расширение — через
6 месяцев». Ранняя идентификация предотвратила блокировку приёмки:
перепроектирование заняло 1 день вместо 2 недель.

### BAR.StakeholderIdentification:6 - Bias-Annotation

**NotWishReason** — «Мы и так знаем всех заинтересованных»: без явного stakeholder
map / onion model пропуск holders constraints необнаружим.

**Near-Miss (boundary, not this pattern).** Stakeholder map построен, concerns
зафиксированы — но через месяц эксплуатация блокирует приёмку: constraint «10 000
пользователей» зафиксирован со слов бизнес-заказчика, а носитель constraint
(инженер эксплуатации) не был идентифицирован. Это проблема разделения concern
ownership, а не идентификации → применяется `BAR.RequirementValidation`.

### BAR.StakeholderIdentification:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.SIH-1` | Register содержит: идентификатор, роль, concern(ы), канал, полномочия по приёмке | Операционализирует AcceptanceCriterion |
| `CC-BAR.SIH-2` | Каждая функциональная область имеет ≥1 носителя требования и ≥1 носителя constraint | Coverage функциональных областей |
| `CC-BAR.SIH-3` | Holders constraints (безопасность, эксплуатация, регулятор) явно идентифицированы | Запрет ограничения позитивными стейкхолдерами |
| `CC-BAR.SIH-4` | Негативные стейкхолдеры идентифицированы; при ограниченном доступе зафиксирована причина | MandatoryConstraints: негативные обязательны |

### BAR.StakeholderIdentification:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Stakeholder proxy substitution** | PO опрашивается как «представитель всех»; требования эксплуатации/безопасности записываются со слов PO, который не role-holder для constraint-bearing ролей | Прямая идентификация holder каждого concern |
| **Positive-stakeholder bias** | Register содержит только «дружественных» стейкхолдеров; holders constraints пропущены «они всё равно скажут нет» | MandatoryConstraints прямо запрещают ограничиваться позитивными стейкхолдерами |

### BAR.StakeholderIdentification:9 - Consequences

**ImprovementCheck** — каждая функциональная область имеет идентифицированных
стейкхолдеров; для каждого зафиксирован concern и канал; время до обнаружения
пропущенного стейкхолдера сокращается.

**ValidationBoundary** — проверка stakeholder map независимым reviewer; refresh при
появлении нового функционального домена или внешней системы.

**FreshnessOrExpiry** — `stale` при изменении оргструктуры заказчика, регуляторного
поля или состава смежных систем. **ReadinessDisposition** — `P2W-ready` для перехода
к elicitation от идентифицированных стейкхолдеров.

### BAR.StakeholderIdentification:10 - Rationale

Устранить root cause late requirements до того, как ошибка станет стоить
перепроектирования: невыявленный holder constraint на этапе приёмки — один из
самых дорогих классов late requirement.

### BAR.StakeholderIdentification:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 2 (Key Concepts) — классификация стейкхолдеров по влиянию, RACI | Adopt | Ролевая классификация в AcceptanceCriterion | Reopen on BABOK v4 |
| BABOK v3, ch. 3 (BA Planning) — идентификация до elicitation | Adopt as-is | ScopeCut: идентификация строго до elicitation | Reopen on BABOK v4 |
| IREB CPRE FL, ch. 2 (Context Boundary) — holders constraints обязательны | Adopt | MandatoryConstraints + conformance checklist | Reopen on CPRE FL update |

### BAR.StakeholderIdentification:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.StakeholderIdentification:End