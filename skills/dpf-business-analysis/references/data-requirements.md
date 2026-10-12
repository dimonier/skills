---
id: BAR.DataRequirements
title: Выявление и спецификация требований к данным
status: seed
keywords: [data-requirements, data-quality, privacy, retention, legacy-migration]
dependencies:
  builds_on: [C.25, A.7]
  coordinates_with: [C.16, C.27, A.2, A.2.1, A.10]
---

## BAR.DataRequirements - Выявление и спецификация требований к данным

> **Trigger:** Требования к данным — «перечень атрибутов без бизнес-правил валидации, жизненного цикла, privacy/retention»; модель данных создаётся разработчиком без участия аналитика.

---

### BAR.DataRequirements:1 - Problem frame

Use this pattern where data is a central asset (учётная система, CRM, ERP, реестр,
витрина): treat data requirements as a first-class class of requirements, not a
flat list of fields.

**ScopeCut** — выявление, анализ и спецификация требований к данным как подмножества
требований к системе; **не** охватывает проектирование БД, администрирование,
ETL-разработку.

### BAR.DataRequirements:2 - Problem

**ProblemSignal** — «система должна хранить: ФИО, дата рождения, телефон» — перечень
атрибутов без правил валидации, жизненного цикла, privacy/retention; модель данных
создаётся разработчиком без аналитика; миграция legacy не учтена.

**SymptomDetection** — схема без unique constraint → дубликаты; «хранить историю» без
указания сущностей и срока; legacy-данные не соответствуют новым constraints;
персональные данные без срока давности.

**ProblemHypothesis** — требования к данным не рассматриваются как самостоятельный
класс: аналитик ограничивается «экранными формами», оставляя данные разработчику.

### BAR.DataRequirements:3 - Forces

| Force | Settlement |
|---|---|
| «Данные — забота разработчика» vs разрыв бизнеса и данных | Требования к данным — часть спецификации |
| Перечень полей vs полнота 5 аспектов | Атрибуты + правила + жизненный цикл + качество + privacy |
| Модель по «здравому смыслу» vs business rules | Модель данных с участием аналитика |

### BAR.DataRequirements:4 - Solution

**EntityOfConcern** — требование к данным: описание структуры, constraints, качества,
жизненного цикла (CRUD + archive + delete), privacy/retention, миграции.

**AcceptanceCriterion** — (1) для каждой сущности: атрибуты (имя, тип, обязательность,
уникальность), правила валидации, владелец; (2) для каждого правила — источник;
(3) для персональных данных: категория, срок хранения, условие удаления; (4) модель
верифицирована аналитиком; (5) target по ISO 25012 для CDE; (6) профилирование legacy
с documented issues и планом очистки.

**MandatoryConstraints** — запрещено ограничивать требования перечнем полей; запрещено
проектировать модель без аналитика; запрещено хранить персональные данные без срока
и условия удаления; запрещена миграция без профилирования.

**CharacterizationRelation** — data requirement completeness (5 аспектов), validation
rule coverage, data quality target measurability, legacy data readiness.

### BAR.DataRequirements:5 - Archetypal Grounding

**Show.** Медицинская ИС, сущность «Пациент»: атрибуты с constraints, правила
валидации (СНИЛС — regex + контрольная сумма), классификация персональных данных по
152-ФЗ. Срок хранения медкарты — 25 лет (приказ Минздрава), согласие — 5 лет после
отзыва. Retention policy позволила настроить автоудаление и предъявить на аудите
Роскомнадзора documented policy — штраф предотвращён.

### BAR.DataRequirements:6 - Bias-Annotation

**NotWishReason** — «Данные — забота разработчика, аналитик описывает только экраны»:
разрыв между бизнес-требованиями и моделью данных.

**Near-Miss (boundary, not this pattern).** Data requirements с retention = 3 года, но
персональные данные внутри «Заявки» не удалялись у 15% записей — retention задан на
уровне сущности, а не атрибута. Это не misuse DataRequirements, а дефект
классификации → уточнение по `BAR.RequirementSpecification` (atomicity).

### BAR.DataRequirements:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.DRQ-1` | Атрибуты (тип, обязательность, уникальность), правила, владелец | Структура сущности |
| `CC-BAR.DRQ-2` | Для ПДн: категория, срок, условие удаления; источник указан | Privacy/retention |
| `CC-BAR.DRQ-3` | Legacy профилировано: documented issues, план очистки | Миграция без сюрпризов |
| `CC-BAR.DRQ-4` | Разработчик создаёт схему, тестировщик пишет тесты по targets | Реализуемость и тестируемость |

### BAR.DataRequirements:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Data requirements = перечень полей** | Плоский список без types/constraints/жизненного цикла/privacy | ≤20% требований покрыто; нужны 5 аспектов |
| **Модель данных без аналитика** | Разработчик не знает business rules и regulatory | До 40% валидаций не реализованы |

### BAR.DataRequirements:9 - Consequences

**ImprovementCheck** — каждая сущность имеет атрибуты, правила, жизненный цикл,
качество, privacy; legacy проанализировано.

**ValidationBoundary** — разработчик по data requirements создаёт схему; тестировщик
по targets пишет тесты; refresh при изменении законодательства.

**FreshnessOrExpiry** — `stale` при изменении законодательства, смене data owner,
миграции без профилирования. **ReadinessDisposition** — `P2W-ready` для проектирования
БД и ETL.

### BAR.DataRequirements:10 - Rationale

Предотвратить дефекты данных — самый долгоживущий класс дефектов: некачественные
данные мигрируют из системы в систему.

### BAR.DataRequirements:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 10.16 (Data Modeling) | Extended | Privacy/retention + legacy profiling + sign-off аналитика | Reopen on BABOK v4 |
| DAMA-DMBOK2, ch. 3 / ISO 25012 | Adopt | Data owner/classification + 15 dimensions | Reopen on source revision |

### BAR.DataRequirements:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.DataRequirements:End