---
id: BAR.RequirementPrioritization
title: Приоритизация требований
status: seed
keywords: [prioritization, backlog, trade-off, wsjf, stakeholder-alignment]
dependencies:
  builds_on: [C.25, G.9]
  coordinates_with: [G.0, G.4, G.5, C.16]
---

## BAR.RequirementPrioritization - Приоритизация требований

> **Trigger:** Product backlog содержит 200+ требований, все помечены как «критичные»; каждый стейкхолдер продвигает «свои» требования как наивысший приоритет.

---

### BAR.RequirementPrioritization:1 - Problem frame

Use this pattern when resources are constrained and ≥3 stakeholders compete for them:
order the requirement set by explicit, agreed criteria rather than by assertion or vote.

**ScopeCut** — приоритизация требований в рамках одного релиза/итерации; **не**
заменяет портфельное управление и стратегическое планирование.

### BAR.RequirementPrioritization:2 - Problem

**ProblemSignal** — backlog из 200+ «критичных» требований; команда не может
объяснить, почему реализуется именно этот набор; стейкхолдеры конфликтуют, каждый
продвигая «свои» требования.

**SymptomDetection** — спринт-планирование занимает часы споров «что брать»;
реализованное не используется (low adoption); production incident из-за
неприоритизированного НФТ.

**ProblemHypothesis** — не заданы explicit prioritization criteria; приоритизация
сводится к «кто громче кричит».

### BAR.RequirementPrioritization:3 - Forces

| Force | Settlement |
|---|---|
| «Всё важно, сделаем всё» vs ограниченность ресурсов | Отказ от приоритизации — не «гибкость», а растрата ресурсов |
| Политический вес vs бизнес-ценность | Приоритет ≠ голосование; явные value/cost/risk критерии |
| Аналитик ранжирует vs реализуемость | Приоритизация с участием носителей ресурсных constraints |

### BAR.RequirementPrioritization:4 - Solution

**EntityOfConcern** — приоритизированный набор требований (prioritized backlog):
упорядоченное множество с явными критериями упорядочивания.

**AcceptanceCriterion** — для каждого требования: (1) бизнес-ценность, (2)
стоимость/усилия, (3) риск при невыполнении, (4) архитектурная значимость/
зависимости, (5) временная критичность; критерии согласованы со стейкхолдерами
**до** приоритизации; rejected alternatives по методу зафиксированы.

**MandatoryConstraints** — запрещено декларировать всё «критичным»/«must-have»; ≥1
критерий не «голосование стейкхолдера»; запрещена приоритизация без носителей
ресурсных constraints (разработка, эксплуатация).

**CharacterizationRelation** — business value, cost-of-delay, risk reduction,
architectural significance, stakeholder alignment (согласие с итоговым порядком).

### BAR.RequirementPrioritization:5 - Archetypal Grounding

**Show.** E-commerce перед Чёрной пятницей: backlog из 85 «критичных» требований.
WSJF с явными критериями (ценность, срочность, снижение риска, объём работ) вскрыл:
«кеширование чекаута» (2 дня, предотвращает 60%-ный риск сбоя) имеет в 8 раз
больший WSJF, чем «редизайн вишлиста» (15 дней). Релиз доставил топ-5 по WSJF;
Чёрная пятница прошла с нулевым даунтаймом.

### BAR.RequirementPrioritization:6 - Bias-Annotation

**NotWishReason** — «Всё важно, давайте сделаем всё»: отказ от приоритизации под
видом «у нас гибкая методология».

**Near-Miss (boundary, not this pattern).** Ранжирование по ROI без учёта
архитектурных зависимостей: топ-требование зависит от неприоритизированного
инфраструктурного. Это не misuse приоритизации, а неполнота критериев →
multi-criteria подход.

### BAR.RequirementPrioritization:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.PRI-1` | Бизнес-ценность quantified или ranked по согласованному критерию | Предотвращает «всё важно» |
| `CC-BAR.PRI-2` | Стоимость/усилия оценены разработчиком, не аналитиком | Предотвращает «приоритизацию без разработки» |
| `CC-BAR.PRI-3` | Критерии согласованы до ранжирования; rejected criteria зафиксированы | Предотвращает «приоритет голосованием» |
| `CC-BAR.PRI-4` | Приоритизация с участием носителей ресурсных constraints | Предотвращает разрыв приоритета и реализуемости |

### BAR.RequirementPrioritization:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Приоритет голосованием** | Побеждает политический вес, а не ценность | `G.9`-based trade-off, а не majority vote |
| **Приоритизация без разработки** | Top-5 нереализуемы без оценки feasibility/cost | Участие носителей ресурсных constraints |

### BAR.RequirementPrioritization:9 - Consequences

**ImprovementCheck** — для каждого требования зафиксирована оценка по явным
критериям; порядок обоснован комбинацией критериев; стейкхолдеры признают trade-off.

**ValidationBoundary** — overlap между приоритетом и фактически реализованным ≥ 80%;
refresh при изменении бизнес-стратегии.

**FreshnessOrExpiry** — `stale` после завершения релиза/итерации или при изменении
приоритетов бизнеса. **ReadinessDisposition** — `P2W-ready` для планирования
итерации/релиза.

### BAR.RequirementPrioritization:10 - Rationale

Остановить растрату ресурсов на неприоритетные требования до того, как они вытеснят
критически важные.

### BAR.RequirementPrioritization:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 5 (Prioritization) — оценка value/cost/risk/urgency | Adopt | AcceptanceCriterion требует multi-factor оценку | Reopen on BABOK v4 |
| BABOK v3, ch. 10.33 (Techniques) — MoSCoW, Kano, WSJF | Adopt | WSJF как допустимый метод | Reopen on BABOK v4 |
| IREB CPRE FL, ch. 6 (Negotiation) — критерии согласуются, не голосуются | Adopt | Критерии согласованы до ранжирования | Reopen on CPRE FL update |

### BAR.RequirementPrioritization:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.RequirementPrioritization:End