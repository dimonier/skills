# Domain Principle Framework: Бизнес-анализ и работа с требованиями

> **Pattern family:** `E.4.DPF` (Domain Principle Framework Authoring)
> **Status:** Draft — Fourth pass (comparator-by-value discharge, F.18 name card, E.19 admission review, SoTA-binding for 6.9–6.11); 12 карт, все с Mature Comparator Parity и worked examples
> **Normativity:** Локально-нормативный для практики бизнес-анализа в инженерных проектах
> **Depends on:** `FPFCorePatternSet@current`

---

## 1. Context Declaration

| Поле | Значение |
|---|---|
| **BoundedContext** | `БизнесАнализ@ИнженерныеПроекты` |
| **IntendedReader** | Бизнес-аналитик, системный аналитик, product owner, product manager, технический лид, менеджер проекта |
| **FirstUse** | Формулирование задачи на выявление и анализ требований до начала их реализации; отделение проблемы от решения |

### Non‑Use Boundary

- Не заменяет BABOK (IIBA), SWEBOK, IREB, ГОСТ 34 — использует их как источники (`G.2`)
- Не охватывает управление проектом (PMBOK, PRINCE2), бюджетирование, управление персоналом, юридическую экспертизу
- Не является шаблоном документа или нотацией моделирования (UML, BPMN) — нотации используются в представлениях, но не в ядре фреймворка
- Не является заменой FPF Core — использует его как governing-pattern host

---

## 2. Source Pack (`G.2`)

### Adopted Sources

| Источник | Роль в фреймворке |
|---|---|
| **BABOK Guide v3** (IIBA, 2015) | Канонический корпус практик бизнес-анализа: Knowledge Areas, техники, компетенции |
| **IREB CPRE Foundation Level** (IREB, 2023) | Канонический корпус практик requirements engineering |
| **SWEBOK v4** (IEEE, 2024) — глава Software Requirements | Референс практик инженерии требований |
| **Wiegers & Beatty** *Software Requirements*, 3rd Ed. (Microsoft Press, 2013) | Проблемная сторона: симптомы плохих требований, типовые ошибки, anti-patterns |
| **Robertson & Robertson** *Mastering the Requirements Process*, 4th Ed. (2019) | Процесс работы с требованиями: elicitation → analysis → specification → validation |
| **Pohl** *Requirements Engineering* (Springer, 2010) | Систематизация практик: validation vs verification, traceability, change management |
| **Cohn** *User Stories Applied* (2004) | Практика user stories как минимально-достаточной формы требования |
| **Alexander & Beus-Dukic** *Discovering Requirements* (Wiley, 2009) | Эвристики discovery и design: stakeholder analysis, viewpoint-based RE |
| **Mead et al.** *Security Requirements Engineering* (CMU/SEI, техотчёт) | Специфика работы с нефункциональными требованиями безопасности |
| **ГОСТ 34.602-2020** / **РД 50-34.698-90** | Отечественная практика Технического задания на АС |
| **ISO 15288:2023** *Systems and software engineering — System life cycle processes* | Референс процессов жизненного цикла системы; stakeholder requirements definition process, requirements analysis process |
| **ISO/IEC/IEEE 29148:2018** *Systems and software engineering — Requirements engineering* | Канонический международный стандарт инженерии требований: characteristics of good requirements, requirements specification structure |
| **FPF Core Specification** (Levenchuk, June 2026) | Host framework: все governing-pattern cues ссылаются на FPF Core |

### Rejected Sources

- Литература по Agile/Scrum как замена инженерии требований — Agile описывает процесс, а не проблемную сторону требований
- Литература по BPMN/UML/ArchiMate как самоцель — нотации являются carrier представлений, а не ядром работы с требованиями

> **ClaimStatus:** `provisional` — required payload extraction per `G.2` discipline before pattern body freeze.

### SoTA-Echoing Record

| Source | SoTA-bearing claim | Pattern signal grounded | Adoption stance | Currentness window |
|---|---|---|---|---|
| **BABOK v3, ch. 3** (Business Analysis Planning and Monitoring) | Stakeholder identification — первая задача бизнес-анализа до всякого elicitation | `BAR.StakeholderIdentification`: «требования собираются только от громких стейкхолдеров» | **Adopted** — problem signal воспроизводит BABOK-диагноз stakeholder neglect как первопричину late requirements | 2015–present; review на BABOK v4 |
| **BABOK v3, ch. 6** (Strategy Analysis) | Разделение потребности и решения — корневая компетенция бизнес-анализа | `BAR.ProblemVsSolutionSeparation`: «стейкхолдер говорит "постройте кнопку X"» | **Adopted** — problem signal и AcceptanceCriterion воспроизводят BABOK-линию problem framing до solution design | 2015–present; review на BABOK v4 |
| **IREB CPRE FL 2023, ch. 4** (Requirements Elicitation) | Elicitation techniques подбираются под тип источника и класс требований | `BAR.RequirementElicitation`: «скрытые требования не выявляются» | **Adopted** — technique adequacy из AcceptanceCriterion восходит к IREB-классификации elicitation techniques | 2023–present; review на CPRE FL update |
| **Wiegers & Beatty, 3rd Ed., ch. 11** (Characteristics of a Good Requirement) | Характеристики качества требования: complete, correct, feasible, necessary, prioritized, unambiguous, verifiable | `BAR.RequirementSpecification`: «требование нельзя проверить» | **Adopted** — MandatoryConstraints и CharacterizationRelation воспроизводят Wiegers-характеристики | 2013–present; review при выходе 4th Ed. |
| **Wiegers & Beatty, 3rd Ed., ch. 14** (Requirements Prioritization) | Без явной приоритизации каждый стейкхолдер считает свои требования наивысшим приоритетом | `BAR.RequirementPrioritization`: «200+ требований, все критичные» | **Adopted** — problem signal и MandatoryConstraints воспроизводят Wiegers-диагноз отсутствия explicit prioritization criteria | 2013–present; review при выходе 4th Ed. |
| **Pohl, 2010, ch. 3** (Validation vs Verification) | Validation: «are we building the right system?» vs Verification: «are we building the system right?» (Boehm 1981) | `BAR.RequirementValidation`: «на демо стейкхолдер: это не то» | **Adopted** — Strict Distinction validation/verification в ScopeCut и governing-pattern cues | 2010–present |
| **Pohl, 2010, ch. 7** (Traceability); Gotel & Finkelstein (1994) | Traceability: «ability to describe and follow the life of a requirement in both forward and backward direction» | `BAR.RequirementTraceability`: «невозможно ответить почему мы это делаем» | **Adopted** — forward/backward trace в AcceptanceCriterion восходит к Pohl-определению traceability как directed relation | 2010–present |
| **Wiegers & Beatty, 3rd Ed., ch. 16**; BABOK v3, ch. 5 (Requirements Life Cycle Management) | Scope creep — ведущая причина провала проектов; cost-of-change растёт экспоненциально (Boehm) | `BAR.RequirementChangeManagement`: «scope creep не отслеживается» | **Adopted** — problem signal и MandatoryConstraints восходят к Wiegers-диагнозу scope creep и BABOK-дисциплине Life Cycle Management | 2013–present; review на BABOK v4 |
| **Robertson & Robertson, 4th Ed., ch. 2** (The Requirements Process) | Процесс: elicitation → analysis → specification → validation | Core Flow (Section 7): последовательность фаз | **Adopted** — последовательность фаз воспроизводит Robertson-процесс как справочный каркас | 2019–present |
| **Cohn, *User Stories Applied* (2004)** | User story как минимально-достаточная форма требования | `BAR.RequirementSpecification`: AcceptanceCriterion требует actor/role и измеримый acceptance criteria | **Adapted** — user story формат принят как один из допустимых carrier; rejected: story без acceptance criteria и problem context | 2004–present |
| **Alexander & Beus-Dukic, 2009, ch. 3-4** (Stakeholder Analysis; Viewpoints) | Stakeholder analysis через viewpoints: разные группы видят систему через разные concern-lenses | `BAR.StakeholderIdentification`: AcceptanceCriterion требует concern и канал для каждого стейкхолдера | **Adopted** — viewpoint-based stakeholder identification через требование фиксации concern и канала | 2009–present |
| **ISO/IEC/IEEE 29148:2018** | Международный стандарт инженерии требований: characteristics of good requirements, structure of requirements specification | `BAR.RequirementSpecification`: характеристики качества требования, measured acceptance criteria | **Adopted** — стандарт подтверждает Wiegers-характеристики как международно-признанный SoTA | 2018–present |
| **Mead et al., CMU/SEI** (Security Requirements Engineering) | Систематический подход: abuse cases, threat modeling, security quality attributes | `BAR.SecurityRequirements` (new card): «требования безопасности сводятся к авторизации» | **Adopted** — threat modeling и abuse cases восходят к Mead-подходу security requirements engineering | техотчёт–present |
| **ГОСТ 34.602-2020** / **РД 50-34.698-90** | Отечественная практика ТЗ на АС: прослеживаемость требований до приёмочных испытаний | `BAR.RequirementTraceability`: mandatory traceability для regulated domain | **Adopted** — требование прослеживаемости из ГОСТ 34 в MandatoryConstraints | 2020–present |
| **ISO 15288:2023** | Stakeholder requirements definition process, requirements analysis process — системная инженерия | `BAR.StakeholderIdentification`, `BAR.RequirementElicitation`: identification stakeholders и elicitation как часть системной инженерии | **Adopted** — процессы ISO 15288 подтверждают placement идентификации стейкхолдеров и elicitation в жизненном цикле | 2023–present |
| **BABOK v3, ch. 10.35** (Process Modeling) | Process modeling как источник требований: процесс не самоцель, а carrier требований | `BAR.BusinessProcessModeling`: «модель лежит на полке» | **Adopted** — problem signal воспроизводит BABOK-диагноз: модель процесса без traceability links до требований не выполняет функцию elicitation | 2015–present; review на BABOK v4 |
| **Silver, *BPMN Method and Style*** | Уровневое моделирование: descriptive → analytical → executable как стадии зрелости процессной модели | `BAR.BusinessProcessModeling`: AcceptanceCriterion требует as-is baseline и traceability links как mandatory | **Adopted** — Silver-уровни (descriptive/as-is → to-be) прямо отражены в MandatoryConstraints (запрет to-be без as-is) и ComparabilityRelation | 2009–present |
| **Cockburn, *Writing Effective Use Cases* (2000)** | Goal-driven use cases: pre/post-conditions, extensions, actor goals — «use case is a contract for behavior» | `BAR.UseCaseModeling`: «use case = UI specification» | **Adopted** — problem signal и AcceptanceCriterion из 7 пунктов восходят к Кокбёрн-структуре use case (goal, pre/post-conditions, extensions, UI-neutrality) | 2000–present |
| **BABOK v3, ch. 10.50** (Use Cases and Scenarios) | Use case как техника спецификации: actor, goal, pre/post-conditions, main flow, alternative flows | `BAR.UseCaseModeling`: AcceptanceCriterion из 7 пунктов восходит к BABOK-описанию use case technique | **Adopted** — BABOK-техника use case формализована в MandatoryConstraints (запрет UI-действий, обязательность extensions) | 2015–present; review на BABOK v4 |
| **DAMA-DMBOK2** (Data Management Body of Knowledge) | Data requirements как часть data management: quality, lifecycle, privacy, ownership | `BAR.DataRequirements`: «перечень атрибутов без правил» | **Adopted** — problem signal воспроизводит DAMA-диагноз: требования к данным не должны ограничиваться структурой; 5 аспектов AcceptanceCriterion восходят к DAMA-доменам data management | 2017–present |
| **ISO 25012** (Data Quality Model) | 15 характеристик качества данных с measurement framework | `BAR.DataRequirements`: AcceptanceCriterion требует quantified quality targets для CDE | **Adopted** — требование quantified quality targets и ComparabilityRelation по критичности восходят к ISO 25012 measurement framework | 2008–present |

> **SoTA-Echoing status:** `provisional` — строки подлежат уточнению exact page/chapter ref и проверке adoption stance при переходе к industrial-grade DPF. Currentness window review — ежегодно или при major edition change sources.

---

## 3. Architecture Decision (`E.4.PFAD`)

**`PFAD-BAR-001`**

| Слот | Значение |
|---|---|
| **FrameworkFamily** | `DomainPrincipleFramework` |
| **Purpose** | Дать инженерные паттерны проблемной стороны бизнес-анализа и работы с требованиями — до выбора нотации, шаблона документа, инструмента управления требованиями |

### First Pattern Set

1. **`BAR.StakeholderIdentification`** — Идентификация и классификация стейкхолдеров и их concerns
2. **`BAR.ProblemVsSolutionSeparation`** — Разделение проблемы и решения: ядро бизнес-анализа
3. **`BAR.RequirementElicitation`** — Выявление требований из разных источников
4. **`BAR.RequirementSpecification`** — Спецификация требований: форма, полнота, измеримость
5. **`BAR.RequirementPrioritization`** — Приоритизация требований при ограниченных ресурсах
6. **`BAR.RequirementValidation`** — Валидация требований до инвестиций в реализацию
7. **`BAR.RequirementTraceability`** — Трассировка требований от источника до приёмки
8. **`BAR.RequirementChangeManagement`** — Управление изменениями требований без scope creep

### Dependency Boundary

| Слот | Значение |
|---|---|
| **DependsOn** | `FPFCorePatternSet@current` |
| **NoCoreLanding** | `true` |
| **ReverseDependencyBlocked** | `true` |
| **PublicationUnit** | Локальный монолит (данный файл) с извлекаемыми relation records |

---

## 4. Name Preparation

| Поле | Значение |
|---|---|
| **PrimaryName** | Принциповый фреймворк бизнес-анализа и работы с требованиями |
| **PublicLabel** | `BusinessAnalysisPrincipleFramework` |
| **ProvisionalAlias** | `BAPF` |
| **F18NameCard** | См. раздел 4a |
| **NameScope** | Bounded context инженерной практики бизнес-анализа |

---

### 4a. F.18 Name Card

| Slot | Value |
|---|---|
| PublicName | Принциповый фреймворк бизнес-анализа и инженерии требований (БАПФ) |
| PublicAbbreviation | `БАПФ` / `BAPF` |
| EnglishName | Business Analysis Principle Framework |
| NameRationale | «Бизнес-анализ и инженерия требований» отражает двойной фокус: проблемная сторона бизнес-анализа (BABOK) + инженерная сторона требований (IREB, Wiegers, Pohl) |
| NameScope | Инженерная практика бизнес-анализа и работы с требованиями в проектах создания/модификации информационных систем |
| DistinctFrom | BABOK Guide (IIBA) — корпус практик, не принциповый фреймворк; IREB CPRE — syllabus, не pattern language; ГОСТ 34 — стандарт документирования, не метод работы |
| Status | provisional — требуется апробация в ≥3 проектах до заморозки |

---

## 5. Carrier Admission (`C.33`)

| Слот | Содержание |
|---|---|
| **CapturedStructure** | Контекстная декларация, source pack с SoTA-Echoing, архитектурное решение; двенадцать `ProblemCard@Context` с worked slices (near-miss, local anti-patterns, conformance checklists); expanded `E.4.PFR` relation records |
| **NotCaptured** | Полные паттерные тела `E.8` с filled worked slices (positive cases, heterogeneous transfer cases, countercases); `E.21` per-card evaluation |
| **AdmissibleUse** | P2W-ready problem-side input для практики бизнес-анализа; drafting aid для постановки задачи бизнес-аналитику |
| **NonAdmissibleUse** | Готовый «регламент» работы с требованиями без адаптации под организацию/проект; замена BABOK или IREB |

---

## 6. Problem Cards (`C.22.2`)

### 6.1 `BAR.StakeholderIdentification` — Идентификация стейкхолдеров и их concerns

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Требования собираются только от одного-двух «громких» стейкхолдеров; упущенные стейкхолдеры выходят на этапе приёмки с «это не то, что нам нужно»; носители ключевых constraints (безопасник, эксплуатация, регулятор) не опрошены |
| **ContextGrounding** | Проект создания/модификации системы с `≥3` группами интересов: бизнес-пользователи, эксплуатация, безопасность, регулятор, интеграция со смежными системами |
| **ScopeCut** | Идентификация и классификация стейкхолдеров на старте работы с требованиями; не охватывает управление ожиданиями на всём жизненном цикле |
| **NotWishReason** | «Мы и так знаем всех заинтересованных» — без явного stakeholder map/onion model пропуск holders constraints необнаружим |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Инцидент: на этапе приёмки эксплуатация заявляет «эта система не влезает в наш дата-центр» — физический constraint не был выявлен, потому что эксплуатация не была идентифицирована как стейкхолдер |
| **EntityOfConcern** | Стейкхолдер (stakeholder) — лицо/роль/организация/внешняя система, имеющая concern (интерес, требование, ограничение, риск) в отношении целевой системы |
| **SymptomDetection** | Новое требование появляется поздно (late requirement); приёмка блокируется неожиданным стейкхолдером; требование «X критично» оспорено другим стейкхолдером с «X не нужно, нужно Y» |
| **ProblemHypothesis** | Не проведён систематический stakeholder identification — команда работает с «удобными» стейкхолдерами, пропуская holders constraints, регулирующих и негативных стейкхолдеров |
| **ImprovementCheck** | Каждая функциональная область системы имеет идентифицированных стейкхолдеров; для каждого стейкхолдера зафиксирован concern и канал получения требований; время до обнаружения пропущенного стейкхолдера сокращается |
| **AcceptanceCriterion** | Stakeholder register/onion model содержит: идентификатор стейкхолдера, роль в проекте (владелец требований, владелец constraints, консультант, информируемый), concern(ы), канал коммуникации, полномочия по приёмке |
| **MandatoryConstraints** | Нельзя ограничиваться «позитивными» стейкхолдерами — holders constraints (безопасность, эксплуатация, регулятор) обязательны к выявлению; негативные стейкхолдеры (конкуренты, регулятор-запретитель) должны быть идентифицированы даже при ограниченном доступе |
| **CharacterizationRelation** | Полнота покрытия (coverage — доля типов стейкхолдеров, для которых есть представитель), своевременность идентификации (elapsed time от старта до идентификации), разнообразие concerns (не сведены ли все к «удобству использования») |
| **ValidationBoundary** | Проверка stakeholder map независимым reviewer; refresh при появлении нового функционального домена или внешней системы |
| **FreshnessOrExpiry** | `stale` при изменении оргструктуры заказчика, регуляторного поля или состава смежных систем |
| **ProblemFormulationFollowUpReason** | Устранить root cause late requirements до того, как ошибка станет стоить перепроектирования |
| **ReadinessDisposition** | `P2W-ready` для перехода к elicitation требований от идентифицированных стейкхолдеров |

#### Worked Examples

**Positive Worked Slice:** В проекте внедрения ERP бизнес-аналитик на старте построил stakeholder onion model: 4 слоя (core team, direct users, constraint holders, external). Идентифицировал инженера эксплуатации ЦОД (constraint holder) и офицера ИБ — роли, которые заказчик не назвал при первых интервью. При попытке добавить серверный компонент эксплуатация указала: «физического места в стойке нет, расширение — через 6 месяцев». Ранняя идентификация предотвратила блокировку приёмки: перепроектирование заняло 1 день вместо 2 недель.

**Near-Miss Example:** Команда провела stakeholder workshop. Stakeholder map построен, concerns зафиксированы. Через месяц эксплуатация блокирует приёмку: система не влезает в дата-центр — constraint «10 000 пользователей» зафиксирован со слов бизнес-заказчика, но носитель constraint (инженер эксплуатации) не был идентифицирован как стейкхолдер. Это проблема разделения concern ownership, а не идентификации — применяется `BAR.RequirementValidation`.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Stakeholder proxy substitution** | Бизнес-аналитик опрашивает Product Owner как «представителя всех»; требования эксплуатации и безопасности записываются со слов PO | PO не является role-holder для constraint-bearing ролей. Паттерн требует прямой идентификации holder каждого concern |
| **Positive-stakeholder bias** | Stakeholder register содержит только «дружественных» стейкхолдеров; holders constraints (безопасник, DBA, compliance) пропущены — «они всё равно скажут нет» | MandatoryConstraints прямо запрещают ограничиваться позитивными стейкхолдерами |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.SIH-1` | Stakeholder register содержит: идентификатор, роль, concern(ы), канал коммуникации, полномочия по приёмке | Операционализирует AcceptanceCriterion |
| `CC-BAR.SIH-2` | Каждая функциональная область имеет ≥1 стейкхолдера-носителя требования и ≥1 стейкхолдера-носителя constraint | Coverage функциональных областей |
| `CC-BAR.SIH-3` | Holders constraints (безопасность, эксплуатация, регулятор) явно идентифицированы | Запрет ограничения позитивными стейкхолдерами |
| `CC-BAR.SIH-4` | Негативные стейкхолдеры идентифицированы; при ограниченном доступе зафиксирована причина | MandatoryConstraints: негативные обязательны |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 2 (Business Analysis Key Concepts) | Классификация стейкхолдеров: влияние × интерес, RACI — кто и с каким весом участвует в проекте | **Adopted** — ролевая классификация отражается в AcceptanceCriterion (владелец требований, владелец constraints, консультант, информируемый) | **Extended:** BABOK классифицирует по влиянию, BAPF добавляет constraint-holder dimension (носитель constraints обязателен независимо от политического веса). Операционализация: CC-BAR.SIH-3/4 — constraint holders и негативные стейкхолдеры обязательны к выявлению |
| BABOK v3, ch. 3 (BA Planning and Monitoring) | Stakeholder identification — первая задача планирования, выполняется до elicitation | **Adopted as-is** — ScopeCut воспроизводит: идентификация строго до elicitation | Добавлен explicit freshness condition (stale при изменении оргструктуры), не присутствующий в BABOK. Anti-pattern «Stakeholder proxy substitution» называет misuse, не описанный в BABOK |
| IREB CPRE FL, ch. 2 (System and Context Boundaries) | Context boundary analysis: идентификация всех источников воздействия на систему, включая внешние системы и constraint holders | **Adopted** — MandatoryConstraints требуют идентификации holders constraints | Добавлена coverage characterization (доля типов стейкхолдеров с представителем) и explicit negative stakeholder requirement. IREB фиксирует необходимость, BAPF даёт измеримую проверку через conformance checklist |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Stakeholder как роль (Role) и её concern | `A.2`, `A.2.1` |
| Concern как problem signal до превращения в требование | `C.22.2` |
| BoundedContext для локализации значения concern | `C.11` |
| Coverage как характеризация полноты | `C.16` |
| Приоритизация стейкхолдеров и их concerns | `G.9` |

---

### 6.2 `BAR.ProblemVsSolutionSeparation` — Разделение проблемы и решения

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Стейкхолдер формулирует требование как «постройте мне кнопку X» (решение), а не «я не могу сделать Y за Z минут» (проблема); команда начинает проектировать и реализовывать решение, не поняв проблему; реализованное решение не решает действительную проблему стейкхолдера |
| **ContextGrounding** | Работа бизнес-аналитика на входе в проект/итерацию: получение входа от стейкхолдеров и превращение его в требования, пригодные для передачи в разработку |
| **ScopeCut** | Разделение problem description и solution description на этапе elicitation и analysis; не охватывает архитектурное проектирование решения |
| **NotWishReason** | «Заказчик сказал — делаем» — принятие solution-shaped request как требования без анализа проблемы |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | BABOK v3: «A requirement is a usable representation of a need» — не сама нужда и не её реализация. Wiegers: «The hardest single part of building a software system is deciding precisely what to build» |
| **EntityOfConcern** | Требование (requirement) как эпистемический артефакт — описание потребности или ограничения, из которого можно вывести критерии приёмки, НЕ описание реализации |
| **SymptomDetection** | Стейкхолдер говорит: «добавьте поле X на форму Y» (решение); бизнес-аналитик не спрашивает «какую задачу вы решаете с помощью поля X?»; команда спорит о средствах (технологический стек, фреймворк), а не о целях |
| **ProblemHypothesis** | Бизнес-аналитик не проводит problem framing — принимает solution-shaped request как requirement, пропуская шаг «какая потребность/проблема стоит за этим решением» |
| **ImprovementCheck** | Каждое требование имеет зафиксированный problem context (какую потребность удовлетворяет); стейкхолдер подтверждает, что problem description корректен; rejected alternatives (почему не подходят другие решения) зафиксированы |
| **AcceptanceCriterion** | Для требования зафиксированы: (1) problem statement (наблюдаемая проблема или потребность), (2) кто и в какой ситуации испытывает проблему, (3) как измеряется наличие проблемы сейчас, (4) что будет считаться решением проблемы (acceptance criteria), (5) rejected alternatives с причинами отклонения |
| **MandatoryConstraints** | Запрещено принимать solution-shaped request за требование без problem context; запрещено фиксировать requirement как «реализовать функциональность F» без указания, какую потребность F удовлетворяет |
| **CharacterizationRelation** | Problem clarity (может ли сторонний читатель восстановить проблему из требования), solution neutrality (насколько требование свободно от предписанного решения), testability (можно ли из требования вывести критерии приёмки) |
| **ValidationBoundary** | Проверка на `≥3` требованиях из разных функциональных областей; refresh при обнаружении, что принятое решение не решает проблему |
| **FreshnessOrExpiry** | `stale` при изменении бизнес-процесса или потребностей стейкхолдера, делающем problem statement неактуальным |
| **ProblemFormulationFollowUpReason** | Предотвратить самый дорогой дефект: «сделали не то» (решение правильное, проблема — не та) |
| **ReadinessDisposition** | `P2W-ready` для передачи требования в спецификацию и проектирование |

#### Worked Examples

**Positive Worked Slice:** В fintech-проекте стейкхолдер запросил «кнопку экспорта данных в Excel с фильтрацией и группировкой». Бизнес-аналитик применил problem framing: выяснил, что менеджер тратит 3 часа в неделю на ручную сверку данных из трёх систем (CRM, биллинг, бухгалтерия). Отделённая от решения проблема — противоречивость данных, а не отсутствие экспорта — привела к реализации scheduled reconciliation pipeline. Результат: время сверки сокращено с 3 часов до 5 минут; реализована не кнопка, а устранение корневой проблемы.

**Near-Miss Example:** Стейкхолдер: «Нужен экспорт данных в Excel с фильтрацией и группировкой». Бизнес-аналитик записал problem statement, стейкхолдер подтвердил. Выяснилось: проблема не в отсутствии экспорта (он есть), а в противоречивости данных между системами. Это не ошибка problem framing, а ошибка elicitation — не выявлен root cause. Применяется `BAR.RequirementElicitation`.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Specification disguised as problem statement** | Problem statement: «система должна обеспечивать время отклика ≤ 2 сек» — спецификация под видом problem framing | AcceptanceCriterion требует наблюдаемую проблему, субъекта и текущее состояние. Спецификация без текущего измерения — антипаттерн |
| **Problem framing as infinite regress** | Аналитик строит цепочку «five whys» до стратегии компании; команда ждёт спецификацию третью неделю | ScopeCut: problem framing на этапе анализа, не стратегический консалтинг. Достаточно одного уровня problem context |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.PVS-1` | Для каждого требования зафиксирован problem statement: наблюдаемая проблема, кто испытывает, как измеряется сейчас | AcceptanceCriterion пп. (1)-(3) |
| `CC-BAR.PVS-2` | Для каждого требования зафиксировано, что считается решением (acceptance criteria) | AcceptanceCriterion п. (4) |
| `CC-BAR.PVS-3` | Для каждого требования зафиксированы rejected alternatives с причинами отклонения | AcceptanceCriterion п. (5) |
| `CC-BAR.PVS-4` | Ни одно требование не зафиксировано как «реализовать F» без указания потребности | MandatoryConstraints |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 6 (Strategy Analysis) | Problem framing — отделение потребности от решения до определения scope; strategy analysis предшествует solution design | **Adopted** — AcceptanceCriterion требует problem statement раньше solution description | **Extended:** BABOK описывает framing как аналитическую деятельность; BAPF даёт конкретную 5-элементную структуру (problem statement, who, current measure, acceptance, rejected alternatives) и запрещает requirement без problem context через MandatoryConstraints. BABOK — guideline, BAPF — gate |
| BABOK v3, ch. 7 (Requirements Analysis and Design Definition) | Различение need и solution в спецификации требования: требование описывает потребность, не реализацию | **Adopted** — MandatoryConstraints запрещают solution-shaped request как требование без problem context | Операционализация через CharacterizationRelation: solution neutrality как измеримая характеристика. Anti-pattern «Specification disguised as problem statement» — BABOK описывает различение, BAPF даёт detection rule |
| IREB CPRE FL, ch. 3 (Requirements Elicitation) | Problem analysis vs solution design как раздельные этапы: анализ проблемы предшествует проектированию решения | **Adopted** — ScopeCut воспроизводит разделение этапов | Added freshness condition (stale при изменении бизнес-процесса) и ReadinessDisposition `P2W-ready` как gate. IREB разделяет этапы концептуально, BAPF даёт критерий готовности к переходу

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Различение Problem и Solution | `C.22.2` (ProblemCard@Context) |
| Различение описания (Description) и описываемого (EntityOfConcern) | `A.7` (Strict Distinction) |
| Requirement как эпистемический артефакт | `A.0` (Episteme), `C.2.1` |
| Приёмочный критерий как acceptance probe | `C.22.2` (acceptance probe) |
| Rejected alternatives | `G.9` (parity) |

---

### 6.3 `BAR.RequirementElicitation` — Выявление требований

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Стейкхолдеры не могут сформулировать, что им нужно, или формулируют противоречиво; бизнес-аналитик проводит интервью, но получает «всё должно работать хорошо»; скрытые (tacit) требования не выявляются, потому что стейкхолдер считает их «очевидными» |
| **ContextGrounding** | Фаза elicitation в работе с требованиями: первичный сбор информации от стейкхолдеров, документов, legacy-систем и других источников |
| **ScopeCut** | Выявление требований через подбор и применение техник elicitation; не охватывает их последующую спецификацию и валидацию |
| **NotWishReason** | «Проведём интервью и запишем, что скажут» — без подготовки структуры интервью, без кросс-валидации источников, без выявления невысказанных требований |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | BABOK v3: 50+ техник elicitation (interview, workshop, observation, document analysis, prototyping, survey). Wiegers: «Customers don't know what they want until they see it» |
| **EntityOfConcern** | Процесс elicitation как трансформация (Transformation): сырой сигнал от источника → структурированный материал требований |
| **SymptomDetection** | Стейкхолдер говорит «вы меня не поняли» после получения спецификации; требования, полученные из разных источников, противоречат друг другу; «очевидные» требования (например, время отклика ≤ 2 сек) не задокументированы |
| **ProblemHypothesis** | Не подобран адекватный набор техник elicitation под тип источника и тип требований; tacit knowledge не выявлено, потому что интервьюер не спросил о «само собой разумеющемся» |
| **ImprovementCheck** | Для каждого класса требований (функциональные, нефункциональные, constraints, бизнес-правила) определён источник и техника elicitation; противоречия между источниками выявлены и зафиксированы до спецификации |
| **AcceptanceCriterion** | Для каждого требования зафиксированы: источник (стейкхолдер, документ, система), техника elicitation, дата, контекст получения; для каждого класса требований применена как минимум одна техника, релевантная этому классу; tacit требования выявлены через observation/prototyping/T-shirt sizing |
| **MandatoryConstraints** | Запрещено полагаться на единственную технику elicitation (только интервью); запрещено принимать утверждение стейкхолдера без кросс-валидации с другим источником при высоком риске требования |
| **CharacterizationRelation** | Source diversity (количество независимых источников), technique adequacy (соответствие техники elicitation типу требования), contradiction discovery rate (доля противоречий, выявленных до спецификации vs после приёмки) |
| **ValidationBoundary** | Проверка: другой аналитик по тем же источникам восстанавливает сопоставимый набор требований; refresh при смене ключевого стейкхолдера или появлении нового источника |
| **FreshnessOrExpiry** | `stale` при изменении источника (уход стейкхолдера, обновление регулирующего документа) |
| **ProblemFormulationFollowUpReason** | Встроить систематический elicitation до спецификации — предотвратить «мы не спросили» как причину дорогих изменений |
| **ReadinessDisposition** | `P2W-ready` для перехода к спецификации требований |

#### Worked Examples

**Positive Worked Slice:** В проекте автоматизации больничного отделения бизнес-аналитик применил комбинацию structured interview (дневная смена) и observation (ночная смена). Дневное интервью с начальником отделения описывало «идеальный» процесс; observation выявил, что ночная смена ведёт параллельный бумажный журнал, обходя систему — «требуется 5-минутный перезапуск при пересменке, ночью нет времени». Tacit knowledge зафиксировано как требование: время перезапуска ≤ 30 сек. Результат: требование, не выявляемое интервью, предотвратило отторжение системы ночной сменой и дорогостоящую доработку.

**Near-Miss Example:** Бизнес-аналитик провёл интервью с 5 стейкхолдерами, document analysis и prototyping. Через 2 месяца стейкхолдер: «не учли, что ночная смена выполняет операцию X иначе» — начальник смены описал дневной процесс. Это не проблема elicitation (техники подобраны), а stakeholder identification: «оператор ночной смены» не идентифицирован. Применяется `BAR.StakeholderIdentification`.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Interview monoculture** | Аналитик применяет только интервью для всех классов требований; НФТ записаны со слов пользователей без измерения | MandatoryConstraints запрещают единственную технику. НФТ не выявляются интервью — нужен observation и document analysis |
| **Tacit knowledge extraction theatre** | Протокол: «наблюдение — 2 часа». Зафиксировано «оператор выполняет X», но не выявлено ПОЧЕМУ он делает Y до Z вопреки инструкции | AcceptanceCriterion требует выявления tacit требований. Формальное наблюдение без probing — misuse |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.REQ-1` | Для каждого требования зафиксированы: источник, техника elicitation, дата, контекст получения | Прослеживаемость до источника |
| `CC-BAR.REQ-2` | Применено ≥2 различные техники elicitation; ни один класс не опирается только на интервью | Запрет единственной техники |
| `CC-BAR.REQ-3` | Высокорисковые требования (capacity, security, regulatory) кросс-валидированы с независимым источником | Кросс-валидация |
| `CC-BAR.REQ-4` | Tacit требования выявлены через observation/prototyping/T-shirt sizing; результат зафиксирован | Tacit knowledge |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 4 (Elicitation and Collaboration) | 50+ техник elicitation с guidelines по matching technique to source; elicitation event = prepare → conduct → confirm | **Adopted** — MandatoryConstraints требуют техники под тип источника; ImprovementCheck проверяет coverage классов требований | **Extended:** BABOK описывает техники как каталог; BAPF добавляет explicit запрет единственной техники (MandatoryConstraints) и кросс-валидацию для высокорисковых требований. Anti-pattern «Interview monoculture» называет misuse, не выделенный в BABOK |
| IREB CPRE FL, ch. 4 (Requirements Elicitation) | Классификация техник по типам источников (stakeholder, document, system); criteria for technique selection | **Adopted** — ImprovementCheck: для каждого класса требований определён источник и техника | Операционализация: Conformance Checklist CC-BAR.REQ-1/2/3 превращает IREB-классификацию в проверяемые требования. IREB классифицирует, BAPF enforcement через checklist |
| BABOK v3, ch. 10.32 (Observation) | Observation technique: active/passive observation для выявления tacit knowledge и реального (не декларируемого) поведения | **Adopted** — AcceptanceCriterion требует observation/prototyping/T-shirt sizing для tacit требований | Добавлен anti-pattern «Tacit knowledge extraction theatre»: формальное наблюдение без probing — misuse, не описанный в BABOK. BABOK даёт технику, BAPF предупреждает о misuse техники |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Elicitation как трансформация (Transformation) | `A.3.4` |
| Источник требований как источник evidence | `A.10` (Evidence Graph) |
| Роль бизнес-аналитика в elicitation | `A.2.1`, `A.15` |
| Техника elicitation как MethodDescription | `A.3.2` |
| Кросс-валидация источников | `B.3` (Trust Calculus) |

---

### 6.4 `BAR.RequirementSpecification` — Спецификация требований

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Требования записаны в свободной форме на естественном языке — разработчик и тестировщик интерпретируют их по-разному; требование нельзя проверить (нет измеримого acceptance criteria); разные требования противоречат друг другу, но противоречие не обнаружено до кодирования |
| **ContextGrounding** | Фаза specification: превращение сырых материалов elicitation в документированные требования, пригодные для передачи в разработку и тестирование |
| **ScopeCut** | Спецификация отдельного требования или набора требований в рамках одного bounded context; не охватывает архитектурную спецификацию системы |
| **NotWishReason** | «Напишем SRS на 300 страниц, как в ГОСТе» — без учёта, кто и как будет использовать эту спецификацию |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Wiegers: характеристики качества требования — complete, correct, feasible, necessary, prioritized, unambiguous, verifiable. IEEE 830-1998: characteristics of a good SRS |
| **EntityOfConcern** | Требование как эпистемический артефакт с определённой структурой: идентификатор, описание, acceptance criteria, приоритет, источник, зависимости |
| **SymptomDetection** | Разработчик говорит «я сделал то, что написано», а тестировщик говорит «это не проходит приёмку» — одно и то же требование прочитано по-разному; требование содержит слова «быстро», «удобно», «надёжно» без квантификации; требование описывает «как» (экранная форма), а не «что» (функция системы) |
| **ProblemHypothesis** | Требования не проходят проверку на characteristics of a good requirement (unambiguous, verifiable, atomic) — спецификация выполнена как пересказ слов стейкхолдера, а не как инженерный артефакт |
| **ImprovementCheck** | Каждое требование проходит проверку на: однозначность (один читатель — одна интерпретация), атомарность (одно требование — одна функция/ограничение), измеримость (acceptance criteria формализованы), необходимость (прослеживается до потребности стейкхолдера) |
| **AcceptanceCriterion** | Требование содержит: (1) уникальный идентификатор, (2) описание функции/ограничения, (3) actor/role, выполняющий действие, (4) измеримый acceptance criteria, (5) приоритет, (6) источник (traceability back); нефункциональное требование содержит quantified scenario: stimulus → response → measure |
| **MandatoryConstraints** | Запрещены неоднозначные термины («быстро», «удобно», «достаточно», «при необходимости») без quantified measure; запрещено одно требование, описывающее несколько независимых функций (не атомарно); запрещено отсутствие acceptance criteria |
| **CharacterizationRelation** | Unambiguity, atomicity, verifiability, completeness (в рамках scope cut), consistency (отсутствие противоречий между требованиями), necessity (traceability до потребности) |
| **ValidationBoundary** | Независимая проверка: тестировщик по acceptance criteria может написать test case без дополнительных разъяснений; refresh при изменении требований стейкхолдера |
| **FreshnessOrExpiry** | `stale` если не проходит повторную проверку на характеристики качества при изменении контекста |
| **ProblemFormulationFollowUpReason** | Предотвратить дефекты требований — самый дорогой класс дефектов (исправление на этапе эксплуатации в 100x дороже, чем на этапе требований) |
| **ReadinessDisposition** | `P2W-ready` для передачи в разработку и тестирование |

#### Characterization Measures

| Characteristic | Measurement protocol | Target threshold |
|---|---|---|
| **Unambiguity** | Три независимых читателя (разработчик, тестировщик, стейкхолдер) читают требование и независимо формулируют ожидаемое поведение; pairwise agreement rate — доля пар «читатель A и B дали одинаковую интерпретацию» | `≥ 0.90` pairwise agreement |
| **Atomicity** | Для каждого требования проверка: содержит ли оно ровно одну функцию/ограничение? Критерий: «может ли требование быть независимо приоритизировано и протестировано?» | `≥ 0.95` требований атомарны |
| **Verifiability** | Для выборки из ≥20 требований тестировщик пишет test case ТОЛЬКО по acceptance criteria; доля требований, для которых test case написан без дополнительных разъяснений | `≥ 0.90` успешной test-case derivation |

#### Worked Examples

**Positive Worked Slice:** В govtech-проекте разработки реестровой системы бизнес-аналитик для каждого из 120 требований зафиксировал quantified acceptance criteria в формате «stimulus → response → measure». Для требования «реестр должен масштабироваться под пиковую нагрузку» зафиксировано: «при 500 одновременных запросов время ответа ≤ 3 сек для 95% запросов». На приёмке подрядчик заявил «система работает хорошо», но нагрузочное тестирование заказчика показало 15 сек при 200 пользователях. Благодаря измеримым criteria спор разрешён объективно: подрядчик признал несоответствие и выполнил доработку за свой счёт.

**Near-Miss Example:** Требование «система должна формировать отчёт в PDF с группировкой по менеджерам» — однозначно, атомарно, criteria измеримы. На приёмке стейкхолдер: «не то — нужен Excel для сводки». Problem statement правильный, но стейкхолдер не знал, что PDF не позволит обработку. Это не дефект спецификации, а ошибка validation. Применяется `BAR.RequirementValidation`.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Natural-language literature** | Требование — эссе: «Система должна обеспечивать удобный интерфейс, позволяющий быстро и эффективно обрабатывать заявки с гибкой настройкой…» | MandatoryConstraints запрещают «удобно», «быстро», «гибкой» без quantified measure |
| **Atomicity violation** | Одно требование: «регистрировать заявку, отправлять уведомление и формировать отчёт» — три независимые функции | Нарушение атомарности блокирует независимую приоритизацию и тестирование |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.RSP-1` | Каждое требование содержит: уникальный идентификатор, описание функции/ограничения, actor/role | AcceptanceCriterion пп. (1)-(3) |
| `CC-BAR.RSP-2` | Acceptance criteria измеримы; НФТ содержит quantified scenario (stimulus → response → measure) | AcceptanceCriterion п. (4) |
| `CC-BAR.RSP-3` | Требование не содержит неоднозначных терминов («быстро», «удобно», «достаточно») без quantified measure | MandatoryConstraints |
| `CC-BAR.RSP-4` | Одно требование — одна функция/ограничение (атомарность) | MandatoryConstraints: запрет неатомарных |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| Wiegers & Beatty, 3rd Ed., ch. 11 / ISO/IEC/IEEE 29148:2018, ch. 6 | Характеристики качества требования: unambiguous, complete, correct, feasible, necessary, prioritized, verifiable | **Adopted** — MandatoryConstraints и CharacterizationRelation воспроизводят характеристики качества | **Extended:** Wiegers/ISO называют характеристики; BAPF добавляет explicit запрет конкретных неоднозначных терминов («быстро», «удобно», «достаточно», «при необходимости») без quantified measure. Anti-pattern «Natural-language literature» даёт detection rule для violation, отсутствующий в Wiegers |
| IREB CPRE FL, ch. 5 (Requirements Documentation) | Структура спецификации: ID, описание, rationale, acceptance criteria, source; документация как activity | **Adopted** — AcceptanceCriterion воспроизводит IREB-структуру документированного требования | Добавлен mandatory quantified scenario формат для НФТ: stimulus → response → measure. IREB упоминает quantifiability, BAPF задаёт структурный шаблон |
| BABOK v3, ch. 7 (Requirements Analysis and Design Definition) | Quality criteria для требований; проверка спецификации на измеримость, атомарность, непротиворечивость | **Adopted** — ImprovementCheck operationalizes BABOK quality criteria | Added ValidationBoundary: тестировщик по acceptance criteria пишет test case без разъяснений. BABOK говорит о testability, BAPF даёт operational test через внешнюю проверку тестировщиком |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Характеристики качества требования | `C.16`, `A.19` (ECS) |
| Acceptance criteria как acceptance probe | `C.22.2` |
| Приоритет требования | `G.9` (parity/priority), `C.25` (Q-bundle) |
| Трассировка до источника | `A.10` (Evidence Graph) |
| Требование как эпистемический артефакт | `C.2.1` (Episteme), `E.17` (MultiView) |

---

### 6.5 `BAR.RequirementPrioritization` — Приоритизация требований

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Product backlog содержит 200+ требований, все помечены как «критичные»; команда не может объяснить, почему реализуется именно этот набор, а не другой; стейкхолдеры конфликтуют: каждый продвигает «свои» требования как наивысший приоритет |
| **ContextGrounding** | Проект с ограниченными ресурсами (время, бюджет, люди) и `≥3` конкурирующими за ресурсы стейкхолдерами |
| **ScopeCut** | Приоритизация требований в рамках одного релиза/итерации; не заменяет портфельное управление и стратегическое планирование |
| **NotWishReason** | «Всё важно, давайте сделаем всё» — отказ от приоритизации под видом «у нас гибкая методология» |

#### Conditional Fields

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

#### Characterization Measures

| Characteristic | Measurement protocol | Target threshold |
|---|---|---|
| **WSJF calculation coverage** | Для каждого приоритизированного требования проверяется наличие четырёх компонент WSJF: business value (оценка), time criticality (оценка), risk reduction (оценка), job size (человеко-часы разработчика). WSJF = (value + criticality + risk_reduction) / job_size | `≥ 0.80` требований с полным WSJF расчётом |
| **Stakeholder alignment score** | Kendall's τ (rank correlation) между итоговым приоритизированным порядком и индивидуальным ранжированием каждого стейкхолдера; среднее значение τ по всем стейкхолдерам | `τ ≥ 0.60` (среднее) |
| **Priority-realization overlap** | Jaccard similarity между top-N приоритизированных требований и фактически реализованными требованиями за релиз; N = размер спринта/релиза | `≥ 0.80` overlap |

#### Worked Examples

**Positive Worked Slice:** E-commerce-платформа готовит релиз к Чёрной пятнице. Бэклог из 85 требований, все стейкхолдеры настаивают: «критично». Бизнес-аналитик применяет WSJF (Weighted Shortest Job First) с явными критериями: бизнес-ценность (рост выручки), срочность (дедлайн Чёрной пятницы), снижение риска (вероятность падения сайта), объём работ (часы разработки). Оценка WSJF вскрывает: «кеширование чекаута» (2 дня, предотвращает 60%-ный риск сбоя) имеет в 8 раз больший WSJF-балл, чем «редизайн вишлиста» (15 дней, маржинальный рост выручки). Релиз доставляет 5 максимальных WSJF-требований в срок; Чёрная пятница проходит с нулевым даунтаймом. Релиз спасён от срыва из-за скрытого перекоса приоритетов в пользу заметных, но малополезных требований.

**Near-Miss Example:** Продакт-менеджер ранжирует backlog по ROI за квартал без учёта архитектурных зависимостей. Команда не может взять требование с высоким ROI — оно зависит от неприоритизированного инфраструктурного требования. Это не misuse приоритизации — критерий выбран, но неполон; проблема в невидимых зависимостях, требующих multi-criteria подхода.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Приоритет голосованием** | Стейкхолдеры голосуют «за» свои требования; побеждает наибольший политический вес, а не бизнес-ценность | Подменяет quantified value/cost/risk сравнение social negotiation — паттерн требует `G.9`-based trade-off, а не majority vote |
| **Приоритизация без разработки** | Аналитик ранжирует по бизнес-ценности без оценки feasibility и стоимости; top-5 требований нереализуемы в срок | Нарушает MandatoryConstraint об участии носителей ресурсных constraints — приоритет без оценки cost порождает wish list |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.PRI-1` | Для каждого требования зафиксирована оценка бизнес-ценности — не «важно», а quantified или ranked по согласованному критерию | Предотвращает «всё важно» и подмену критериев |
| `CC-BAR.PRI-2` | Оценка стоимости/усилий выполнена разработчиком, не аналитиком | Предотвращает «приоритизацию без разработки» |
| `CC-BAR.PRI-3` | Критерии приоритизации согласованы со стейкхолдерами до ранжирования, rejected criteria зафиксированы | Предотвращает «приоритет голосованием» |
| `CC-BAR.PRI-4` | Приоритизация проведена с участием носителей ресурсных constraints (разработка, эксплуатация) | Предотвращает разрыв между приоритетом и реализуемостью |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 5 (Requirements Life Cycle Management) — Prioritization | Приоритизация как процесс оценки ценности, риска, стоимости и urgency; упорядочение требований для итеративного планирования | **Adopted** — AcceptanceCriterion требует multi-factor оценки (value, cost, risk, urgency) для каждого требования | **Extended:** BABOK описывает процесс, BAPF добавляет MandatoryConstraint «запрещено декларировать всё "критичным"» и anti-pattern «Приоритет голосованием». BABOK — descriptive, BAPF — prescriptive через запреты и misuse catalog |
| BABOK v3, ch. 10.33 (Prioritization Techniques) | Классификация техник: MoSCoW, Kano, timeboxing, weighted ranking; WSJF как комбинация value × urgency × cost | **Adopted** — WSJF используется как допустимый метод; AcceptanceCriterion требует оценки по явным критериям | Добавлен MandatoryConstraint: участие носителей ресурсных constraints (разработка, эксплуатация) обязательно. BABOK фокусируется на технике аналитика, BAPF добавляет implementer role как обязательного участника. Anti-pattern «Приоритизация без разработки» |
| IREB CPRE FL, ch. 6 (Requirements Negotiation and Prioritization) | Приоритизация как multi-perspective negotiation; критерии согласуются стейкхолдерами до ранжирования, а не голосуются | **Adopted** — критерии приоритизации согласованы до ранжирования; rejected criteria зафиксированы | Операционализация: ComparabilityRelation (матрица value × cost × risk × urgency) как инструмент сравнения; Conformance Checklist CC-BAR.PRI-3/4. IREB описывает negotiation, BAPF даёт проверяемый conformance gate |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Приоритет требования как Q-bundle (value, cost, risk) | `C.25` |
| Сравнение требований (pair-choice, MoSCoW) | `G.9`, `G.0` |
| Trade-off analysis | `G.4` |
| Ordering как selected set из portfolio | `G.5` |
| Характеризация качества приоритизации | `C.16` |

---

### 6.6 `BAR.RequirementValidation` — Валидация требований

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда потратила спринт на реализацию требования, а на демо стейкхолдер говорит: «это не то, что я имел в виду»; требование задокументировано, но не проверено на выполнимость — разработка обнаруживает нереализуемое ограничение через месяц; тестировщик не может написать test case, потому что acceptance criteria не тестируемы |
| **ContextGrounding** | Фаза validation: проверка требований на корректность, полноту, выполнимость и тестируемость до передачи в разработку |
| **ScopeCut** | Валидация требований (правильные ли требования?) — в отличие от верификации (правильно ли реализованы требования?); не охватывает приёмочное тестирование |
| **NotWishReason** | «Мы записали требования со слов заказчика, значит, они правильные» — отказ от валидации под видом «заказчик всегда прав» |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Pohl: validation vs verification — validation отвечает на вопрос «are we building the right system?», verification — «are we building the system right?». Boehm (1981) — различение validation и verification впервые в инженерии ПО |
| **EntityOfConcern** | Валидированный набор требований — требования, прошедшие проверку на: stakeholder agreement, feasibility, testability, consistency, completeness |
| **SymptomDetection** | Стейкхолдер отклоняет реализованную функциональность на demo/review; требование содержит contradicting constraints («система должна быть доступна 24/7» и «профилактика каждую ночь в 3:00»); разработчик говорит «это нельзя сделать заявленным способом» через 3 недели после старта |
| **ProblemHypothesis** | Валидация не проводится систематически — команда полагается на устное «да, всё верно» от стейкхолдера без structured validation (walkthrough, inspection, prototyping, test-case derivation) |
| **ImprovementCheck** | Каждое требование проходит validation checklist: stakeholder confirms problem statement + acceptance criteria; разработчик подтверждает feasibility (без детального проектирования); тестировщик подтверждает testability; пары требований проверены на consistency |
| **AcceptanceCriterion** | Для каждого требования: (1) stakeholder signed off problem statement и acceptance criteria, (2) feasibility check пройден (architecture spike при высоком риске), (3) test-case derivation выполнен (acceptance criteria тестируемы), (4) consistency check с зависимыми требованиями пройден; для набора требований: отсутствуют неразрешённые конфликты между требованиями |
| **MandatoryConstraints** | Запрещено передавать требование в разработку без signed-off acceptance criteria; запрещено пропускать feasibility check для требований с высоким риском невыполнимости; запрещена валидация без участия implementer role (разработчик, архитектор) |
| **CharacterizationRelation** | Stakeholder agreement rate (доля требований с signed-off), feasibility risk coverage, testability rate (доля требований с derived test cases), consistency conflicts found (до реализации vs после) |
| **ValidationBoundary** | Проверка на одном релизе: доля требований, вызвавших переделку из-за validation defect; refresh при изменении требований |
| **FreshnessOrExpiry** | `stale` если требование изменено без повторной валидации |
| **ProblemFormulationFollowUpReason** | Устранить validation defects до того, как их стоимость станет неприемлемой |
| **ReadinessDisposition** | `P2W-ready` для передачи в разработку (gate: requirement accepted for implementation) |
| **UnknownHandling** | `safe-probe-needed` если feasibility сомнительна — architecture spike до commitment |

#### Worked Examples

**Positive Worked Slice:** Международная логистическая компания интегрирует систему с таможенным API перевозчика. Требование: «растаможивание груза в реальном времени с откликом ≤ 5 секунд». Бизнес-аналитик настаивает на feasibility spike до фиксации требования в бэклоге. Архитектор строит тонкий прототип за 2 дня и обнаруживает: под нагрузкой таможенный API отвечает 12–18 секунд — требование физически недостижимо с текущим вендором. Бизнес-аналитик пересогласовывает требование: «асинхронное растаможивание с уведомлением в течение 5 секунд после ответа API». Три месяца wasted development на тупиковую интеграцию предотвращены; стейкхолдер signed off пересмотренное требование с измеримыми acceptance criteria.

**Near-Miss Example:** Стейкхолдер на демо rejected функциональность — ожидал локального сохранения, а система отправляла на сервер. Acceptance criteria были signed off, feasibility проверен, test cases написаны. Проблема не в validation — скрытое ожидание не было выявлено при elicitation. Паттерн валидации применим, но не защищает от требований, отсутствующих в спецификации.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Валидация = демо прототипа** | Команда показывает прототип; стейкхолдер: «выглядит хорошо»; требование считается валидированным — acceptance criteria не проверены, feasibility не оценён | Подменяет structured validation на UX-показ. Паттерн требует проверки problem statement + testability + consistency, а не approval wireframe |
| **Валидация без разработчика** | Аналитик и стейкхолдер согласовали требование; через 2 недели разработчик: «невыполнимо на текущем стеке» | Нарушает MandatoryConstraint об участии implementer role. Feasibility без того, кто будет реализовывать — гадание |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.VAL-1` | Acceptance criteria signed off стейкхолдером с подтверждением «критерии описывают мою потребность» | Предотвращает «это не то, что я имел в виду» |
| `CC-BAR.VAL-2` | Feasibility check пройден — разработчик/архитектор подтвердил реализуемость; при высоком риске — architecture spike | Предотвращает обнаружение нереализуемых требований через недели разработки |
| `CC-BAR.VAL-3` | Test-case derivation выполнен — тестировщик написал test case без дополнительных разъяснений | Предотвращает «нетестируемые» требования |
| `CC-BAR.VAL-4` | В валидации участвовал implementer role (разработчик или архитектор) | Предотвращает «валидацию без разработчика» |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 5 (Requirements Life Cycle Management) — Validate Requirements | Проверка требований на alignment с потребностями стейкхолдера, feasibility, testability, consistency до передачи в разработку | **Adopted** — AcceptanceCriterion требует signed-off acceptance criteria + feasibility check + test-case derivation | **Extended:** BABOK описывает validation как activity аналитика; BAPF добавляет mandatory участие implementer role (разработчик/архитектор) — «Валидация без разработчика» как anti-pattern. BABOK validation — stakeholder-side, BAPF добавляет implementer-side check |
| IREB CPRE FL, ch. 8 (Requirements Validation) | Различение validation (правильные ли требования?) и verification (правильно ли реализовано?); критерии качества для validation | **Adopted** — ScopeCut фиксирует strict distinction validation vs verification; AcceptanceCriterion operationalizes quality criteria | Добавлен anti-pattern «Валидация = демо прототипа» и explicit unknown-handling tactic (safe-probe-needed → architecture spike). IREB определяет validation концептуально, BAPF даёт misuse detection и тактику работы с неизвестным |
| Pohl, 2010, ch. 3 (Validation vs Verification) | Boehm (1981) различение: validation = «are we building the right system?», verification = «are we building the system right?» | **Adopted as-is** — strict distinction в ScopeCut и governing-pattern cues восходит к Boehm/Pohl | **Adopted as-is; BAPF operationalization adds conformance checklist but no novel practice.** Значение — встраивание академического различения в operational framework с gate decision и freshness condition |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Различение validation (строим правильную систему?) и verification (правильно строим?) | `A.7` (Strict Distinction) |
| Acceptance criteria как acceptance probe | `C.22.2` |
| Feasibility check как risk condition | `C.24` (safe probe) |
| Stakeholder sign-off как gate decision | `A.21` |
| Test-case derivation как проверка testability | `C.16` |
| Конфликт требований как inconsistency в Q-bundle | `C.25` |

---

### 6.7 `BAR.RequirementTraceability` — Трассировка требований

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Невозможно ответить на вопрос «почему мы это делаем?» для конкретного требования; при изменении требования невозможно определить, какие компоненты системы и тесты затронуты; на приёмочных испытаниях нельзя подтвердить, что все требования покрыты тестами |
| **ContextGrounding** | Проект с `≥3` видами артефактов в цепочке: потребность → требование → архитектурное решение → код → тест; нормативные требования (ГОСТ 34, DO-178C, ISO 26262) к прослеживаемости |
| **ScopeCut** | Установление и поддержание traceability links между артефактами; не охватывает автоматизацию трассировки инструментом |
| **NotWishReason** | «У нас agile, документировать traceability не надо» — путаница между форматом носителя и необходимостью прослеживаемости при изменениях |

#### Conditional Fields

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

#### Worked Examples

**Positive Worked Slice:** Компания-разработчик авионики готовит сертификационный аудит DO-178C. Требование `REQ-127` (формат записи полётных данных, compliance с регламентом) имеет полную trace-цепочку: потребность стейкхолдера → `REQ-127` → design-спецификация `D-44` → модуль кода `FDRWriter.c` → тесты `T-127-1` по `T-127-8`. Аудитор случайно выбирает `REQ-127` и требует доказательств покрытия за 15 минут. Бизнес-аналитик из RM-инструмента поднимает полную цепочку forward и backward trace, включая записи о sign-off на каждом этапе. Сертификация пройдена без замечаний — traceability matrix спасла проект от потенциальной 6-месячной задержки.

**Near-Miss Example:** Команда использует JIRA с плагином traceability; все связи проставлены, coverage 100%. При изменении `REQ-31` impact analysis показывает 5 затронутых тестов, после изменения 2 падают — trace links проставлены формально, но семантически некорректны (ошибочная связь через copy-paste). Это не misuse паттерна, а проблема качества связей, требующая consistency check.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Трассировка в Excel для аудита** | Traceability matrix — Excel-файл, созданный перед аудитом; связи не обновляются при изменениях, impact analysis невозможен | Подменяет working traceability на audit artifact. Паттерн требует живых связей для impact analysis, а не статического документа |
| **Трассировка только вперёд** | Forward trace есть, обратных связей нет: от теста нельзя подняться к требованию, от требования — к потребности | Нарушает bidirectional traceability: без backward trace невозможна проверка coverage и root-cause analysis |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.TRC-1` | Для каждого требования существует forward trace до design элемента, в котором оно реализовано | Предотвращает «потерянные» требования без связи до реализации |
| `CC-BAR.TRC-2` | Для каждого требования существует forward trace до ≥1 test case | Предотвращает непокрытые тестами требования |
| `CC-BAR.TRC-3` | Для каждого test case существует backward trace до требования | Предотвращает «плавающие» тесты без родительского требования |
| `CC-BAR.TRC-4` | Для safety-critical/regulated domain: 100% требований имеют полную trace-цепочку до теста, проверено аудитом | Предотвращает compliance risk и сертификационные задержки |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 5 (Requirements Life Cycle Management) — Maintain Requirements | Traceability как дисциплина поддержания связей: потребность → требование → design → implementation → test; bidirectional trace | **Adopted** — AcceptanceCriterion требует forward и backward trace links в traceability matrix | **Extended:** BABOK описывает bidirectional trace как good practice; BAPF делает backward trace mandatory через MandatoryConstraints («запрещены "плавающие" тесты без trace до требования»). Anti-pattern «Трассировка только вперёд» называет violation точнее, чем BABOK |
| IREB CPRE FL, ch. 7 (Requirements Documentation) | Трассировка как свойство спецификации требований: forward и backward traceability для управления изменениями | **Adopted** — traceability links как enabler для impact analysis (Section 7: ChangeImpactMatrix) | Добавлены quantified метрики: coverage (доля требований с полной цепочкой), impact analysis time (≤15 мин). IREB определяет traceability как свойство, BAPF задаёт измеряемые цели |
| ГОСТ 34.602-2020 / РД 50-34.698-90 | Требование прослеживаемости от ТЗ до приёмочных испытаний как обязательное свойство документации АС | **Adopted** — MandatoryConstraints: для safety-critical/regulated domain traceability обязательна до test case | Добавлен anti-pattern «Трассировка в Excel для аудита» — формальное соблюдение ГОСТ без working traceability. ГОСТ предписывает, BAPF предупреждает об имитации соблюдения |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Trace link как Evidence Graph | `A.10` |
| Coverage как характеризация качества traceability | `C.16` |
| Requirement как эпистемический артефакт с relations | `C.2.1` |
| Связь требования с design/implementation | `C.32.ADR`, `E.17` |
| Forward/backward trace как направленный relation | `A.6.P` (Relation Precision) |
| Freshness при изменении артефактов цепочки | `G.11` |

---

### 6.8 `BAR.RequirementChangeManagement` — Управление изменениями требований

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Новые требования добавляются «по звонку» без оценки влияния на реализованные; scope creep не отслеживается — через полгода проект делает в 2x больше, чем планировалось, но ключевая функциональность не готова; изменение требования не сопровождается change impact analysis |
| **ContextGrounding** | Проект/продукт в активной разработке `> 3` месяцев, с `≥2` активными стейкхолдерами, поставляющими новые и изменяющие существующие требования |
| **ScopeCut** | Управление изменениями отдельного требования или группы связанных требований; не охватывает управление контрактом и бюджетирование |
| **NotWishReason** | «Мы agile — изменения приветствуются» без оценки стоимости изменения (cost-of-change) и без проверки, не ломает ли изменение уже работающую функциональность |

#### Conditional Fields

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

#### Worked Examples

**Positive Worked Slice:** Телеком-оператор мигрирует биллинговую систему под регуляторный дедлайн. За 30 дней до запуска директор по маркетингу требует «real-time уведомления о расходах» — оценка: 4 недели дополнительной разработки. Процесс change control срабатывает: change request `CR-77` зафиксирован, impact analysis выявляет 3 затронутых модуля и конфликт с фичей регуляторной отчётности, gate decision: deferred до post-launch релиза с документированным rationale, направленным директору маркетинга и копией регулятору. Миграция биллинга укладывается в регуляторный дедлайн; post-launch релиз доставляет уведомления без срыва compliance.

**Near-Miss Example:** Стейкхолдер просит «экспорт в PDF». Команда оформляет change request, impact analysis (1 модуль, 3 теста), оценка 3 дня. Через спринт: библиотека PDF конфликтует с лицензией продукта — изменение rejected. Change control процесс сработал корректно. Проблема не в change management, а в неполноте стейкхолдеров — юрдепартамент не был идентифицирован как holder constraint.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Изменение по звонку** | Стейкхолдер звонит разработчику: «добавь поле X, срочно». Change request не оформлен, impact не оценён; через месяц никто не помнит, почему поле существует | Нарушает MandatoryConstraint о запрете изменений baseline без change request — uncontrolled mutation требований |
| **Все изменения принимаются** | Change control board автоматически approves все запросы без trade-off с текущим scope; backlog разбухает, ключевая функциональность откладывается | Gate decision без reject/defer — backlog inflation, а не управление. Паттерн требует explicit decision с rationale |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.CHM-1` | Каждое изменение baseline оформлено как change request с идентификатором, источником и описанием изменения | Предотвращает «изменения по звонку» |
| `CC-BAR.CHM-2` | Каждый change request содержит impact analysis (требования, design, код, тесты) — подписан разработчиком | Предотвращает слепые изменения без понимания последствий |
| `CC-BAR.CHM-3` | Каждый change request имеет explicit решение (accepted/deferred/rejected) с documented rationale | Предотвращает «все изменения принимаются» |
| `CC-BAR.CHM-4` | После реализации baseline требований обновлён — зафиксирована новая версия с датой и списком изменений | Предотвращает расхождение baseline и реальности |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 5 (Requirements Life Cycle Management) — Manage Changes | Процесс управления изменениями: capture → impact analysis → gate decision → baseline update; governance stakeholders участвуют в decision | **Adopted** — AcceptanceCriterion воспроизводит полный process flow; change request → impact analysis → gate decision → baseline update | **Extended:** BABOK описывает процесс как activity description; BAPF формулирует MandatoryConstraints как prohibitions (запрещено менять baseline без CR, запрещён CR без impact analysis). BABOK — descriptive, BAPF — prescriptive через запреты |
| BABOK v3, ch. 6 (Strategy Analysis) — Scope Management | Предотвращение scope creep через explicit decision criteria: change request оценивается относительно зафиксированного scope baseline | **Adopted** — SolvabilityBand: feasible при наличии baseline; blocked без baseline | Добавлены CharacterizationRelation метрики: scope creep rate, baseline stability, change request throughput. BABOK концептуально предупреждает о scope creep, BAPF даёт количественные индикаторы. Anti-pattern «Все изменения принимаются» |
| IREB CPRE FL, ch. 9 (Requirements Management) | Управление изменениями: жизненный цикл change request, approval workflow, синхронизация связанных артефактов | **Adopted** — traceability refresh при каждом изменении baseline как часть change control | Добавлен anti-pattern «Изменение по звонку» и explicit gate decision с rationale (accept/defer/reject). IREB описывает workflow, BAPF называет violation mode и даёт detection rule |

#### Governing‑Pattern Cues

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

### 6.9 `BAR.BusinessProcessModeling` — Моделирование бизнес-процессов как источник требований

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Бизнес-процессы моделируются как самоцель: создаются as-is и to-be диаграммы, которые «лежат на полке»; модель процесса не содержит ссылок на требования к системе; изменение процесса не вызывает обновления требований; процессная модель и спецификация требований существуют в разных «мирах», не связанных traceability |
| **ContextGrounding** | Проект автоматизации/цифровизации бизнес-процессов, где бизнес-процесс является основным источником функциональных требований к системе |
| **ScopeCut** | Использование моделирования бизнес-процессов (BPMN, EPC, UML Activity) как техники выявления и обоснования требований; не охватывает BPM-автоматизацию (BPMS), имитационное моделирование и организационный дизайн |
| **NotWishReason** | «Нарисуем процесс в BPMN — и требования появятся сами» — без методики извлечения требований из модели процесса, без связи элементов модели с требованиями |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | BABOK v3: Process Modeling technique (ch. 10.35). Silver «BPMN Method and Style» — методика уровневого моделирования. BPMN 2.0 (OMG, 2011) |
| **EntityOfConcern** | Модель бизнес-процесса как эпистемический артефакт, из которого извлекаются требования — процесс не самоцель, а carrier требований к автоматизирующей системе |
| **SymptomDetection** | Бизнес-аналитик рисует BPMN-диаграмму, но не может показать, какое требование к системе вытекает из конкретного activity; при изменении процесса разработчики не знают, какие требования затронуты; to-be процесс описан, но система автоматизирует as-is |
| **ProblemHypothesis** | Моделирование процесса не интегрировано в процесс работы с требованиями — диаграмма создаётся как артефакт «для галочки», а не как structured input для elicitation требований |
| **ImprovementCheck** | Каждый элемент модели процесса, взаимодействующий с системой, прослеживается до требования; изменение процесса идентифицирует затронутые требования; модель покрывает функциональные области системы без «белых пятен» |
| **AcceptanceCriterion** | (1) Для каждого элемента процесса, взаимодействующего с системой (user task → system task, service task), зафиксировано ≥1 требование; (2) для каждого gateway определено бизнес-правило — источник требования; (3) связь «элемент процесса → требование» задокументирована (traceability link); (4) при изменении процесса traceability позволяет получить список затронутых требований за ≤30 минут; (5) as-is процесс зафиксирован как baseline; to-be содержит rationale каждого изменения |
| **MandatoryConstraints** | Запрещено моделировать to-be процесс без as-is baseline; запрещено создавать процессную модель без traceability links до требований; запрещено «оптимизировать процесс» (to-be) без problem statement — что в as-is не устраивает стейкхолдеров |
| **CharacterizationRelation** | Process-to-requirement coverage (доля элементов процесса с trace до требования), model granularity adequacy, freshness (актуальность при изменении регламентов), requirement derivation velocity |
| **ComparabilityRelation** | Сравнение as-is и to-be моделей по метрикам (время выполнения, количество ручных шагов, количество системных интеграций) — rationale для изменения требований |
| **ValidationBoundary** | Проверка: другой аналитик по модели процесса восстанавливает набор требований; refresh при изменении регламента, оргструктуры или автоматизирующей системы |
| **FreshnessOrExpiry** | `stale` при изменении бизнес-процесса без обновления модели и связанных требований; `stale` при внедрении новой системы, меняющей процесс |
| **ProblemFormulationFollowUpReason** | Связать моделирование процесса и требования, чтобы изменение процесса не вызывало «слепых» изменений в системе |
| **ReadinessDisposition** | `P2W-ready` для использования модели процесса как structured input для elicitation и спецификации требований |
| **SolvabilityBand** | `feasible` при наличии доступа к носителям процесса (владелец процесса, исполнители); `blocked` если процесс не документирован и стейкхолдеры недоступны |
| **UnknownHandling** | `safe-probe-needed` если границы процесса не определены — workshop process discovery до моделирования |

#### Worked Examples

**Positive Worked Slice:** В крупном розничном банке бизнес-аналитик построил as-is модель процесса «выдача кредита наличными». Модель выявила, что 40% шагов (14 из 35) выполняются вручную: переключение между АБС и CRM, ручная сверка данных кредитной заявки с бюро кредитных историй, бумажное согласование для сумм свыше 300 000 руб. Каждый ручной шаг стал источником требования к автоматизации: интеграция с БКИ через API, электронный маршрут согласования с цифровой подписью, единое окно операциониста. Связь «элемент процесса → требование» зафиксирована в traceability matrix, что позволило при изменении регламента ЦБ за ≤30 минут определить затронутые требования.

**Transfer:** в здравоохранении та же методика traceability «элемент процесса → требование» позволила при смене клинических регламентов (приказ Минздрава) за ≤1 день определить затронутые требования к МИС и избежать трёхмесячного перепроектирования.

**Near-Miss Example:** Команда строит BPMN-диаграмму процесса закупок, извлекает требования: «система должна отправлять заявку на склад», «система должна резервировать бюджет». Через месяц выясняется: 30% заявок возвращаются без обработки — склад не понимает, что заказано, потому что в заявке нет артикула. Диаграмма была нарисована, но проблема не в процессе — проблема в данных: номенклатурный справочник не синхронизирован между системой закупок и складом. Это не misuse BusinessProcessModeling, а дефект `BAR.DataRequirements` (требования к master data не выявлены). Применяется DataRequirements, а не перемоделирование процесса.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **BPMN как самоцель** | Бизнес-аналитик два месяца рисует диаграммы в шести уровнях декомпозиции; требования к системе не извлечены, ссылок «элемент процесса → требование» нет | AcceptanceCriterion требует traceability link для каждого элемента, взаимодействующего с системой. Модель без links — артефакт «для галочки», а не источник требований |
| **To-be без as-is baseline** | Команда сразу моделирует «целевой» процесс, не зафиксировав текущее состояние; «проблема» не задокументирована — нарисован идеальный процесс, не связанный с реальностью | MandatoryConstraints запрещают to-be без as-is baseline и problem statement. Без as-is невозможно измерить улучшение и обосновать требования |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| CC-BAR.BPM-1 | Для каждого элемента процесса, взаимодействующего с системой, зафиксировано ≥1 traceability link до требования | Операционализирует AcceptanceCriterion пп. (1) и (3): процесс как источник требований |
| CC-BAR.BPM-2 | As-is процесс зафиксирован как baseline; to-be содержит rationale каждого изменения относительно as-is | Операционализирует MandatoryConstraints: запрет to-be без as-is baseline |
| CC-BAR.BPM-3 | При изменении процесса traceability позволяет получить список затронутых требований за ≤30 минут | Операционализирует AcceptanceCriterion п. (4): impact analysis через процесс |
| CC-BAR.BPM-4 | Другой аналитик по модели процесса восстанавливает сопоставимый набор требований | Операционализирует ValidationBoundary: модель как воспроизводимый источник |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 10.35 (Process Modeling) | Process Modeling как техника elicitation: создание as-is и to-be моделей для понимания текущего и целевого процесса | **Extended** — BABOK описывает моделирование как технику; BAPF добавляет mandatory traceability link «элемент процесса → требование» и запрет to-be без as-is baseline | Substantial extension: BABOK treats process model as elicitation output; BAPF treats it as structured input to requirements, requiring traceability link from each system-interacting element. Value: process change → requirement impact analysis за ≤30 мин. Anti-pattern «BPMN как самоцель» не описан в BABOK |
| Silver, *BPMN Method and Style* | Уровневая методика моделирования: контекст → процесс → задача; focus on diagram clarity and methodological consistency | **Adapted** — Silver's levels adopted as modeling carrier; BAPF adds problem-side framing: процесс не самоцель, а источник требований | Silver фокусируется на качестве диаграмм; BAPF переориентирует моделирование на problem-side: as-is baseline → problem statement → to-be с rationale. Silver — modeling methodology, BAPF — requirement derivation methodology |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Процесс как Transformation (вход → деятельность → выход) | `A.3.4` |
| As-is / To-be различение как temporal states | `C.27` |
| Элемент процесса → требование как traceability link | `A.10`, `C.32` |
| Process coverage как характеризация полноты выявления требований | `C.16` |

---

### 6.10 `BAR.UseCaseModeling` — Моделирование вариантов использования

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Use cases пишутся как «пользователь нажимает кнопку X, система показывает экран Y» — UI-спецификация, а не описание цели пользователя; основной успешный сценарий описан, но альтернативные потоки пропущены; pre/post-conditions не проверяемы; use case не отвечает на вопрос «какую цель достигает actor?» |
| **ContextGrounding** | Проект с use case modelling как техникой спецификации функциональных требований; система имеет ≥3 типов акторов с различными целями |
| **ScopeCut** | Use case modelling как техника спецификации функциональных требований через цели акторов; не охватывает UML-нотацию как таковую, генерацию кода, сценарное тестирование |
| **NotWishReason** | «Use case — это просто текстовое описание, напишем как получится» — без структуры Кокбёрна, без goal-driven подхода, без проверяемых pre/post-conditions |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Cockburn «Writing Effective Use Cases» (2000) — goal-driven use cases. Jacobson «Use Cases: The Next Generation» (2011) — use-case 2.0 с use case slices. BABOK v3: Use Cases and Scenarios technique |
| **EntityOfConcern** | Use case как goal-driven эпистемический артефакт — описание поведения системы, приводящего к observable result of value для актора; не UI-спецификация |
| **SymptomDetection** | Use case содержит «пользователь выбирает из выпадающего списка» (UI-деталь); альтернативный поток «если что-то пошло не так» без specific failure condition; post-condition «заказ сохранён» без проверяемых критериев; 40% сценариев не описаны |
| **ProblemHypothesis** | Use case modelling — описание UI-навигации (screen flow) вместо goal-driven technique: аналитик не начинает с «какую цель преследует актор?» |
| **ImprovementCheck** | Каждый use case имеет: (1) одного primary actor с явной целью, (2) измеримый post-condition, (3) extension scenarios с specific failure/alternative conditions; не содержит UI-специфичных деталей; альтернативные потоки покрывают ≥90% documented failure modes |
| **AcceptanceCriterion** | (1) Use case начинается с goal statement: «Actor X достигает цели Y посредством системы»; (2) pre-conditions проверяемы; (3) post-conditions проверяемы и различны для main success и extension; (4) main success на уровне «actor intention → system responsibility», шаги нумерованы; (5) для каждого шага — extension conditions; (6) extensions покрывают бизнес-правила, системные отказы, таймауты; (7) use case не содержит UI-деталей |
| **MandatoryConstraints** | Запрещено описывать use case как последовательность UI-действий; запрещён use case без extension scenarios; запрещены pre/post-conditions без проверяемых критериев; запрещено смешивать цели разных акторов в одном use case |
| **CharacterizationRelation** | Goal clarity (читатель называет цель одним предложением), extension completeness, UI-neutrality, actor-goal uniqueness, post-condition verifiability |
| **ValidationBoundary** | Проверка: тестировщик по use case пишет test cases для main success и всех extensions без разъяснений; refresh при изменении бизнес-процесса или появлении нового актора |
| **FreshnessOrExpiry** | `stale` при изменении бизнес-процесса, затрагивающего цель актора; `stale` при изменении системных constraints |
| **ProblemFormulationFollowUpReason** | Устранить ошибку «use case = UI specification» до того, как она приведёт к непокрытым сценариям и переделкам |
| **ReadinessDisposition** | `P2W-ready` для передачи use case в разработку, тестирование и приёмку |
| **SolvabilityBand** | `feasible` при доступе к акторам для валидации целей; `blocked` если акторы не могут сформулировать цель |
| **UnknownHandling** | `safe-probe-needed` если граница системы не определена — контекстная диаграмма до use case modelling |

#### Characterization Measures

| Characteristic | Measurement protocol | Target threshold |
|---|---|---|
| **Goal clarity** | Независимый читатель (не автор use case) по тексту use case формулирует цель актора одним предложением; проверяется соответствие заявленному goal statement автора; доля совпадений по выборке из ≥10 use cases | `≥ 0.90` совпадений |
| **Extension completeness** | Для каждого use case: доля шагов main success, для которых зафиксированы extension conditions (бизнес-правила, системные отказы, таймауты), от общего числа шагов main success | `≥ 0.85` extension-covered steps / total steps |

#### Worked Examples

**Positive Worked Slice:** В страховой компании бизнес-аналитик начал с вопроса «какую цель преследует актор?» для каждого use case. Актор «Андеррайтер» заявил потребность в «быстром расчёте тарифа». Аналитик построил goal-driven use case «Рассчитать страховой тариф»: goal statement — андеррайтер получает тариф за ≤30 сек; pre-condition — заявка укомплектована; post-condition — тариф рассчитан и сохранён с историей. В процессе моделирования актор запросил «экран сравнения тарифов» — аналитик проверил: цель «сравнить» не заявлена бизнесом, сравнение не меняет решение о тарифе. Use case не был расширен под UI-желание; разработка ненужного экрана предотвращена. Через месяц актор подтвердил: цель достигнута без «сравнения».

**Transfer:** в телекоме goal-driven подход к use case предотвратил реализацию 12 UI-экранов «админки биллинга», которые менеджеры запросили «для удобства», но которые не соответствовали ни одной документированной цели актора — экономия 6 человеко-месяцев.

**Near-Miss Example:** Use case «Оформить полис» описан без UI-деталей: актор — Страхователь, цель — получить полис, post-condition — полис выпущен и отправлен. Extension scenarios: «Страхователь не прошёл скоринг» — система отказывает. Через месяц выясняется: скоринг возвращает не «да/нет», а три уровня риска; для среднего уровня риска требуется ручное согласование андеррайтером. Это не misuse UseCaseModeling (структура корректна), а дефект `BAR.RequirementElicitation` — бизнес-правило скоринга не было выявлено как источник требований. Применяется elicitation, а не переписывание use case.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Use case как UI flow** | Use case описывает последовательность экранов: «пользователь открывает форму X, выбирает из выпадающего списка Y, нажимает кнопку Z»; цель актора не указана | MandatoryConstraints запрещают описание как последовательность UI-действий. Паттерн требует goal statement и шаги в формате «actor intention → system responsibility» |
| **Счастливый путь без extensions** | Use case содержит только main success scenario; альтернативные потоки не описаны или описаны как «если ошибка — показать сообщение» без specific failure condition | MandatoryConstraints запрещают use case без extension scenarios. Без extensions тестировщик не может написать тесты для failure modes — до 40% сценариев не покрыто |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| CC-BAR.UCM-1 | Каждый use case имеет goal statement: «Actor X достигает цели Y посредством системы» | Операционализирует AcceptanceCriterion п. (1): goal-driven подход |
| CC-BAR.UCM-2 | Use case не содержит UI-специфичных деталей; шаги в формате «actor intention → system responsibility» | Операционализирует MandatoryConstraints и AcceptanceCriterion п. (7): UI-neutrality |
| CC-BAR.UCM-3 | Для каждого шага main success зафиксированы extension conditions, покрывающие бизнес-правила, системные отказы, таймауты | Операционализирует AcceptanceCriterion пп. (5)-(6): extension completeness |
| CC-BAR.UCM-4 | Тестировщик по use case пишет test cases для main success и всех extensions без дополнительных разъяснений | Операционализирует ValidationBoundary: testability через use case |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 10.50 (Use Cases and Scenarios) | Use cases как техника спецификации: описание взаимодействия актора с системой для достижения цели; main success + alternative flows | **Extended** — BABOK описывает use cases как технику спецификации; BAPF добавляет mandatory goal-driven структуру по Кокбёрну и explicit запрет UI-flow описаний | BABOK treats use case as one of many specification techniques; BAPF elevates goal-driven framing to mandatory structure (goal statement, actor intention → system responsibility steps) and names anti-pattern «Use case как UI flow», не выделенный в BABOK |
| Cockburn, *Writing Effective Use Cases* (2000) | Каноническая структура: goal, pre/post-conditions, extensions, UI-neutrality; use case как контракт между стейкхолдерами | **Adopted** — Cockburn-структура воспроизведена как MandatoryConstraints (goal statement, проверяемые pre/post-conditions, extensions, запрет UI-деталей) | Adopted as-is; BAPF operationalization adds conformance checklist and anti-pattern catalog but no novel practice beyond Cockburn. Anti-pattern «Счастливый путь без extensions» является прямым следствием Cockburn-требования extension completeness, не нововведением |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Actor как Role с целью | `A.2`, `A.2.1` |
| Use case goal как problem signal (потребность актора) | `C.22.2` |
| Pre/Post-conditions как acceptance probes | `C.22.2`, `A.21` |
| Extension scenario как branching (альтернатива main success) | `C.25`, `C.27` |

---

### 6.11 `BAR.DataRequirements` — Выявление и спецификация требований к данным

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Требования к данным — «система должна хранить поля: ФИО, дата рождения, телефон» — перечень атрибутов без business rules валидации, без жизненного цикла данных, без privacy/retention требований; модель данных создаётся разработчиком без участия аналитика; миграция данных с legacy-систем не учтена |
| **ContextGrounding** | Проект, где данные — центральный актив (учётная система, CRM, ERP, реестр, витрина данных); требования к данным — обязательная часть спецификации |
| **ScopeCut** | Выявление, анализ и спецификация требований к данным как подмножества требований к системе; не охватывает проектирование БД, администрирование, ETL-разработку |
| **NotWishReason** | «Данные — забота разработчика, аналитик описывает только экраны» — отказ от работы с данными, приводящий к разрыву между бизнес-требованиями и моделью данных |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | DAMA-DMBOK2 — data requirements как часть data management. BABOK v3: Data Modeling technique. ISO 25012 (Data Quality Model) — 15 характеристик качества данных |
| **EntityOfConcern** | Требование к данным — описание данных системы: структура, constraints, качество, жизненный цикл (CRUD + archive + delete), privacy/retention, миграция |
| **SymptomDetection** | Схема БД без unique constraint на телефон/email — дубликаты; «хранить историю изменений» без указания сущностей и срока; legacy-данные не соответствуют новым constraints (ИНН из 9 цифр в поле из 12); персональные данные без срока давности |
| **ProblemHypothesis** | Требования к данным не рассматриваются как самостоятельный класс требований — аналитик ограничивается «экранными формами», оставляя данные разработчику |
| **ImprovementCheck** | Каждая бизнес-сущность имеет: атрибуты с типами и constraints, бизнес-правила валидации (cross-field, cross-entity), жизненный цикл, требования к качеству (quantified), retention/privacy классификацию; legacy-данные проанализированы до миграции |
| **AcceptanceCriterion** | (1) Для каждой сущности: атрибуты (имя, тип, обязательность, уникальность), правила валидации, владелец данных; (2) для каждого правила — источник (закон, регламент); (3) для персональных данных: категория, срок хранения, условие удаления; (4) модель данных верифицирована аналитиком; (5) целевой уровень качества по ISO 25012 для каждого critical data element; (6) профилирование legacy-данных с documented issues и планом очистки |
| **MandatoryConstraints** | Запрещено ограничивать требования к данным перечнем полей без правил валидации; запрещено проектировать модель данных без участия аналитика; запрещено хранить персональные данные без срока хранения и условия удаления; запрещена миграция без профилирования и плана очистки |
| **CharacterizationRelation** | Data requirement completeness (5 аспектов: атрибуты, правила, жизненный цикл, качество, privacy), validation rule coverage, data quality target measurability, legacy data readiness |
| **ComparabilityRelation** | Сравнение целевых метрик качества по критичности сущности — CDE vs не-CDE (`G.9`) |
| **ValidationBoundary** | Проверка: разработчик по data requirements создаёт схему БД; тестировщик по data quality targets пишет тесты; refresh при изменении законодательства или регламентов |
| **FreshnessOrExpiry** | `stale` при изменении законодательства о данных; `stale` при смене data owner; `stale` при миграции legacy без повторного профилирования |
| **ProblemFormulationFollowUpReason** | Предотвратить дефекты данных — самый долгоживущий класс дефектов (некачественные данные мигрируют из системы в систему) |
| **ReadinessDisposition** | `P2W-ready` для передачи data requirements в проектирование БД и ETL |
| **SolvabilityBand** | `feasible` при наличии data owner и доступа к legacy-данным; `blocked` если data owner не назначен |
| **UnknownHandling** | `safe-probe-needed` если требования законодательства неясны — legal review до спецификации |

#### Characterization Measures

| Characteristic | Measurement protocol | Target threshold |
|---|---|---|
| **Data requirement completeness** | Для каждой бизнес-сущности проверяется наличие каждого из 5 аспектов: (1) атрибуты с типами/constraints, (2) правила валидации, (3) жизненный цикл, (4) целевые метрики качества, (5) privacy/retention классификация. Оценка: доля покрытых аспектов от 5 на сущность, усреднённая по всем сущностям | `≥ 0.90` (среднее 4.5/5 аспектов на сущность) |
| **Validation rule coverage** | Для каждой сущности: число зафиксированных правил валидации, делённое на число атрибутов сущности. Для ключевых атрибутов (ИНН, телефон, email, дата) проверяется наличие ≥1 правила; нулевое значение допустимо для неключевых атрибутов (например, комментарий) | `≥ 0.50` правил на атрибут (в среднем); `= 1.00` для ключевых атрибутов |
| **CDE quality target measurability** | Для каждого Critical Data Element (CDE): наличие quantified quality target по ≥3 dimensions ISO 25012 (accuracy, completeness, consistency, timeliness, uniqueness); доля CDE с quantified targets от общего числа CDE | `≥ 0.95` CDE с quantified targets |

#### Worked Examples

**Positive Worked Slice:** В медицинской информационной системе бизнес-аналитик специфицировал data requirements для сущности «Пациент»: атрибуты с типами и constraints, правила валидации (СНИЛС — regex + контрольная сумма), классификация персональных данных по 152-ФЗ (категория «специальные» — медицинские данные). Для каждого critical data element зафиксирован срок хранения: медкарта — 25 лет с даты последнего обращения (приказ Минздрава), согласие на обработку — 5 лет после отзыва. Retention policy в data requirements позволила: (1) настроить автоматическое удаление просроченных согласий, (2) на аудите Роскомнадзора предъявить documented policy — штраф по 152-ФЗ предотвращён.

**Transfer:** в розничной торговле quantified data quality targets для CDE «Цена» и «Остаток» (по ISO 25012) предотвратили каскадную ошибку ценообразования при синхронизации ERP с 200 точками продаж — 0 инцидентов цены vs 15 инцидентов в месяц до внедрения data requirements.

**Near-Miss Example:** Data requirements для сущности «Заявка» содержат: атрибуты, правила валидации, retention = 3 года. Через год аудит обнаруживает: в заявках хранятся персональные данные заявителей, срок истёк у 15% записей, но данные не удалены — retention policy задана на уровне сущности «Заявка», а не на уровне персональных данных внутри неё. Это не misuse DataRequirements (policy есть), а дефект классификации: privacy classification выполнена на уровне сущности, а не атрибута. Применяется уточнение по `BAR.RequirementSpecification` (atomicity data requirements), а не переписывание всего data requirements пакета.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Data requirements = перечень полей** | «Система хранит ФИО, телефон, email» — плоский список атрибутов без типов, constraints, правил валидации, без жизненного цикла и privacy classification | AcceptanceCriterion требует: атрибуты с типами/constraints, правила валидации, жизненный цикл, качество, privacy. Перечень полей покрывает ≤20% требований к данным |
| **Модель данных без аналитика** | Разработчик создал схему БД по «здравому смыслу»; бизнес-правила (уникальность ИНН, формат ОГРН, кросс-проверка дат) реализованы частично или неверно; privacy requirements отсутствуют | MandatoryConstraints запрещают проектирование модели данных без участия аналитика. Разработчик не знает business rules и regulatory constraints — результат: до 40% валидаций не реализованы |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| CC-BAR.DRQ-1 | Для каждой сущности зафиксированы: атрибуты (имя, тип, обязательность, уникальность), правила валидации, владелец данных | Операционализирует AcceptanceCriterion п. (1): структура сущности |
| CC-BAR.DRQ-2 | Для персональных данных зафиксированы: категория, срок хранения, условие удаления; источник требования (закон, регламент) указан | Операционализирует AcceptanceCriterion пп. (2)-(3) и MandatoryConstraints: privacy/retention |
| CC-BAR.DRQ-3 | Legacy-данные профилированы до миграции: documented issues, план очистки | Операционализирует AcceptanceCriterion п. (6): миграция без сюрпризов |
| CC-BAR.DRQ-4 | Разработчик по data requirements создаёт схему БД; тестировщик по data quality targets пишет тесты | Операционализирует ValidationBoundary: data requirements реализуемы и тестируемы |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 10.16 (Data Modeling) | Data Modeling как техника анализа требований: ERD, class diagrams, data dictionary; моделирование структуры данных как part of requirements analysis | **Extended** — BABOK описывает моделирование данных как технику; BAPF добавляет mandatory privacy/retention requirements, legacy profiling и обязательное участие аналитика в проектировании модели данных | Substantial extension: BABOK covers data structure modeling; BAPF adds 3 dimensions absent in BABOK — (1) privacy/retention lifecycle per attribute, (2) legacy data profiling with documented issues, (3) mandatory analyst sign-off on database schema. Anti-pattern «Модель данных без аналитика» называет misuse, не описанный в BABOK |
| DAMA-DMBOK2, ch. 3 (Data Governance) / ISO 25012 (Data Quality Model) | DAMA-DMBOK2: data governance framework — data owner, data classification, stewardship. ISO 25012: 15 dimensions качества данных | **Adopted** — DAMA data owner/classification concept и ISO 25012 dimensions использованы как source reference для AcceptanceCriterion и CharacterizationRelation | Операционализация: DAMA задаёт governance-контекст, BAPF превращает его в проверяемые требования (data quality targets для CDE, верификация через тестировщика по data quality targets). DAMA — framework, BAPF — conformance gate |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Data quality dimensions как характеризация | `C.16` |
| Business rule как constraint | `C.25`, `A.7` |
| Жизненный цикл данных как temporal states | `C.27` |
| Data owner как Role с ответственностью | `A.2`, `A.2.1` |
| Data requirement traceability до источника (закон, регламент) | `A.10` |

---

### 6.12 `BAR.SecurityRequirements` — Выявление и спецификация требований безопасности

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Требования безопасности — «должна быть авторизация и аутентификация» — без threat model, без abuse cases, без требований защиты данных in transit/at rest; ролевая модель создаётся разработчиком по предположениям; безопасность делегируется «инфраструктуре» без анализа приложения; аудит безопасности — post factum пентест |
| **ContextGrounding** | Система, обрабатывающая чувствительные данные (персональные, финансовые, коммерческая тайна) или объект КИИ |
| **ScopeCut** | Выявление и спецификация требований безопасности как класса нефункциональных требований; не охватывает пентест, security audit, проектирование архитектуры безопасности, SOC-мониторинг |
| **NotWishReason** | «Безопасность сделает инфраструктурная команда» — отказ от анализа угроз на уровне бизнес-требований |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Mead et al. «Security Requirements Engineering» (CMU/SEI) — abuse cases, threat modeling. OWASP ASVS — каталог проверяемых требований безопасности. ISO 27001. ГОСТ Р 56939-2016 — «Разработка безопасного ПО» |
| **EntityOfConcern** | Требование безопасности — описание свойства системы, противодействующего конкретной угрозе и снижающего риск до приемлемого уровня; не архитектурное решение |
| **SymptomDetection** | «Авторизация» реализована — любой залогиненный пользователь видит данные всех подразделений (нет row-level security); «пароль надёжный» без quantified criteria; API без rate limiting и аутентификации; данные между микросервисами по HTTP — «внутренняя сеть безопасна»; аудиторский запрос не удовлетворяется за ≤1 день |
| **ProblemHypothesis** | Требования безопасности не выявляются систематически — аналитик не применяет threat modeling, не формулирует abuse cases, не ранжирует угрозы по риску |
| **ImprovementCheck** | Для каждой функциональной области: идентифицированы угрозы (STRIDE), для unacceptable risk — security requirement, abuse cases покрыты для критичных сценариев, ролевая модель верифицирована бизнес-владельцем, данные классифицированы по чувствительности |
| **AcceptanceCriterion** | (1) Threat model выполнен для системы и критичных компонентов; (2) для каждой угрозы выше acceptable threshold — security requirement, снижающее риск; (3) каждый security requirement имеет проверяемый критерий (OWASP ASVS level); (4) abuse cases для top-N критичных сценариев (N ≥ 5); (5) матрица «роль × операция × объект доступа» верифицирована; (6) требования к защите: in transit, at rest, in use; (7) требования аудита: что логируется, срок хранения, доступ к логам |
| **MandatoryConstraints** | Запрещено «система должна быть защищённой» без measured criteria; запрещено проектировать ролевую модель без бизнес-владельца данных; запрещено считать сетевой периметр достаточной защитой; запрещено хранить/передавать чувствительные данные без требования шифрования |
| **CharacterizationRelation** | Threat coverage, abuse case coverage, security requirement verifiability, role model completeness, data classification coverage |
| **ComparabilityRelation** | Ранжирование угроз по риску = impact × likelihood для приоритизации security requirements (`G.9`) |
| **ParityRelation** | При ограниченных ресурсах приоритизация по risk reduction на единицу затрат обязательна (`G.9`) |
| **ValidationBoundary** | Проверка: архитектор безопасности по threat model проектирует security architecture; пентестер составляет программу тестирования; refresh при изменении функциональности, канала доступа, законодательства |
| **FreshnessOrExpiry** | `stale` при изменении threat landscape; `stale` при изменении законодательства; `stale` при появлении нового класса пользователей |
| **ProblemFormulationFollowUpReason** | Предотвратить самый опасный класс дефектов — уязвимости, найденные злоумышленником, а не аналитиком |
| **ReadinessDisposition** | `P2W-ready` для передачи security requirements в проектирование архитектуры безопасности |
| **SolvabilityBand** | `feasible` при наличии экспертизы threat modeling; `blocked` без доступа к экспертизе |
| **UnknownHandling** | `safe-probe-needed` если threat landscape неизвестен — threat modeling workshop до спецификации |

#### Worked Examples

**Positive Worked Slice:** В финтех-стартапе, строящем P2P-платформу кредитования, бизнес-аналитик провёл threat modeling workshop до начала разработки. Threat model (STRIDE) выявил угрозу «Spoofing identity»: аутентификация через SMS — злоумышленник может перехватить код через SS7-атаку. Abuse case «Мошенник оформляет заём на жертву» описал цепочку: перехват SMS → вход в аккаунт → выпуск займа → вывод на свой счёт. Risk assessment показал unacceptable risk (impact = financial loss × reputation damage). Security requirement: «все финансовые операции должны подтверждаться вторым фактором, не зависящим от телефонного номера (аппаратный токен / biometrics)». Уязвимость выявлена до пентеста; стоимость исправления на этапе требований — 0 человеко-дней против 15 дней на этапе кода.

**Transfer:** в телемедицине threat model (STRIDE) до начала разработки выявил угрозу «Information disclosure» через незащищённый WebRTC-канал видеоконсультаций — шифрование канала было специфицировано как security requirement на этапе требований; предотвращена потенциальная утечка медицинских данных 50 000 пациентов и штраф по GDPR/152-ФЗ.

**Near-Miss Example:** Security requirements: «все API должны использовать HTTPS», «пароли хешируются bcrypt», «сессии инвалидируются через 15 мин неактивности». Внешний аудит: система уязвима к horizontal privilege escalation — пользователь меняет ID в URL и видит чужие данные. Row-level security не реализована, потому что threat model не рассматривал угрозу «Information disclosure через manipulation of object reference». Это не misuse SecurityRequirements (требования специфицированы), а дефект threat model — threat coverage неполна. Применяется `BAR.RequirementElicitation` (не выявлена угроза) или повторный threat modeling, а не переписывание security requirements.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Безопасность = авторизация** | Security requirements: «администратор имеет полный доступ», «пользователь — только чтение». Threat model не выполнялся, abuse cases не написаны, защита данных in transit/at rest не специфицирована | AcceptanceCriterion требует threat model (STRIDE), abuse cases, требования защиты данных in transit/at rest/in use. Сведение к ролевой модели без threat analysis — пропуск injection, XSS, data leakage угроз |
| **Периметр как достаточная защита** | «Система за файрволом, внутренняя сеть безопасна» — API между микросервисами по HTTP без аутентификации; чувствительные данные в логах без маскирования | MandatoryConstraints запрещают считать сетевой периметр достаточной защитой. Zero-trust: угрозы действуют и внутри периметра (insider threat, lateral movement) |

#### Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| CC-BAR.SRQ-1 | Threat model (STRIDE) выполнен для системы и критичных компонентов; для каждой угрозы выше acceptable threshold зафиксировано security requirement | Операционализирует AcceptanceCriterion пп. (1)-(2): threat-driven подход |
| CC-BAR.SRQ-2 | Abuse cases покрывают top-N критичных сценариев (N ≥ 5); каждый abuse case прослеживается до security requirement | Операционализирует AcceptanceCriterion п. (4): abuse cases |
| CC-BAR.SRQ-3 | Матрица «роль × операция × объект доступа» верифицирована бизнес-владельцем данных | Операционализирует AcceptanceCriterion п. (5) и MandatoryConstraints: role model |
| CC-BAR.SRQ-4 | Каждый security requirement имеет проверяемый критерий по OWASP ASVS level; данные классифицированы по чувствительности | Операционализирует AcceptanceCriterion пп. (3), (6)-(7): verifiability и data classification |

#### Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| Mead et al., CMU/SEI *Security Requirements Engineering* | Систематический подход: abuse cases + threat modeling (STRIDE) для выявления security requirements до начала разработки | **Adopted** — AcceptanceCriterion требует threat model и abuse cases как mandatory steps; Mead-подход воспроизведён полностью | **Extended:** Mead определяет подход концептуально; BAPF добавляет mandatory OWASP ASVS level-based verifiability для каждого security requirement, anti-pattern «Безопасность = авторизация» и MandatoryConstraint о недостаточности сетевого периметра. Mead — methodology, BAPF — conformance gate с проверяемыми критериями |
| OWASP ASVS | Каталог проверяемых security requirements с уровнями (L1/L2/L3): требования к аутентификации, авторизации, защите данных, логированию | **Adopted** — ASVS level используется как quantified критерий: каждый security requirement должен иметь проверяемый критерий по OWASP ASVS level | Операционализация: ASVS — каталог, BAPF требует selection конкретного level для каждого требования и проверку через Conformance Checklist CC-BAR.SRQ-4. ASVS describes what to check, BAPF requires it as acceptance gate |
| ISO 27001 / ГОСТ Р 56939-2016 | ISO 27001: governance framework ИБ. ГОСТ Р 56939: требования к разработке безопасного ПО | **Adopted** — использованы как regulatory source reference для MandatoryConstraints | Adopted as-is for regulatory binding; BAPF не добавляет novel practice поверх ISO/ГОСТ, но встраивает их как mandatory reference в problem-side framework (не в governance document) |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Threat model как identification угроз (problem signals безопасности) | `C.22.2` |
| Abuse case как негативный сценарий (что система не должна допустить) | `C.24`, `C.22.2` |
| Security requirement как constraint в Q-bundle (снижение риска как value) | `C.25` |
| Ранжирование угроз по риску (impact × likelihood) как parity ordering | `G.9` |
| Role-Based Access Control (роль × операция × объект) как Role pattern | `A.2`, `A.2.1` |

---

## 7. Relation Records (`E.4.PFR`)

### Expanded Relation Map

| Source | Target | Relation Kind | Relation Function | Reversibility |
|---|---|---|---|---|
| `BAR.StakeholderIdentification` | `BAR.RequirementElicitation` | `inputTo` | Идентифицированные стейкхолдеры — обязательный вход для elicitation | Необратимая: без stakeholder list elicitation неполна |
| `BAR.StakeholderIdentification` | `BAR.RequirementPrioritization` | `informs` | Полномочия стейкхолдеров по приёмке определяют вес требований | Частично обратимая: приоритизация может выявить неучтённых стейкхолдеров |
| `BAR.StakeholderIdentification` | `BAR.RequirementValidation` | `constrains` | Только идентифицированные стейкхолдеры могут signed off требования | Частично обратимая: validation может обнаружить missing stakeholder |
| `BAR.RequirementElicitation` | `BAR.ProblemVsSolutionSeparation` | `inputTo` | Elicitation поставляет сырой материал; problem framing отделяет потребность от решения | Необратимая: без elicitation нечего разделять |
| `BAR.RequirementElicitation` | `BAR.RequirementSpecification` | `inputTo` | Выявленные требования — вход для спецификации | Необратимая: без elicitation спецификация не опирается на источники |
| `BAR.ProblemVsSolutionSeparation` | `BAR.RequirementSpecification` | `inputTo` | Problem statement + acceptance criteria — обязательный вход для спецификации | Необратимая: без problem framing спецификация теряет grounding |
| `BAR.ProblemVsSolutionSeparation` | `BAR.RequirementPrioritization` | `informs` | Problem severity — критерий приоритизации | Частично обратимая: приоритизация может показать, что «проблема» не критична |
| `BAR.RequirementSpecification` | `BAR.RequirementValidation` | `inputTo` | Специфицированное требование — вход для валидации | Необратимая: без спецификации нечего валидировать |
| `BAR.RequirementSpecification` | `BAR.RequirementPrioritization` | `inputTo` | Специфицированные требования — вход для приоритизации | Необратимая: приоритизация без spec рискует ранжировать нереализуемое |
| `BAR.RequirementSpecification` | `BAR.RequirementTraceability` | `inputTo` | Требование с ID — начало цепочки трассировки | Необратимая: без ID trace link не к чему привязывать |
| `BAR.RequirementValidation` | `BAR.RequirementTraceability` | `triggers` | Валидированное требование запускает создание trace links | Необратимая: traceability стартует от валидированного требования |
| `BAR.RequirementValidation` | `BAR.RequirementPrioritization` | `feedsBack` | Валидация может выявить нереализуемость → пересмотр приоритета | Обратимая: validation ↔ prioritization — цикл |
| `BAR.RequirementPrioritization` | `BAR.RequirementChangeManagement` | `constrains` | Приоритеты определяют порог принятия change requests | Частично обратимая: change request может инициировать пересмотр приоритетов |
| `BAR.RequirementTraceability` | `BAR.RequirementChangeManagement` | `enables` | Traceability links — necessary precondition для impact analysis | Необратимая: без traceability change management слеп |
| `BAR.RequirementTraceability` | `BAR.RequirementValidation` | `supports` | Traceability позволяет проверить coverage: валидированные требования → тесты | Частично обратимая: validation выявляет gaps в traceability |
| `BAR.RequirementChangeManagement` | → *all patterns* | `triggers` | Change request запускает обновление: re-elicit, re-spec, re-validate, re-prioritize, re-trace | Обратимая: change → полный цикл обновления всех паттернов |

### Core Flow Diagram (Expanded with Feedback Loops)

```
  StakeholderIdentification ──inputTo──▶ Elicitation ──inputTo──▶ ProblemVsSolutionSeparation
         │               ▲                                        │
         │               │                                        │ inputTo
         │               │                                        ▼
         │               │                                  Specification
         │               │                              ┌───────┼───────┐
         │               │                         inputTo inputTo inputTo
         │               │                              │       │       │
         │               │                              ▼       ▼       ▼
         │               │                        Prioritization  │  Traceability
         │               │                              │  ▲      │  ▲
         │               │                              │  │      │  │
         │            informs                       constrains│    │  │
         │               │                              │ feedsBack│  │
         │               │                              ▼  │      ▼  │
         │               └────────── informs ──── Validation  │    │  │
         │                     (stakeholder weight)      │     │    │  │
         │                                               │triggers  │  │
         │                                               ▼     │    │  │
         └─────────── constrains ────▶ ChangeManagement ◀──────┘    │  │
         (sign-off authority)            │         ▲                │  │
                                         │         │  enables       │  │
                                         │         └── Traceability ─┘  │
                                         │                               │
                                         │ triggers (re-elicit, re-spec, │
                                         │ re-validate, re-prioritize,   │
                                         │ re-trace)                     │
                                         └───────────────────────────────┘

  [P2W] gate после Validation: requirement accepted for implementation
```

### Change Impact Matrix

| If this pattern changes | Then review these patterns | Because |
|---|---|---|
| `BAR.StakeholderIdentification` | `BAR.RequirementElicitation`, `BAR.RequirementPrioritization`, `BAR.RequirementValidation` | Новый/удалённый стейкхолдер меняет: список источников, вес требований, круг sign-off |
| `BAR.ProblemVsSolutionSeparation` | `BAR.RequirementSpecification`, `BAR.RequirementPrioritization` | Изменение problem statement требует переспецификации; новая severity меняет приоритет |
| `BAR.RequirementElicitation` | `BAR.ProblemVsSolutionSeparation`, `BAR.RequirementSpecification` | Новый материал требует problem framing; могут потребоваться новые спецификации |
| `BAR.RequirementSpecification` | `BAR.RequirementValidation`, `BAR.RequirementPrioritization`, `BAR.RequirementTraceability` | Изменение acceptance criteria требует перевалидации; изменение структуры ломает trace links |
| `BAR.RequirementPrioritization` | `BAR.RequirementChangeManagement` | Изменение критериев/приоритетов меняет порог принятия change requests |
| `BAR.RequirementValidation` | `BAR.RequirementSpecification`, `BAR.RequirementTraceability` | Failed validation → переспецификация; изменение validation status меняет traceability |
| `BAR.RequirementTraceability` | `BAR.RequirementChangeManagement`, `BAR.RequirementValidation` | Изменение traceability-модели меняет точность impact analysis |
| `BAR.RequirementChangeManagement` | *ALL patterns* | Change process затрагивает все паттерны: re-elicit, re-spec, re-prioritize, re-validate, re-trace |
| `BAR.BusinessProcessModeling` | `BAR.RequirementElicitation`, `BAR.RequirementTraceability` | Изменение процесса требует пересмотра требований и traceability links |
| `BAR.UseCaseModeling` | `BAR.RequirementSpecification`, `BAR.RequirementValidation` | Изменение use case требует переспецификации и перевалидации |
| `BAR.DataRequirements` | `BAR.RequirementSpecification`, `BAR.RequirementValidation`, `BAR.RequirementTraceability` | Новые требования к данным требуют спецификации, валидации и трассировки |
| `BAR.SecurityRequirements` | `BAR.RequirementSpecification`, `BAR.RequirementValidation`, `BAR.RequirementPrioritization` | Security requirements имеют приоритет выше бизнес-требований в regulated domain |

### Edition Dependency

| Слот | Значение |
|---|---|
| **FrameworkEditionRef** | `BusinessAnalysisPrincipleFramework@Draft` |
| **DependsOnEditionRefs** | `FPFCorePatternSet@current` |
| **DependencyReason** | Все governing‑pattern cues ссылаются на FPF Core |
| **CompatibilityBoundary** | При изменении `C.22.2`, `A.10`, `C.16`, `A.21`, `G.9`, `C.25`, `G.11`, `C.27` — пересмотреть ProblemCard‑поля и relation records |
| **E53ConformanceNote** | Требуется проверка после стабилизации имён паттернов |

---

## 8. Publication

| Слот | Значение |
|---|---|
| **ThisFile** | Локальный монолит первого входа |
| **PublicationScope** | Бизнес-аналитики, системные аналитики, product owners, технические лиды, менеджеры проектов |
| **FirstEntryCarrier** | `BABusinessAnalysis-dpf.md` — читается как единый документ |
| **RelationRecordsCarrier** | Секция 7; подлежит извлечению в отдельный PFR‑файл при росте |
| **NonPublicationNote** | `FPF-Spec.md` не модифицируется; Core не расширяется |

---

## 9. Quality Route

### Evaluation Characteristics

| Характеристика | Вопрос |
|---|---|
| **Discoverability** | Может ли бизнес-аналитик найти нужный ProblemCard за `≤2 минуты`? |
| **SourceFidelity** | Восстановимы ли adopted sources (BABOK, IREB, Wiegers) в problem signals и acceptance criteria? |
| **OntologyClarity** | Разделены ли problem‑side record (ProblemCard), решение (design) и work planning (MethodDescription → Work)? Различимы ли requirement, specification, acceptance criteria? |
| **ThinAffordance** | Каждый ProblemCard читается за `≤5 минут` экспертом? |
| **Refreshability** | Видны ли explicit stale/refresh условия для каждого ProblemCard? |
| **Composability** | Может ли бизнес-аналитик использовать как весь DPF, так и отдельный ProblemCard независимо? |

### Quality Framework

| Шаг | Владелец | Назначение |
|---|---|---|
| 1 | `E.22` | Framing evaluation purpose |
| 2 | `E.21` | Pattern‑quality evaluation каждого ProblemCard |
| 3 | `E.23` | Improvement loop — добавление worked slices, anti‑patterns, SoTA‑Echoing |
| 4* | `E.19` | Admission review (при росте фреймворка) |

### E.22 Improvement-Oriented Quality Evaluation Frame (Second Pass)

**QualityEvaluationQuestionFrame:**

| Slot | Value |
|---|---|
| **Object version under quality evaluation** | `BusinessAnalysisPrincipleFramework@Draft (second pass)` — 12 ProblemCards с worked slices, SoTA-Echoing, expanded PFR |
| **Object-under-improvement evaluation** | `E.21` (FPF Pattern-Quality Evaluation CharacteristicSpace) |
| **Evaluation purpose selection** | `floorEvaluation` + `exceptionalImprovementEvaluation` |
| **Declared quality floor** | `4 wellExpressedForDeclaredUse` на RequiredPatternQualityCoordinates для declared use: «P2W-ready problem-side input для практики бизнес-анализа» |
| **Desired improvement aim** | Подтвердить, что second-pass DPF достиг floor на ключевых координатах; выявить remaining below-floor координаты для следующего improvement pass |
| **Protected trade-offs** | `usability` (thin affordance — ≤5 мин/карта), `locality` (карты самодостаточны), `source preservation`, `corpus ecology` |
| **Expected evidence basis** | Текущее тело v.SecondPass; BABOK v3, IREB CPRE FL 2023, Wiegers 3rd Ed., Pohl 2010, Robertson 4th Ed., ISO 29148, ISO 15288, ГОСТ 34; FPF Core June 2026 |
| **Expected result form** | `E.21` result: все 19 координат, PrecisionRestorationProfile, статус, stop condition |
| **Non-use boundary** | Не является `E.19` admission review, release gate, project evidence, assurance claim |

### E.21 Pattern-Quality Evaluation — Second Pass Delta

**E.21 result (фреймворк как целостная публикационная единица):**

| Slot | Value |
|---|---|
| **Pattern of concern** | `BusinessAnalysisPrincipleFramework@Draft` (full file, 12 cards + spine) |
| **Declared scope** | P2W-ready problem-side input для практики бизнес-анализа |
| **Working reader** | Бизнес-аналитик, системный аналитик, PO, технический лид |
| **Qualification window** | June 2026, FPF Core current, BABOK v3/IREB FL 2023 as SoTA front |

**PrecisionRestorationProfile:**

| Layer | Effect |
|---|---|
| **overallEffect** | `boundedLocal` — precision-restoration issues локальны, не блокируют reading flow |
| **wordHeadUsePrecision** | `clean` — FPF-governed wording used consistently |
| **kindRestorationCheck** | Not triggered — no wording repair proposals that change kind/relation |
| **phraseApparatus** | `clean` — no boilerplate overwrap detected |
| **repetitionAndNegativeDistribution** | `bounded-local` — некоторые mandatory constraints дублируются между ProblemCard и Conformance Checklist (by design: checklist операционализирует constraint) |
| **onticAndSlotRelationClarity** | `clean` |
| **descriptionPublicationSourceBoundary** | `clean` |
| **patternApplicationOntology** | `clean` |
| **affectedCoordinates** | `UseAffordabilityAndApparatusProportionality` may be stressed by added volume |
| **repairProposal** | No repair — current duplication is bounded (checklist-as-operationalization, not copy-paste) |

**RequiredPatternQualityCoordinates evaluation:**

| Coordinate | Pre-pass | Second pass | Delta rationale |
|---|---|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | 3 | **4** | Problem signals already strong; near-miss examples added per card улучшают recognition границ |
| `EntityOfConcernAndClaimScopeStability` | 3 | **4** | EoC стабилен across all 12 cards; SoTA-Echoing grounding усиливает claim scope |
| `PatternApplicationGuidance` | 2 | **4** | Anti-patterns и conformance checklists операционализируют guidance; each card specifies what NOT to do |
| `ClosureAndBoundedNonUseRecoverability` | 2 | **3** | Stop/repair conditions per card; non-use improved through near-miss → "this is NOT this pattern, use pattern X"; remains at 3 — no worked stop/overturn case yet |
| `NeighborAuthorityAndBoundedUseFit` | 2 | **4** | Expanded PFR с relation kind и reversibility; Change Impact Matrix; related-pattern statements named by value |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | 3 | **3** | Карты lead with EoC; добавление worked slices не сместило фокус; остаётся 3 — precision-restoration profile показывает bounded-local effect |
| `PracticalUseDeltaAndHarmPrevention` | 2 | **4** | Worked slices демонстрируют practical delta через near-miss и anti-pattern examples; checklist items named harm |
| `UseAffordabilityAndApparatusProportionality` | 3 | **2→3** | Объём вырос существенно (~900→~1000 строк). Каждая карта всё ещё читается за ≤5 мин, но общий размер может затруднить first-entry reading. Protected trade-off: usability под давлением |
| `RepairLocalityAndChangeImpactPredictability` | 3 | **4** | Change Impact Matrix в Section 7; каждая карта имеет explicit refresh conditions |
| `ProxyForValueSubstitutionResistance` | 2 | **3** | CharacterizationRelation названы; no explicit proxy case yet |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | 2 | **4** | SoTA-Echoing table с adoption stance и currentness window на каждый pattern signal; source refs per card |
| `CaseCountercaseAndTransferCoverage` | 1 | **3** | Near-miss examples + anti-patterns per card = case coverage создана; остаётся 3 — lacking heterogeneous transfer cases и filled worked cases (только near-miss) |
| `MaturePatternParityAndSelectedContentSufficiency` | 1 | **3** | SoTA-Echoing называет sources, но mature comparator parity (comparison с BABOK/IREB как full frameworks) не выполнена; selected ingredients named but not discharged by value with comparator IDs |
| `SoTABindingAndCurrentness` | 1 | **4** | SoTA-Echoing table with adoption stance, currentness window, and reopen conditions; SoTA-binding achieved for all 8 core + 2 смежные cards |
| `FormalClaimAdmissibilityAndLensFit` | 2 | **2** | No formal measurement/lens claims made — admissible absence; но CharacterizationRelation не имеют quantified measures |
| `FalsifiabilityAndLoweringCondition` | 2 | **3** | FreshnessOrExpiry explicit per card; lowering and reopen conditions через currentness window в SoTA-Echoing; still implicit for some coordinates |
| `CorpusEntryProjectionAndEcologyFit` | 2 | **3** | Monolith self-contained; section cross-references exist; no README/ToC/I.2 projection evidence for corpus-facing claim |
| `EvolutionFrontAndRefreshDiscipline` | 2 | **3** | Refresh triggers per Section 10; SoTA-Echoing currentness windows; no variant/front/archive discipline yet |

**PatternQualityStatus:** `repairBeforeUse` — floor `4` не достигнут на координатах `ClosureAndBoundedNonUseRecoverability` (3), `EntityOfConcernPrimacyAndSemioBiasResistance` (3), `UseAffordabilityAndApparatusProportionality` (2), `CaseCountercaseAndTransferCoverage` (3), `MaturePatternParityAndSelectedContentSufficiency` (3), `FormalClaimAdmissibilityAndLensFit` (2), `CorpusEntryProjectionAndEcologyFit` (3).

**E.21 Delta Summary:**

| Phase | Below-floor coordinates | Floor coordinates | Exceptional coordinates |
|---|---|---|---|
| Pre-pass (first-hour route) | 17 из 19 | 2 из 19 (`WorkingSituation`, `UseAffordability`) | 0 |
| Second pass | 7 из 19 | 12 из 19 | 0 |

**Key gains:** SoTA-Echoing (+3), NeighborAuthority (+2), CaseCoverage (+2), PracticalUseDelta (+2), PatternApplicationGuidance (+2), ClaimTraceability (+2).

**Key remaining gaps:** UseAffordability под давлением от роста объёма (требуется thin-affordance ревизия); CaseCountercase lacks heterogeneous transfer cases; MaturePatternParity не выполнена (comparator-by-value discharge); FormalClaimAdmissibility — characterization без quantified measures.

**First repair:** `UseAffordabilityAndApparatusProportionality` — рассмотреть выделение Conformance Checklists в отдельный carrier (appendix) или компактизацию через reference-based формат.

**Stop condition:** Достигнут значимый прогресс (12 из 19 координат на floor 4). Следующий pass — `exceptionalImprovementEvaluation` targeting remaining below-floor coordinates через `E.23` loop.

**Reopen if:** FPF Core edition изменяет `C.22.2`, `E.8`, или `E.21` coordinate definitions; новая редакция BABOK/IREB меняет SoTA claims; adoption telemetry показывает misuse patterns не покрытые existing anti-patterns.

### Per-Card E.21 Quality Evaluation (Third Pass Compact)

**Core cards (6.1–6.8):** все `admissibleForDeclaredUse` (avg 3.4–4.2 per card). **New cards (6.9–6.12):** все `repairBeforeUse` (avg 2.4–2.8) — требуется full 19-coordinate E.21 и heterogeneous transfer cases.

| Card | Avg | Status | Key gap |
|---|---|---|---|
| 6.1 `StakeholderIdentification` | 3.8 | admissible | CaseCoverage — нет heterogeneous transfer cases |
| 6.2 `ProblemVsSolutionSeparation` | 4.0 | admissible | CaseCoverage — нет positive worked slice в heterogeneous domain |
| 6.3 `RequirementElicitation` | 3.8 | admissible | CaseCoverage — нет technique selection method description |
| 6.4 `RequirementSpecification` | 3.4 | admissible | FormalClaimAdmissibility — characterization без measurement protocol |
| 6.5 `RequirementPrioritization` | 3.6 | admissible | ClosureAndBoundedNonUse — recovery pathway при провале приоритизации имплицитен |
| 6.6 `RequirementValidation` | 3.8 | admissible | ClosureAndBoundedNonUse — нет explicit recovery при систематическом провале gate |
| 6.7 `RequirementTraceability` | 3.4 | admissible | CaseCoverage — нет heterogeneous transfer cases |
| 6.8 `RequirementChangeManagement` | 4.2 | admissible | Falsifiability — lowering condition при accuracy < 70% не задан |
| 6.9 `BusinessProcessModeling` | 2.4 | repairBeforeUse | CaseCoverage + full 19-coordinate E.21 отсутствуют; SoTA-Echoing и worked examples — есть |
| 6.10 `UseCaseModeling` | 2.6 | repairBeforeUse | CaseCoverage + full 19-coordinate E.21 отсутствуют; SoTA-Echoing и worked examples — есть |
| 6.11 `DataRequirements` | 2.4 | repairBeforeUse | CaseCoverage + full 19-coordinate E.21 отсутствуют; SoTA-Echoing и worked examples — есть |
| 6.12 `SecurityRequirements` | 2.8 | repairBeforeUse | CaseCoverage + full 19-coordinate E.21 отсутствуют; SoTA-Echoing и worked examples — есть |

> **Evaluation scope:** Compact 5-coordinate per-card evaluation focusing on наиболее релевантные координаты для типа карты. Полная 19-координатная per-card evaluation — pending fifth pass.

---

## 10. Currentness Route (`G.11`)

### Refresh Triggers

- Изменение FPF Core edition (особенно `C.22.2`, `A.10`, `A.21`, `G.9`, `C.16`)
- Выход новых редакций BABOK (IIBA) или CPRE (IREB)
- Adoption telemetry: повторяющиеся misuse patterns (card-as-work-request, readiness shortcut, пропуск problem framing)
- Появление новых регуляторных требований к документированию требований (ГОСТ, ISO)
- Локальные инциденты: requirement defect, вызвавший переделку с unacceptable cost-of-change

### Stale Indicators

- Каждый ProblemCard содержит explicit freshness condition
- Ревизия всего фреймворка: ежегодно или при major Core edition change
- Deprecation: через `superseding` relation record при замене ProblemCard

### Ownership

| Роль | Владелец |
|---|---|
| **FrameworkEditionOwner** | Функция бизнес-анализа организации/проекта |
| **SourcePackOwner** | Тот же |
| **RelationRecordsOwner** | Тот же |
| **RefreshPlanOwner** | Ведущий бизнес-аналитик / руководитель практики |

---

## 11. E.19 Admission Review Gate

| Gate criterion | Status | Evidence |
|---|---|---|
| All ProblemCards at floor 4 on framework-level E.21 | PARTIAL: 12/19 coordinates at 4, 7 below | E.21 third-pass delta evaluation (Section 9) |
| All cards individually admissibleForDeclaredUse | PARTIAL: 8/12 admissible, 4 repairBeforeUse | Per-card E.21 compact evaluation: 6.1–6.8 admissible; 6.9–6.12 repairBeforeUse (avg 2.0–2.4) |
| SoTA-binding complete for all cards | YES | SoTA-Echoing table (Section 2): 21 rows covering all 12 ProblemCards with adoption stance and currentness window. 6.9–6.12 received SoTA entries in fourth pass |
| Comparator-by-value discharge present | YES | Section 6: Mature Comparator Parity tables (4 columns: comparator prescription → BAPF relation → value delta) for all 12 cards |
| Heterogeneous transfer evidence | PARTIAL | 4 transfer cases for 6.9–6.12 (healthcare, telecom, retail, telemedicine); core cards 6.1–6.8 lack explicit cross-domain transfer cases (only within-domain positive slices) |
| Carrier publication form conformant | YES | Single markdown file, C.33 carrier admission declared (Section 5) |
| Non-use boundary explicit | YES | Section 1 Non-Use Boundary |
| Source pack complete | YES | 16 adopted sources, rejected sources, SoTA-Echoing table with adoption stance and currentness window |
| F.18 name card | YES | Section 4a: F.18 Name Card — provisional with DistinctFrom and статусом |
| Refresh route current | YES | Section 10: per-card FreshnessOrExpiry, stale indicators, refresh triggers, ownership |

**Admission decision:** HOLD — not yet admissible for industrial-grade publication. Resolved: comparator-by-value discharge (12/12), F.18 name card, SoTA-binding (12/12), Characterization Measures (4 weakest cards). Remaining: 4 cards (6.9–6.12) at repairBeforeUse — need full 19-coordinate E.21 to confirm admissibility; heterogeneous transfer cases for core cards 6.1–6.8 (only within-domain positive slices, no explicit cross-domain evidence); UseAffordability at coordinate 2 (volume pressure from 1356-line monolith). Recommended next: add 1 cross-domain transfer case per core card → per-card full 19-coordinate E.21 for 6.9–6.12 → re-evaluate → admit.

---

## Authorship Annotation

| Слот | Значение |
|---|---|
| **AuthorshipNote** | Создан как first‑hour route. Second pass: E.22→E.21→E.23 — SoTA-Echoing, worked slices, anti-patterns, checklists, 4 новых ProblemCard, expanded PFR, ГОСТ/ISO источники. Third pass: thin‑affordance revision (3→2 anti-patterns, 6→4 checklist items), positive worked slices (все 12 карт), Mature Comparator Reference (BABOK/IREB mapping), per‑card E.21 evaluation. Fourth pass: comparator‑by‑value discharge (Mature Comparator Parity — 12 карт), F.18 name card, E.19 admission review, SoTA‑Echoing entries for 6.9–6.11 |
| **FPFCompliance** | Spine: context → source pack → PFAD → names → patterns → relations → quality → refresh; `C.22.2` ProblemCard@Context; governing‑pattern cues; `C.33` carrier admission; `E.22` frame; `E.21` evaluations (framework-level + per-card compact); `E.23` methodology applied; `E.19` admission review; `F.18` name card |

### Completed (Fourth Pass)

- [x] Comparator‑by‑value discharge: Mature Comparator Parity для всех 12 карт (заменил Mature Comparator Reference)
- [x] F.18 Name Card: Section 4a — PublicName, EnglishName, NameRationale, DistinctFrom, provisional status
- [x] E.19 Admission Review Gate: формальная gate проверка перед industrial-grade publication
- [x] SoTA-Echoing entries для 6.9 `BusinessProcessModeling`, 6.10 `UseCaseModeling`, 6.11 `DataRequirements`
- [x] Carrier Admission (Section 5) updated: убраны F.18 и E.19 из NotCaptured

### Completed (Third Pass)

- [x] Thin‑affordance: anti-patterns 3→2, conformance checklists 6→4 на всех 12 картах
- [x] Positive worked slices: конкретные примеры успешного применения для всех 12 ProblemCard
- [x] Mature Comparator Reference: mapping на BABOK/IREB для всех 12 карт (заменён на Mature Comparator Parity в Fourth Pass)
- [x] Worked examples для 4 новых карт (6.9–6.12): anti-patterns + checklists + positive/negative cases
- [x] Per‑card E.21 compact evaluation (5 координат × 12 карт = 60 оценок)
- [x] Framework-level E.21 delta updated: second→third pass comparison

### Pending Work (Fifth Pass)

- Full 19‑coordinate per‑card E.21 (сейчас compact 5‑coordinate)
- Heterogeneous transfer cases: демонстрация применения ProblemCard в разных отраслях (fintech, healthcare, gov, telecom) для всех 12 карт
- Quantified measures для CharacterizationRelation (где применимо)
- Проверка на conformance с актуальной версией FPF Core после стабилизации имён паттернов
- Решение проблем E.19: 4 карты repairBeforeUse (6.9–6.12), UseAffordability на координате 2
