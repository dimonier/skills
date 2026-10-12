---
id: BAR.RequirementTraceability
title: Трассировка требований
status: seed
keywords: [traceability, trace-link, coverage, impact-analysis, bidirectional]
dependencies:
  builds_on: [A.10, C.16]
  coordinates_with: [C.2.1, C.32.ADR, E.17, A.6.P, G.11]
---

## BAR.RequirementTraceability - Трассировка требований

> **Trigger:** Невозможно ответить «почему мы это делаем?» для конкретного требования; при изменении нельзя определить затронутые компоненты и тесты.

---

### BAR.RequirementTraceability:1 - Problem frame

Use this pattern to establish and maintain directed traceability links across the
artifact chain (need → requirement → design → implementation → test), enabling forward
and backward navigation and impact analysis.

**ScopeCut** — установление и поддержание traceability links между артефактами;
**не** охватывает автоматизацию трассировки инструментом.

### BAR.RequirementTraceability:2 - Problem

**ProblemSignal** — нельзя ответить «почему мы это делаем?»; при изменении требования
нельзя определить затронутые компоненты и тесты; на приёмке нельзя подтвердить
покрытие всех требований тестами.

**SymptomDetection** — при изменении `REQ-42` команда не может назвать затронутые
тесты и модули; impact analysis занимает дни; на аудите нельзя показать покрытие
нормативных требований.

**ProblemHypothesis** — traceability links не создаются систематически: команда
полагается на «интуицию» и «память»; артефакты не содержат обратных ссылок.

### BAR.RequirementTraceability:3 - Forces

| Force | Settlement |
|---|---|
| «У нас agile, traceability не нужна» vs управляемость при изменениях | Путаница формата носителя и необходимости прослеживаемости |
| Forward trace vs bidirectional | Обязателен и backward trace (test → requirement → need) |
| Живые связи vs audit artifact | Traceability для impact analysis, не Excel-файл для аудита |

### BAR.RequirementTraceability:4 - Solution

**EntityOfConcern** — traceability matrix / trace link: направленная связь,
позволяющая навигацию вперёд (requirement → design → implementation → test) и назад
(test → requirement → need).

**AcceptanceCriterion** — для каждого требования: связанные design elements, code
modules, test cases; для каждого теста: связанное требование; coverage метрика;
для нормативных требований — 100% покрытие тестами подтверждено.

**MandatoryConstraints** — для safety-critical/regulated domain traceability обязательна
до test case на каждое требование; запрещены «плавающие» требования без trace до
источника и «плавающие» тесты без trace до требования.

**CharacterizationRelation** — coverage (доля требований с полной trace), link density,
freshness (доля актуальных связей), impact analysis time.

### BAR.RequirementTraceability:5 - Archetypal Grounding

**Show.** Авионика, сертификационный аудит DO-178C. Требование `REQ-127` имеет
полную цепочку: потребность → `REQ-127` → `D-44` → `FDRWriter.c` → `T-127-1…8`.
Аудитор случайно выбирает `REQ-127` и требует доказательств покрытия за 15 минут —
полная forward/backward цепочка поднята из RM-инструмента. Сертификация пройдена без
замечаний.

### BAR.RequirementTraceability:6 - Bias-Annotation

**NotWishReason** — «У нас agile, документировать traceability не надо»: путаница
между форматом носителя и необходимостью прослеживаемости при изменениях.

**Near-Miss (boundary, not this pattern).** Все связи проставлены, coverage 100%, но
impact analysis показывает 5 затронутых тестов, после изменения падают 2 — links
формальны и семантически некорректны (copy-paste). Это не misuse паттерна, а дефект
качества связей → consistency check.

### BAR.RequirementTraceability:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.TRC-1` | Forward trace до design элемента для каждого требования | Предотвращает «потерянные» требования |
| `CC-BAR.TRC-2` | Forward trace до ≥1 test case | Предотвращает непокрытые требования |
| `CC-BAR.TRC-3` | Backward trace от каждого test case до требования | Предотвращает «плавающие» тесты |
| `CC-BAR.TRC-4` | Regulated domain: 100% требований с полной trace до теста | Предотвращает compliance risk |

### BAR.RequirementTraceability:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Трассировка в Excel для аудита** | Связи не обновляются; impact analysis невозможен | Живые связи для impact analysis, не статический документ |
| **Трассировка только вперёд** | Нет обратных связей — нельзя проверить coverage/root-cause | Bidirectional traceability |

### BAR.RequirementTraceability:9 - Consequences

**ImprovementCheck** — forward trace до design/implementation/test; backward trace от
теста; impact analysis типового изменения за `≤15 минут`.

**ValidationBoundary** — impact analysis случайного изменения находит все затронутые
артефакты; refresh при изменении любого артефакта в цепочке.

**FreshnessOrExpiry** — `stale` при изменении требования без обновления links; `stale`
при изменении design/implementation/test без обратного обновления.
**ReadinessDisposition** — `P2W-ready` для внедрения дисциплины traceability.

### BAR.RequirementTraceability:10 - Rationale

Предотвратить потерю управляемости при росте системы: без traceability изменения
становятся непредсказуемыми по стоимости и риску.

### BAR.RequirementTraceability:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| BABOK v3, ch. 5 (Maintain Requirements) — bidirectional trace | Adopt | AcceptanceCriterion | Reopen on BABOK v4 |
| IREB CPRE FL, ch. 7 — traceability как свойство спецификации | Adopt | Quantified метрики (impact analysis time) | Reopen on CPRE FL update |
| ГОСТ 34.602 / РД 50-34.698 — прослеживаемость до приёмочных испытаний | Adopt | MandatoryConstraints для regulated domain | Reopen on standard revision |

### BAR.RequirementTraceability:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.RequirementTraceability:End