---
id: BAR.RequirementSpecification
title: Спецификация требований
status: seed
keywords: [specification, quality, atomicity, verifiability, acceptance-criteria]
dependencies:
  builds_on: [A.19, C.22.2]
  coordinates_with: [A.19.ECS, C.16, C.25, A.10, C.2.1, E.17, G.9]
---

## BAR.RequirementSpecification - Спецификация требований

> **Trigger:** Требования записаны в свободной форме — разработчик и тестировщик интерпретируют их по-разному; требование нельзя проверить (нет измеримого acceptance criteria).

---

### BAR.RequirementSpecification:1 - Problem frame

Use this pattern in the specification phase: turn raw elicitation material into
documented requirements that survive hand-off to development and testing without
re-interpretation.

**ScopeCut** — спецификация отдельного требования или набора требований в рамках
одного bounded context; **не** охватывает архитектурную спецификацию системы.

### BAR.RequirementSpecification:2 - Problem

**ProblemSignal** — требования записаны в свободной форме; разработчик и тестировщик
интерпретируют их по-разному; требование нельзя проверить (нет измеримого
acceptance criteria); противоречия не обнаружены до кодирования.

**SymptomDetection** — «я сделал то, что написано» vs «это не проходит приёмку»;
требование содержит «быстро», «удобно», «надёжно» без квантификации; описывает
«как» (экранная форма), а не «что» (функция системы).

**ProblemHypothesis** — требования не проходят проверку на characteristics of a good
requirement (unambiguous, verifiable, atomic): спецификация — пересказ слов
стейкхолдера, а не инженерный артефакт.

### BAR.RequirementSpecification:3 - Forces

| Force | Settlement |
|---|---|
| Полнота (SRS на 300 страниц) vs пригодность использования | Спецификация под того, кто её читает (разработчик/тестировщик), не ради ГОСТа |
| Естественный язык vs однозначность | Запрет неоднозначных терминов без quantified measure |
| Одно требование vs набор функций | Атомарность: одно требование — одна функция/ограничение |

### BAR.RequirementSpecification:4 - Solution

**EntityOfConcern** — требование как эпистемический артефакт со структурой:
идентификатор, описание, acceptance criteria, приоритет, источник, зависимости.

**AcceptanceCriterion** — требование содержит: (1) уникальный идентификатор,
(2) описание функции/ограничения, (3) actor/role, (4) измеримый acceptance criteria,
(5) приоритет, (6) источник; НФТ содержит quantified scenario: stimulus → response →
measure.

**MandatoryConstraints** — запрещены неоднозначные термины («быстро», «удобно»,
«достаточно», «при необходимости») без quantified measure; запрещено одно
требование, описывающее несколько независимых функций; запрещено отсутствие
acceptance criteria.

**CharacterizationRelation** — unambiguity, atomicity, verifiability, completeness
(в рамках scope cut), consistency, necessity (traceability до потребности).

### BAR.RequirementSpecification:5 - Archetypal Grounding

**Show.** В govtech-проекте для каждого из 120 требований зафиксирован quantified
acceptance criteria «stimulus → response → measure». Требование «реестр должен
масштабироваться» → «при 500 одновременных запросах время ответа ≤ 3 сек для 95%
запросов». На приёмке подрядчик заявил «работает хорошо», но нагрузочное
тестирование показало 15 сек при 200 пользователях — измеримые criteria разрешили
спор объективно.

### BAR.RequirementSpecification:6 - Bias-Annotation

**NotWishReason** — «Напишем SRS на 300 страниц, как в ГОСТе» — без учёта, кто и как
будет использовать спецификацию.

**Near-Miss (boundary, not this pattern).** Требование «отчёт в PDF с группировкой»
однозначно и атомарно, но стейкхолдеру нужен был Excel — он не знал, что PDF не
позволит обработку. Это не дефект спецификации, а ошибка validation →
`BAR.RequirementValidation`.

### BAR.RequirementSpecification:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.RSP-1` | Каждое требование содержит: идентификатор, описание, actor/role | AcceptanceCriterion пп. (1)-(3) |
| `CC-BAR.RSP-2` | Acceptance criteria измеримы; НФТ содержит quantified scenario | AcceptanceCriterion п. (4) |
| `CC-BAR.RSP-3` | Нет неоднозначных терминов без quantified measure | MandatoryConstraints |
| `CC-BAR.RSP-4` | Одно требование — одна функция/ограничение (атомарность) | MandatoryConstraints: запрет неатомарных |

### BAR.RequirementSpecification:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Natural-language literature** | Эссе: «удобный интерфейс, быстро и эффективно, гибкая настройка» — без measure | MandatoryConstraints запрещают «удобно/быстро/гибко» без quantified measure |
| **Atomicity violation** | Одно требование: «регистрировать, уведомлять и отчитываться» — 3 функции | Нарушение атомарности блокирует приоритизацию и тестирование |

### BAR.RequirementSpecification:9 - Consequences

**ImprovementCheck** — каждое требование проходит проверку на однозначность,
атомарность, измеримость, необходимость.

**ValidationBoundary** — тестировщик по acceptance criteria пишет test case без
разъяснений; refresh при изменении требований стейкхолдера.

**FreshnessOrExpiry** — `stale` если не проходит повторную проверку на качество при
изменении контекста. **ReadinessDisposition** — `P2W-ready` для передачи в
разработку и тестирование.

### BAR.RequirementSpecification:10 - Rationale

Предотвратить дефекты требований — самый дорогой класс дефектов: исправление на
этапе эксплуатации в ~100× дороже, чем на этапе требований.

### BAR.RequirementSpecification:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| Wiegers & Beatty, ch. 11 / ISO 29148, ch. 6 — характеристики качества | Adopt | MandatoryConstraints + CharacterizationRelation | Reopen on 4th Ed. / ISO revision |
| IREB CPRE FL, ch. 5 (Documentation) — структура документа | Adopt | AcceptanceCriterion воспроизводит структуру | Reopen on CPRE FL update |
| BABOK v3, ch. 7 (Analysis) — quality criteria | Adopt | ImprovementCheck + ValidationBoundary | Reopen on BABOK v4 |

### BAR.RequirementSpecification:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.RequirementSpecification:End