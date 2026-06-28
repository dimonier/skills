# BAR.RequirementTraceability: Трассировка требований

> **Trigger:** Невозможно ответить на вопрос «почему мы это делаем?» для конкретного требования; при изменении требования невозможно определить, какие компоненты и тесты затронуты
> **Governing patterns:** 
>   → `../fpf-core/references/A.10-evidence.md`
>   → `../fpf-core/references/C.16-coverage.md`
>   → `../fpf-core/references/C.2.1-episteme.md`
>   → `../fpf-core/references/C.32.ADR-arch-decision-record.md`
>   → `../fpf-core/references/E.17-multi-view.md`
>   → `../fpf-core/references/A.6.P-relation-precision.md`
>   → `../fpf-core/references/G.11-currentness.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Невозможно ответить на вопрос «почему мы это делаем?» для конкретного требования; при изменении требования невозможно определить, какие компоненты системы и тесты затронуты; на приёмочных испытаниях нельзя подтвердить, что все требования покрыты тестами |
| **ContextGrounding** | Проект с `≥3` видами артефактов в цепочке: потребность → требование → архитектурное решение → код → тест; нормативные требования (ГОСТ 34, DO-178C, ISO 26262) к прослеживаемости |
| **ScopeCut** | Установление и поддержание traceability links между артефактами; не охватывает автоматизацию трассировки инструментом |
| **NotWishReason** | «У нас agile, документировать traceability не надо» — путаница между форматом носителя и необходимостью прослеживаемости при изменениях |

## Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Pohl: traceability — «ability to describe and follow the life of a requirement in both forward and backward direction». ГОСТ 34.602: требование прослеживаемости от ТЗ до приёмочных испытаний. Gotel & Finkelstein (1994) — seminal paper о проблеме traceability в инженерии требований |
| **EntityOfConcern** | Traceability matrix / trace link — направленная связь между артефактами, позволяющая навигацию вперёд (requirement → design → implementation → test) и назад (test → requirement → need) |
| **SymptomDetection** | При изменении требования `REQ-42` команда не может назвать затронутые тесты и модули; impact analysis занимает дни вместо минут; на аудите нельзя показать, что все нормативные требования покрыты тестами |
| **ProblemHypothesis** | Traceability links не создаются систематически — команда полагается на «интуицию» и «память»; артефакты (код, тесты) не содержат обратных ссылок на требования |
| **ImprovementCheck** | Для каждого требования существует forward trace до design, implementation и test; для каждого теста существует backward trace до требования; impact analysis для типового изменения требования выполняется за `≤15 минут` |
| **AcceptanceCriterion** | Traceability matrix содержит: (1) для каждого требования — связанные design elements, code modules, test cases, (2) для каждого теста — связанное требование, (3) coverage метрика: доля требований с полной цепочкой трассировки; для нормативных требований — 100% покрытие тестами подтверждено |
| **MandatoryConstraints** | Для safety-critical/regulated domain — traceability обязательна до test case на каждое требование; запрещены «плавающие» требования без trace до источника и «плавающие» тесты без trace до требования |
| **CharacterizationRelation** | Coverage (доля требований с полной trace), link density (среднее число связей на требование), freshness (доля актуальных связей — не «протухших»), impact analysis time |
| **ValidationBoundary** | Проверка: impact analysis случайного изменения требования — все затронутые артефакты найдены; refresh при изменении любого артефакта в цепочке |
| **FreshnessOrExpiry** | `stale` при изменении требования без обновления traceability links; `stale` при изменении design/implementation/test без обратного обновления |
| **ProblemFormulationFollowUpReason** | Предотвратить потерю управляемости при росте системы — без traceability изменения становятся непредсказуемыми по стоимости и риску |
| **ReadinessDisposition** | `P2W-ready` для внедрения дисциплины traceability в процесс работы с требованиями |
| **SolvabilityBand** | `feasible` при наличии tool support (RM tool); `feasible-but-not-trivial` без tool support |

## Worked Examples

**Positive Worked Slice:** Компания-разработчик авионики готовит сертификационный аудит DO-178C. Требование `REQ-127` (формат записи полётных данных, compliance с регламентом) имеет полную trace-цепочку: потребность стейкхолдера → `REQ-127` → design-спецификация `D-44` → модуль кода `FDRWriter.c` → тесты `T-127-1` по `T-127-8`. Аудитор случайно выбирает `REQ-127` и требует доказательств покрытия за 15 минут. Бизнес-аналитик из RM-инструмента поднимает полную цепочку forward и backward trace, включая записи о sign-off на каждом этапе. Сертификация пройдена без замечаний — traceability matrix спасла проект от потенциальной 6-месячной задержки.

**Near-Miss Example:** Команда использует JIRA с плагином traceability; все связи проставлены, coverage 100%. При изменении `REQ-31` impact analysis показывает 5 затронутых тестов, после изменения 2 падают — trace links проставлены формально, но семантически некорректны (ошибочная связь через copy-paste). Это не misuse паттерна, а проблема качества связей, требующая consistency check.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Трассировка в Excel для аудита** | Traceability matrix — Excel-файл, созданный перед аудитом; связи не обновляются при изменениях, impact analysis невозможен | Подменяет working traceability на audit artifact. Паттерн требует живых связей для impact analysis, а не статического документа |
| **Трассировка только вперёд** | Forward trace есть, обратных связей нет: от теста нельзя подняться к требованию, от требования — к потребности | Нарушает bidirectional traceability: без backward trace невозможна проверка coverage и root-cause analysis |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.TRC-1` | Для каждого требования существует forward trace до design элемента, в котором оно реализовано | Предотвращает «потерянные» требования без связи до реализации |
| `CC-BAR.TRC-2` | Для каждого требования существует forward trace до ≥1 test case | Предотвращает непокрытые тестами требования |
| `CC-BAR.TRC-3` | Для каждого test case существует backward trace до требования | Предотвращает «плавающие» тесты без родительского требования |
| `CC-BAR.TRC-4` | Для safety-critical/regulated domain: 100% требований имеют полную trace-цепочку до теста, проверено аудитом | Предотвращает compliance risk и сертификационные задержки |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 5 (Requirements Life Cycle Management) — Maintain Requirements | Traceability как дисциплина поддержания связей: потребность → требование → design → implementation → test; bidirectional trace | **Adopted** — AcceptanceCriterion требует forward и backward trace links в traceability matrix | **Extended:** BABOK описывает bidirectional trace как good practice; BAPF делает backward trace mandatory через MandatoryConstraints («запрещены "плавающие" тесты без trace до требования»). Anti-pattern «Трассировка только вперёд» называет violation точнее, чем BABOK |
| IREB CPRE FL, ch. 7 (Requirements Documentation) | Трассировка как свойство спецификации требований: forward и backward traceability для управления изменениями | **Adopted** — traceability links как enabler для impact analysis (Section 7: ChangeImpactMatrix) | Добавлены quantified метрики: coverage (доля требований с полной цепочкой), impact analysis time (≤15 мин). IREB определяет traceability как свойство, BAPF задаёт измеряемые цели |
| ГОСТ 34.602-2020 / РД 50-34.698-90 | Требование прослеживаемости от ТЗ до приёмочных испытаний как обязательное свойство документации АС | **Adopted** — MandatoryConstraints: для safety-critical/regulated domain traceability обязательна до test case | Добавлен anti-pattern «Трассировка в Excel для аудита» — формальное соблюдение ГОСТ без working traceability. ГОСТ предписывает, BAPF предупреждает об имитации соблюдения |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Trace link как Evidence Graph | `A.10` |
| Coverage как характеризация качества traceability | `C.16` |
| Requirement как эпистемический артефакт с relations | `C.2.1` |
| Связь требования с design/implementation | `C.32.ADR`, `E.17` |
| Forward/backward trace как направленный relation | `A.6.P` (Relation Precision) |
| Freshness при изменении артефактов цепочки | `G.11` |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L595-L665
