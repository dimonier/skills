# BAR.RequirementChangeManagement: Управление изменениями требований

> **Trigger:** Новые требования добавляются «по звонку» без оценки влияния; scope creep не отслеживается — проект делает в 2x больше, но ключевая функциональность не готова
> **Governing patterns:** 
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/A.21-gate-decision.md`
>   → `../fpf-core/references/A.10-evidence.md`
>   → `../fpf-core/references/C.32.ADR-arch-decision-record.md`
>   → `../fpf-core/references/G.5-selector.md`
>   → `../fpf-core/references/G.11-currentness.md`
>   → `../fpf-core/references/G.9-selector.md`
>   → `../fpf-core/references/C.28-causal-claim.md`
>   → `../fpf-core/references/C.27-temporal.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Новые требования добавляются «по звонку» без оценки влияния на реализованные; scope creep не отслеживается — через полгода проект делает в 2x больше, чем планировалось, но ключевая функциональность не готова; изменение требования не сопровождается change impact analysis |
| **ContextGrounding** | Проект/продукт в активной разработке `> 3` месяцев, с `≥2` активными стейкхолдерами, поставляющими новые и изменяющие существующие требования |
| **ScopeCut** | Управление изменениями отдельного требования или группы связанных требований; не охватывает управление контрактом и бюджетирование |
| **NotWishReason** | «Мы agile — изменения приветствуются» без оценки стоимости изменения (cost-of-change) и без проверки, не ломает ли изменение уже работающую функциональность |

## Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Wiegers: «Scope creep is the leading cause of software project failure». Boehm curve: cost-of-change растёт экспоненциально по фазам жизненного цикла. BABOK v3: Knowledge Area «Requirements Life Cycle Management» |
| **EntityOfConcern** | Change request как problem card особого типа — сигнал о необходимости изменения существующего требования, проходящий через gate decision до принятия в работу |
| **SymptomDetection** | Заказчик просит «небольшое изменение» — через спринт обнаруживается, что затронуты 5 модулей и 20 тестов; baseline требований отсутствует — невозможно сравнить, что изменилось; объём незавершённых изменений растёт быстрее, чем закрываются |
| **ProblemHypothesis** | Отсутствует formal change control process — изменения принимаются ad-hoc, без impact analysis, без traceability update, без пересмотра приоритетов ранее принятых требований |
| **ImprovementCheck** | Каждое изменение требования проходит: (1) change request capture (источник, причина), (2) impact analysis (затронутые требования, архитектура, код, тесты), (3) cost/benefit оценки, (4) gate decision (accept/defer/reject), (5) baseline update и traceability refresh |
| **AcceptanceCriterion** | Для каждого change request зафиксированы: идентификатор, источник, описание изменения, причина изменения, impacted artifacts (требования, design, code, tests), оценка усилий, решение (accepted/deferred/rejected) с rationale, статус реализации; baseline требований обновлён; traceability links актуализированы; стейкхолдер, инициировавший изменение, проинформирован о решении |
| **MandatoryConstraints** | Запрещено вносить изменение в requirement baseline без change request; запрещено принимать change request без impact analysis; запрещено отказывать в change request без rationale (почему rejected или deferred); запрещено обновлять baseline без обновления связанных артефактов (design, test) |
| **CharacterizationRelation** | Change request throughput (входящие/закрытые за период), impact analysis accuracy (попадание оценки vs фактические усилия), baseline stability (частота изменений критичных требований), scope creep rate (прирост scope без изменения ресурсов) |
| **ComparabilityRelation** | Сравнение change requests по `impact × value × urgency` (`G.9`) |
| **ValidationBoundary** | Проверка на `≥3` change requests: impact analysis соответствует фактическим усилиям с точностью `±30%`; refresh при каждом изменении baseline |
| **FreshnessOrExpiry** | `stale` если change request реализован и baseline обновлён; `stale` если change request rejected/deferred и истёк срок актуальности |
| **ProblemFormulationFollowUpReason** | Остановить неконтролируемый scope creep до того, как он сделает проект неуправляемым по срокам и стоимости |
| **ReadinessDisposition** | `P2W-ready` для внедрения change control в процесс работы с требованиями |
| **SolvabilityBand** | `feasible` при наличии baseline требований и traceability; `blocked` без baseline и traceability |
| **UnknownHandling** | `safe-probe-needed` если impact analysis не может быть выполнен с приемлемой точностью — architecture spike или feasibility prototype |

## Worked Examples

**Positive Worked Slice:** Телеком-оператор мигрирует биллинговую систему под регуляторный дедлайн. За 30 дней до запуска директор по маркетингу требует «real-time уведомления о расходах» — оценка: 4 недели дополнительной разработки. Процесс change control срабатывает: change request `CR-77` зафиксирован, impact analysis выявляет 3 затронутых модуля и конфликт с фичей регуляторной отчётности, gate decision: deferred до post-launch релиза с документированным rationale, направленным директору маркетинга и копией регулятору. Миграция биллинга укладывается в регуляторный дедлайн; post-launch релиз доставляет уведомления без срыва compliance.

**Near-Miss Example:** Стейкхолдер просит «экспорт в PDF». Команда оформляет change request, impact analysis (1 модуль, 3 теста), оценка 3 дня. Через спринт: библиотека PDF конфликтует с лицензией продукта — изменение rejected. Change control процесс сработал корректно. Проблема не в change management, а в неполноте стейкхолдеров — юрдепартамент не был идентифицирован как holder constraint.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Изменение по звонку** | Стейкхолдер звонит разработчику: «добавь поле X, срочно». Change request не оформлен, impact не оценён; через месяц никто не помнит, почему поле существует | Нарушает MandatoryConstraint о запрете изменений baseline без change request — uncontrolled mutation требований |
| **Все изменения принимаются** | Change control board автоматически approves все запросы без trade-off с текущим scope; backlog разбухает, ключевая функциональность откладывается | Gate decision без reject/defer — backlog inflation, а не управление. Паттерн требует explicit decision с rationale |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.CHM-1` | Каждое изменение baseline оформлено как change request с идентификатором, источником и описанием изменения | Предотвращает «изменения по звонку» |
| `CC-BAR.CHM-2` | Каждый change request содержит impact analysis (требования, design, код, тесты) — подписан разработчиком | Предотвращает слепые изменения без понимания последствий |
| `CC-BAR.CHM-3` | Каждый change request имеет explicit решение (accepted/deferred/rejected) с documented rationale | Предотвращает «все изменения принимаются» |
| `CC-BAR.CHM-4` | После реализации baseline требований обновлён — зафиксирована новая версия с датой и списком изменений | Предотвращает расхождение baseline и реальности |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 5 (Requirements Life Cycle Management) — Manage Changes | Процесс управления изменениями: capture → impact analysis → gate decision → baseline update; governance stakeholders участвуют в decision | **Adopted** — AcceptanceCriterion воспроизводит полный process flow; change request → impact analysis → gate decision → baseline update | **Extended:** BABOK описывает процесс как activity description; BAPF формулирует MandatoryConstraints как prohibitions (запрещено менять baseline без CR, запрещён CR без impact analysis). BABOK — descriptive, BAPF — prescriptive через запреты |
| BABOK v3, ch. 6 (Strategy Analysis) — Scope Management | Предотвращение scope creep через explicit decision criteria: change request оценивается относительно зафиксированного scope baseline | **Adopted** — SolvabilityBand: feasible при наличии baseline; blocked без baseline | Добавлены CharacterizationRelation метрики: scope creep rate, baseline stability, change request throughput. BABOK концептуально предупреждает о scope creep, BAPF даёт количественные индикаторы. Anti-pattern «Все изменения принимаются» |
| IREB CPRE FL, ch. 9 (Requirements Management) | Управление изменениями: жизненный цикл change request, approval workflow, синхронизация связанных артефактов | **Adopted** — traceability refresh при каждом изменении baseline как часть change control | Добавлен anti-pattern «Изменение по звонку» и explicit gate decision с rationale (accept/defer/reject). IREB описывает workflow, BAPF называет violation mode и даёт detection rule |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Change request как ProblemCard особого типа | `C.22.2` |
| Change control как gate decision | `A.21` |
| Impact analysis как blast radius (affected artifacts) | `A.10`, `C.32.ADR` |
| Baseline как версионированный selected set требований | `G.5`, `G.11` |
| Сравнение change requests по impact/value/urgency | `G.9` |
| Cost-of-change кривая как evidence | `C.28` (causal claim), `C.27` (temporal) |
| Refresh при обновлении baseline | `G.11` |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L667-L740
