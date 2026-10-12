---
id: BAR.RequirementElicitation
title: Выявление требований
status: seed
keywords: [elicitation, technique, source, tacit-knowledge, cross-validation]
dependencies:
  builds_on: [A.3.4, A.10]
  coordinates_with: [A.2.1, A.15, A.3.2, B.3]
---

## BAR.RequirementElicitation - Выявление требований

> **Trigger:** Стейкхолдеры не могут сформулировать, что им нужно; скрытые (tacit) требования не выявляются, потому что стейкхолдер считает их «очевидными».

---

### BAR.RequirementElicitation:1 - Problem frame

Use this pattern during the elicitation phase — the primary collection of material
from stakeholders, documents, legacy systems and other sources — to choose techniques
per source and requirement class, and to surface tacit knowledge before specification.

**ScopeCut** — выявление требований через подбор и применение техник elicitation;
**не** охватывает последующую спецификацию и валидацию.

### BAR.RequirementElicitation:2 - Problem

**ProblemSignal** — стейкхолдеры не могут сформулировать, что им нужно, или
формулируют противоречиво; интервью даёт «всё должно работать хорошо»; скрытые
(tacit) требования не выявляются, потому что стейкхолдер считает их «очевидными».

**SymptomDetection** — «вы меня не поняли» после получения спецификации; требования
из разных источников противоречат друг другу; «очевидные» требования (время отклика
≤ 2 сек) не задокументированы.

**ProblemHypothesis** — не подобран адекватный набор техник под тип источника и тип
требований; tacit knowledge не выявлено, потому что интервьюер не спросил о «само
собой разумеющемся».

### BAR.RequirementElicitation:3 - Forces

| Force | Settlement |
|---|---|
| Интервью достаточно vs НФТ не выявляются интервью | Не полагаться на единственную технику; НФТ — через observation/document analysis |
| Доверие стейкхолдеру vs риск требования | Кросс-валидация с независимым источником при высоком риске |
| Tacit knowledge невидимо vs невыявленное ломает приёмку | Выявлять tacit через observation/prototyping/T-shirt sizing |

### BAR.RequirementElicitation:4 - Solution

**EntityOfConcern** — процесс elicitation как трансформация: сырой сигнал от
источника → структурированный материал требований.

**AcceptanceCriterion** — для каждого требования зафиксированы: источник, техника
elicitation, дата, контекст получения; для каждого класса требований применена ≥1
релевантная техника; tacit требования выявлены через observation/prototyping/T-shirt
sizing.

**MandatoryConstraints** — запрещено полагаться на единственную технику (только
интервью); запрещено принимать утверждение стейкхолдера без кросс-валидации с
другим источником при высоком риске требования.

**CharacterizationRelation** — source diversity (независимые источники), technique
adequacy (соответствие техники типу требования), contradiction discovery rate
(противоречия до спецификации vs после приёмки).

### BAR.RequirementElicitation:5 - Archetypal Grounding

**Show.** В проекте автоматизации больничного отделения комбинация structured
interview (дневная смена) + observation (ночная смена) вскрыла, что ночная смена
ведёт параллельный бумажный журнал, обходя систему («требуется 5-минутный
перезапуск при пересменке»). Tacit knowledge зафиксировано как требование: время
перезапуска ≤ 30 сек. Это предотвратило отторжение системы ночной сменой.

### BAR.RequirementElicitation:6 - Bias-Annotation

**NotWishReason** — «Проведём интервью и запишем, что скажут»: без структуры
интервью, кросс-валидации источников и выявления невысказанных требований.

**Near-Miss (boundary, not this pattern).** Техники подобраны (интервью, document
analysis, prototyping), но «оператор ночной смены» не идентифицирован как
стейкхолдер → это не elicitation, а `BAR.StakeholderIdentification`.

### BAR.RequirementElicitation:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.REQ-1` | Для каждого требования зафиксированы: источник, техника, дата, контекст | Прослеживаемость до источника |
| `CC-BAR.REQ-2` | Применено ≥2 техники; ни один класс не опирается только на интервью | Запрет единственной техники |
| `CC-BAR.REQ-3` | Высокорисковые требования (capacity, security, regulatory) кросс-валидированы | Кросс-валидация |
| `CC-BAR.REQ-4` | Tacit требования выявлены через observation/prototyping; результат зафиксирован | Tacit knowledge |

### BAR.RequirementElicitation:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Interview monoculture** | Интервью для всех классов; НФТ записаны со слов без измерения | НФТ не выявляются интервью — observation + document analysis |
| **Tacit knowledge extraction theatre** | «Наблюдение — 2 часа», зафиксировано «оператор выполняет X», но не ПОЧЕМУ Y до Z вопреки инструкции | Формальное наблюдение без probing — misuse |

### BAR.RequirementElicitation:9 - Consequences

**ImprovementCheck** — для каждого класса требований определён источник и техника;
противоречия между источниками выявлены до спецификации.

**ValidationBoundary** — другой аналитик по тем же источникам восстанавливает
сопоставимый набор требований; refresh при смене ключевого стейкхолдера или новом
источнике.

**FreshnessOrExpiry** — `stale` при изменении источника (уход стейкхолдера,
обновление регулирующего документа). **ReadinessDisposition** — `P2W-ready` для
перехода к спецификации.

### BAR.RequirementElicitation:10 - Rationale

Встроить систематический elicitation до спецификации — предотвратить «мы не
спросили» как причину дорогих изменений.

### BAR.RequirementElicitation:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 4 (Elicitation) — 50+ техник, matching to source | Adopt | MandatoryConstraints: техники под тип источника | Reopen on BABOK v4 |
| IREB CPRE FL, ch. 4 — классификация техник по типам источников | Adopt | ImprovementCheck: источник и техника на класс | Reopen on CPRE FL update |
| BABOK v3, ch. 10.32 (Observation) — tacit knowledge | Adopt | AcceptanceCriterion требует observation/prototyping | Reopen on BABOK v4 |

### BAR.RequirementElicitation:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.RequirementElicitation:End