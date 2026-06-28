# BAR.RequirementPrioritization: Приоритизация требований

> **Trigger:** Product backlog содержит 200+ требований, все помечены как «критичные»; каждый стейкхолдер продвигает «свои» требования как наивысший приоритет
> **Governing patterns:** 
>   → `../fpf-core/references/C.25-q-bundle.md`
>   → `../fpf-core/references/G.9-selector.md`
>   → `../fpf-core/references/G.0-comparison-frame.md`
>   → `../fpf-core/references/G.4-trade-off.md`
>   → `../fpf-core/references/G.5-selector.md`
>   → `../fpf-core/references/C.16-coverage.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Product backlog содержит 200+ требований, все помечены как «критичные»; команда не может объяснить, почему реализуется именно этот набор, а не другой; стейкхолдеры конфликтуют: каждый продвигает «свои» требования как наивысший приоритет |
| **ContextGrounding** | Проект с ограниченными ресурсами (время, бюджет, люди) и `≥3` конкурирующими за ресурсы стейкхолдерами |
| **ScopeCut** | Приоритизация требований в рамках одного релиза/итерации; не заменяет портфельное управление и стратегическое планирование |
| **NotWishReason** | «Всё важно, давайте сделаем всё» — отказ от приоритизации под видом «у нас гибкая методология» |

## Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Wiegers: «If you don't prioritize requirements, every stakeholder will assume all of his or her requirements are top priority». Техники: MoSCoW, Kano model, cost-of-delay, WSJF, pairwise comparison |
| **EntityOfConcern** | Приоритизированный набор требований (prioritized backlog) — упорядоченное множество требований с явными критериями упорядочивания |
| **SymptomDetection** | Спринт-планирование занимает часы в спорах «что брать»; реализованные требования не используются (low adoption); критический production incident возникает из-за неприоритизированного нефункционального требования |
| **ProblemHypothesis** | Не заданы explicit prioritization criteria — команда и стейкхолдеры не имеют общего языка для сравнения ценности требований; приоритизация сводится к «кто громче кричит» |
| **ImprovementCheck** | Для каждого требования зафиксирована оценка по явным критериям (value, cost, risk, time-criticality, dependency); порядок в backlog обоснован комбинацией критериев, а не интуицией; стейкхолдеры согласны с trade-off (признают, что `REQ-42` важнее `REQ-17`) |
| **AcceptanceCriterion** | Для каждого требования: (1) оценка бизнес-ценности, (2) оценка стоимости/усилий, (3) оценка риска при невыполнении, (4) архитектурная значимость/зависимости от других требований, (5) временная критичность; критерии приоритизации согласованы со стейкхолдерами до начала приоритизации; rejected alternatives по методу приоритизации зафиксированы |
| **MandatoryConstraints** | Запрещено декларировать всё «критичным» или «must-have»; как минимум один explicit prioritization criterion должен быть не «голосованием стейкхолдера» (value, risk, cost, dependency); запрещена приоритизация без участия носителей ресурсных constraints (разработка, эксплуатация) |
| **CharacterizationRelation** | Business value (измеримая vs заявленная), cost-of-delay, risk reduction, architectural significance, stakeholder alignment (согласие с итоговым порядком) |
| **ComparabilityRelation** | Матрица `value × cost × risk × urgency` для сравнения требований (`G.9`); pairwise comparison для близких по value требований |
| **ParityRelation** | `G.9` обязателен, когда `≥2` стейкхолдера конкурируют за приоритет |
| **ValidationBoundary** | Проверка на одном релизе: overlap между приоритизированным списком и фактически реализованным ≥ 80%; refresh при изменении бизнес-стратегии или появлении новых стейкхолдеров |
| **FreshnessOrExpiry** | `stale` после завершения релиза/итерации; `stale` при изменении приоритетов бизнеса |
| **ProblemFormulationFollowUpReason** | Остановить растрату ресурсов на неприоритетные требования до того, как они вытеснят критически важные |
| **ReadinessDisposition** | `P2W-ready` для планирования итерации/релиза |
| **SolvabilityBand** | `feasible` при наличии quantified value/risk/cost оценок; `blocked` при отсутствии согласия о критериях |

## Characterization Measures

| Characteristic | Measurement protocol | Target threshold |
|---|---|---|
| **WSJF calculation coverage** | Для каждого приоритизированного требования проверяется наличие четырёх компонент WSJF: business value (оценка), time criticality (оценка), risk reduction (оценка), job size (человеко-часы разработчика). WSJF = (value + criticality + risk_reduction) / job_size | `≥ 0.80` требований с полным WSJF расчётом |
| **Stakeholder alignment score** | Kendall's τ (rank correlation) между итоговым приоритизированным порядком и индивидуальным ранжированием каждого стейкхолдера; среднее значение τ по всем стейкхолдерам | `τ ≥ 0.60` (среднее) |
| **Priority-realization overlap** | Jaccard similarity между top-N приоритизированных требований и фактически реализованными требованиями за релиз; N = размер спринта/релиза | `≥ 0.80` overlap |

## Worked Examples

**Positive Worked Slice:** E-commerce-платформа готовит релиз к Чёрной пятнице. Бэклог из 85 требований, все стейкхолдеры настаивают: «критично». Бизнес-аналитик применяет WSJF (Weighted Shortest Job First) с явными критериями: бизнес-ценность (рост выручки), срочность (дедлайн Чёрной пятницы), снижение риска (вероятность падения сайта), объём работ (часы разработки). Оценка WSJF вскрывает: «кеширование чекаута» (2 дня, предотвращает 60%-ный риск сбоя) имеет в 8 раз больший WSJF-балл, чем «редизайн вишлиста» (15 дней, маржинальный рост выручки). Релиз доставляет 5 максимальных WSJF-требований в срок; Чёрная пятница проходит с нулевым даунтаймом. Релиз спасён от срыва из-за скрытого перекоса приоритетов в пользу заметных, но малополезных требований.

**Near-Miss Example:** Продакт-менеджер ранжирует backlog по ROI за квартал без учёта архитектурных зависимостей. Команда не может взять требование с высоким ROI — оно зависит от неприоритизированного инфраструктурного требования. Это не misuse приоритизации — критерий выбран, но неполон; проблема в невидимых зависимостях, требующих multi-criteria подхода.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Приоритет голосованием** | Стейкхолдеры голосуют «за» свои требования; побеждает наибольший политический вес, а не бизнес-ценность | Подменяет quantified value/cost/risk сравнение social negotiation — паттерн требует `G.9`-based trade-off, а не majority vote |
| **Приоритизация без разработки** | Аналитик ранжирует по бизнес-ценности без оценки feasibility и стоимости; top-5 требований нереализуемы в срок | Нарушает MandatoryConstraint об участии носителей ресурсных constraints — приоритет без оценки cost порождает wish list |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.PRI-1` | Для каждого требования зафиксирована оценка бизнес-ценности — не «важно», а quantified или ranked по согласованному критерию | Предотвращает «всё важно» и подмену критериев |
| `CC-BAR.PRI-2` | Оценка стоимости/усилий выполнена разработчиком, не аналитиком | Предотвращает «приоритизацию без разработки» |
| `CC-BAR.PRI-3` | Критерии приоритизации согласованы со стейкхолдерами до ранжирования, rejected criteria зафиксированы | Предотвращает «приоритет голосованием» |
| `CC-BAR.PRI-4` | Приоритизация проведена с участием носителей ресурсных constraints (разработка, эксплуатация) | Предотвращает разрыв между приоритетом и реализуемостью |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 5 (Requirements Life Cycle Management) — Prioritization | Приоритизация как процесс оценки ценности, риска, стоимости и urgency; упорядочение требований для итеративного планирования | **Adopted** — AcceptanceCriterion требует multi-factor оценки (value, cost, risk, urgency) для каждого требования | **Extended:** BABOK описывает процесс, BAPF добавляет MandatoryConstraint «запрещено декларировать всё "критичным"» и anti-pattern «Приоритет голосованием». BABOK — descriptive, BAPF — prescriptive через запреты и misuse catalog |
| BABOK v3, ch. 10.33 (Prioritization Techniques) | Классификация техник: MoSCoW, Kano, timeboxing, weighted ranking; WSJF как комбинация value × urgency × cost | **Adopted** — WSJF используется как допустимый метод; AcceptanceCriterion требует оценки по явным критериям | Добавлен MandatoryConstraint: участие носителей ресурсных constraints (разработка, эксплуатация) обязательно. BABOK фокусируется на технике аналитика, BAPF добавляет implementer role как обязательного участника. Anti-pattern «Приоритизация без разработки» |
| IREB CPRE FL, ch. 6 (Requirements Negotiation and Prioritization) | Приоритизация как multi-perspective negotiation; критерии согласуются стейкхолдерами до ранжирования, а не голосуются | **Adopted** — критерии приоритизации согласованы до ранжирования; rejected criteria зафиксированы | Операционализация: ComparabilityRelation (матрица value × cost × risk × urgency) как инструмент сравнения; Conformance Checklist CC-BAR.PRI-3/4. IREB описывает negotiation, BAPF даёт проверяемый conformance gate |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Приоритет требования как Q-bundle (value, cost, risk) | `C.25` |
| Сравнение требований (pair-choice, MoSCoW) | `G.9`, `G.0` |
| Trade-off analysis | `G.4` |
| Ordering как selected set из portfolio | `G.5` |
| Характеризация качества приоритизации | `C.16` |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L442-L521
