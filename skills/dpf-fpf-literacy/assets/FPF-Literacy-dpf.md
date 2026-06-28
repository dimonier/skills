# Domain Principle Framework: FPF-грамотность и создание DPF для AI-ассистируемой инженерной работы

> **Pattern family:** `E.4.DPF` (Domain Principle Framework Authoring)
> **Status:** Draft — First-hour route, создан по материалам практикума «Предметный учебник для AI-агента за 90 минут» (Левенчук, 28 июня 2026)
> **Normativity:** Локально-нормативный для практики AI-ассистируемой инженерно-менеджериальной работы
> **Depends on:** `FPFCorePatternSet@current`

---

## 1. Context Declaration

| Поле | Значение |
|---|---|
| **BoundedContext** | `FPF-грамотность@AI-ассистируемаяИнженернаяРабота` |
| **IntendedReader** | Инженер-менеджер, технический лид, системный инженер, researcher — использующий AI-агентов в проектной работе |
| **FirstUse** | Постановка задачи AI-агенту до получения «красивого, но бесполезного» ответа; создание черновика DPF для своей предметной области |

### Non‑Use Boundary

- Не заменяет FPF Core — использует его как governing-pattern host (`E.4.DPF`)
- Не является руководством по конкретным AI-инструментам (ChatGPT, Claude, Codex) — это уровень компьютерной грамотности пользователя
- Не охватывает создание LPF (local practices framework) — это следующий уровень конкретизации под организацию/проект
- Не является учебником по системной инженерии или менеджменту — для этого существуют отдельные DPF

---

## 2. Source Pack (`G.2`)

### Adopted Sources

| Источник | Роль в фреймворке |
|---|---|
| **FPF Core Specification** (Levenchuk, June 2026, github.com/ailev/FPF) | Host framework: все governing-pattern cues ссылаются на FPF Core |
| **Практикум «Предметный учебник для AI-агента за 90 минут»** (Левенчук, 28.06.2026) | Первичный source сигналов проблем, контекста и SoTA-ходов |
| **Christopher Alexander et al.** *A Pattern Language* (1977) | Источник концепции языков паттернов как формата публикации принципов |
| **Niels Bohr** (цитата) | «Профессионал — это тот, кто не делает новичковых ошибок» — grounding для роли DPF |
| **Парижская академия наук** (1775, запрет вечных двигателей) | Исторический пример move exclusion через принцип (закон сохранения энергии) |

### Rejected Sources

- Литература по prompt engineering как самодостаточной дисциплине — входит в bounded context только как носитель контекста, не как метод
- «Попсовые» подходы к AI (астрология, аристотелевская логика как универсальный метод) — явно исключены как non-admissible основания

> **ClaimStatus:** `provisional` — required payload extraction per `G.2` discipline before pattern body freeze.

---

## 3. Architecture Decision (`E.4.PFAD`)

**`PFAD-FPFLIT-001`**

| Слот | Значение |
|---|---|
| **FrameworkFamily** | `DomainPrincipleFramework` |
| **Purpose** | Дать инженерные паттерны для осмысленной постановки задач AI-агенту с опорой на FPF и для создания черновиков DPF в своей предметной области |

### First Pattern Set

1. **`FPFLIT.VanillaVsFPF`** — Различение ответов AI-агента без опоры на принципы и с опорой на FPF
2. **`FPFLIT.FrameworkEcosystemPlacement`** — Размещение рабочей ситуации на уровне FPPS/FPF/DPF/LPF
3. **`FPFLIT.PrincipleAsMoveExclusion`** — Использование принципов как паттернов отсечения негодных ходов
4. **`FPFLIT.FirstHourDPFRoute`** — Создание черновика DPF за первый час (first-hour route)
5. **`FPFLIT.AgentContextLoad`** — Загрузка предметного знания AI-агенту через FPF+DPF
6. **`FPFLIT.DPFImprovementCycle`** — Цикл улучшения черновика DPF до рабочего состояния
7. **`FPFLIT.SoTARecognition`** — Распознавание SoTA-решения в проблемной ситуации vs «попсовый» ответ
8. **`FPFLIT.CarrierFirstEntry`** — Выбор носителя (файл vs чат) для первой публикации DPF

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
| **PrimaryName** | Принциповый фреймворк FPF-грамотности и DPF-авторинга |
| **PublicLabel** | `FPFLiteracyPrincipleFramework` |
| **ProvisionalAlias** | `FPFLitPF` |
| **F18NameCard** | Требуется до заморозки публичного сокращения |
| **NameScope** | Bounded context практики AI-ассистируемой инженерно-менеджериальной работы с опорой на FPF |

---

## 5. Carrier Admission (`C.33`)

| Слот | Содержание |
|---|---|
| **CapturedStructure** | Контекстная декларация, source pack, архитектурное решение; восемь `ProblemCard@Context` |
| **NotCaptured** | Полные паттерные тела `E.8` с worked slices, anti-patterns, conformance checklists; relation records `E.4.PFR`; quality evaluation `E.21`; SoTA-Echoing таблицы с точными references |
| **AdmissibleUse** | P2W-ready problem-side input для практики постановки задач AI-агенту через FPF; drafting aid для создания DPF своей предметной области |
| **NonAdmissibleUse** | Готовый «регламент» для AI-агента без адаптации под конкретную предметную область; замена изучения FPF Core |

---

## 6. Problem Cards (`C.22.2`)

### 6.1 `FPFLIT.VanillaVsFPF` — Различение ответов AI с опорой на принципы и без

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | AI-агент на запрос «помоги улучшить этот документ» выдаёт косметическую правку стиля, общую структуру и уверенные рекомендации — не спрашивая, какое решение должен поддержать документ |
| **ContextGrounding** | Инженер-менеджер использует AI-агента для рабочих задач в проекте; задача не тривиальна и требует не «красивого ответа», а работающего решения |
| **ScopeCut** | Различение типа ответа агента (FPF-опосредованный vs vanilla); не охватывает сравнение разных AI-моделей |
| **NotWishReason** | «Сделай мне красиво» — это ожидание чуда, а не рабочая постановка задачи |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **EntityOfConcern** | Ответ AI-агента как эпистемический артефакт — его структура, обоснованность, пригодность для дальнейшей работы |
| **SymptomDetection** | Агент сглаживает стиль, добавляет общую структуру, пишет уверенные рекомендации; не спрашивает о problem context, не указывает на evidence gaps, не предлагает rejected alternatives |
| **ProblemHypothesis** | Без загрузки принципов (FPF) агент работает в режиме «вероятностной стрельбы по площадям» — выбирает наиболее вероятный, а не наиболее правильный для данной инженерной ситуации ход |
| **ImprovementCheck** | После загрузки FPF агент перестаёт делать косметику вместо работы, обращает внимание на действительно важное, отсекает неважное, указывает на problem-side record до предложения решения |
| **AcceptanceCriterion** | Ответ агента содержит: (1) identification problem context, (2) separation of problem and solution, (3) explicit alternatives with rejected reasons, (4) governing-pattern cues, (5) что остаётся непроверенным |
| **MandatoryConstraints** | Запрещено принимать ответ агента без FPF-контекста за working solution; запрещено использовать «красивый ответ» как decision basis |
| **CharacterizationRelation** | Problem-side fidelity, solution-side SoTA alignment, evidence explicitness, readability for intended reader |
| **ValidationBoundary** | Проверка на трёх типовых запросах (выбор имени, предложение архитектуры, «что делать») — с FPF и без |
| **FreshnessOrExpiry** | `stale` при смене версии FPF Core или модели AI-агента |
| **ProblemFormulationFollowUpReason** | Исключить «машинную попсовую интуицию» из рабочих процессов до того, как она породит дорогие ошибки |
| **ReadinessDisposition** | `P2W-ready` для выбора способа постановки задачи агенту |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Problem identification до решения | `C.22.2` |
| Различение description и described thing | `E.17` |
| Evidence gap explicit | `A.10` |
| Intended reader и publication form | `E.17.EFP` |

---

### 6.2 `FPFLIT.FrameworkEcosystemPlacement` — Размещение ситуации на уровне FPPS/FPF/DPF/LPF

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда не различает, на каком уровне абстракции находится проблема: путает общий принцип работы (FPF), предметное знание (DPF) и локальный регламент (LPF); пытается решить всё одним «универсальным» промптом |
| **ContextGrounding** | Проект использует AI-агентов в коллективной работе; разные участники имеют разные роли, разную предметную экспертизу и разные локальные ограничения |
| **ScopeCut** | Классификация проблемной ситуации по уровням экосистемы FPF; не охватывает детальное проектирование каждого уровня |
| **NotWishReason** | «Давайте загрузим агенту всё сразу» —坍塌 уровней без различения их роли |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Агент даёт ответ уровня «надо мыть руки» (DPF), когда нужен ответ уровня «в нашей клинике руки моют в операционной №3 средством X» (LPF) — или наоборот |
| **EntityOfConcern** | Уровень абстракции в экосистеме фреймворков: FPPS (нулевые принципы — онтологика, семиотика, эпистемология), FPF (первые принципы — работа, роли, методы, агенты, обещания), DPF (вторые принципы — предметные SoTA-ходы), LPF (локальные практики — регламенты организации/проекта) |
| **SymptomDetection** | Ответ агента либо слишком общий (не учитывает предметную специфику), либо слишком конкретный (не учитывает, что ситуация повторяется в разных предметных областях) |
| **ProblemHypothesis** | Команда не провела явное размещение проблемной ситуации на уровнях FPPS→FPF→DPF→LPF — агент получает неполный или избыточный контекст |
| **ImprovementCheck** | Для каждой задачи явно определено: что из FPF (общие принципы работы), что из DPF (предметные правила), что из LPF (локальные регламенты) |
| **AcceptanceCriterion** | Для каждой рабочей ситуации назван целевой уровень и зависимые уровни; агент получает контекст соответствующей гранулярности |
| **MandatoryConstraints** | Запрещено пропускать уровень FPF (первые принципы) при построении DPF — DPF всегда depends on FPF Core |
| **CharacterizationRelation** | Scope абстракции (широта применимости), specificity (конкретность хода), dependency chain (на какие уровни опирается) |
| **ValidationBoundary** | Проверка классификации на ≥3 типовых рабочих ситуациях из разных фаз проекта |
| **FreshnessOrExpiry** | `stale` при изменении архитектуры экосистемы FPF (новые уровни, новые отношения между уровнями) |
| **ProblemFormulationFollowUpReason** | Предотвратить坍塌 уровней — основную причину нерелевантных ответов агента |
| **ReadinessDisposition** | `P2W-ready` для выбора уровня контекста при постановке задачи агенту |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Холон и его уровни | `B.2` |
| Bounded context и его границы | `C.11` |
| Framework dependency declaration | `E.4.PFAD` |
| Scope cut для problem formulation | `C.22.2` |

---

### 6.3 `FPFLIT.PrincipleAsMoveExclusion` — Принцип как паттерн отсечения негодных ходов

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда рассматривает «100500 способов сделать что-то не так» на один-два годных; время тратится на анализ заведомо неработающих вариантов |
| **ContextGrounding** | Инженерная/исследовательская работа, где пространство возможных ходов велико, а обратная связь медленная, дорогая или шумная |
| **ScopeCut** | Применение принципа как move exclusion filter на дальних подступах — до тонкой предметной экспертизы |
| **NotWishReason** | «Давайте рассмотрим все варианты» — без предварительного отсечения заведомо невозможных ходов |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Парижская академия наук (1775): запрет рассмотрения проектов вечных двигателей на основе принципа сохранения энергии. Современные патентные ведомства воспроизводят это правило |
| **EntityOfConcern** | Принцип как паттерн: декларативно (акаузально) представленный метод работы, содержащий Problem frame, Solution (SoTA-ход), Forces, Examples, Anti-patterns, и Governing-pattern cues |
| **SymptomDetection** | Эксперты тратят время на обсуждение вариантов, которые нарушают известные принципы; агент предлагает «красивые» решения, несовместимые с FPF/DPF |
| **ProblemHypothesis** | Принципы не сформулированы явно как move exclusion rules — команда полагается на интуицию, а не на явные паттерны отсечения |
| **ImprovementCheck** | Время до отбрасывания негодного хода сокращается; экспертиза направляется на сравнение admissible вариантов, а не на отсев non-admissible |
| **AcceptanceCriterion** | Принцип содержит: (1) problem frame (в какой ситуации), (2) forces (почему трудно), (3) solution (SoTA-ход), (4) anti-patterns (что нельзя делать), (5) near-miss examples (похоже, но неправильно), (6) governing-pattern cues |
| **MandatoryConstraints** | Принцип не является инструкцией-рецептом; принцип не может быть сведён только к «problem → solution» без остальных секций |
| **CharacterizationRelation** | Move exclusion power (сколько ходов отсекает), false-positive risk (отсекает ли годные ходы), domain coverage (в каких ситуациях применим) |
| **ValidationBoundary** | Проверка на ≥3 исторических примерах, где отсутствие принципа привело к ошибке |
| **FreshnessOrExpiry** | `stale` при появлении нового физического эффекта, научной теории или инженерной практики, меняющей границы применимости |
| **ProblemFormulationFollowUpReason** | Встроить move exclusion в процесс принятия решений до инвестиций в детальный анализ |
| **ReadinessDisposition** | `P2W-ready` для применения как фильтра при рассмотрении вариантов |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Pattern body structure (Problem, Solution, Forces, etc.) | `E.8` |
| Anti-pattern и near-miss specification | `E.8` (anti-pattern section) |
| SoTA-echoing — ссылка на литературу | `G.2` |
| Принцип как admissible move | `A.21` (gate) |

---

### 6.4 `FPFLIT.FirstHourDPFRoute` — Маршрут создания черновика DPF за первый час

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда хочет дать AI-агенту предметное знание, но не знает, с чего начать; попытки «загрузить всё» приводят к неструктурированному контексту, который агент не может эффективно использовать |
| **ContextGrounding** | Инженер-менеджер имеет доступ к AI-агенту, файлу FPF Core и знаниям о своей предметной области; нужно за ограниченное время (≈90 минут) получить первый рабочий черновик DPF |
| **ScopeCut** | First-hour route: создание файла-черновика DPF по spine E.4.DPF; не охватывает полный цикл улучшений до industrial-grade DPF |
| **NotWishReason** | «Сделай мне DPF по моей области» одним промптом без последующего чтения и правок |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Материалы практикума 28.06.2026: демонстрация создания DPF за 90 минут с вариантами задания предметной области |
| **EntityOfConcern** | Файл DPF как first-entry carrier — маркдаун-документ, содержащий spine: context → source pack → PFAD → names → patterns → relations → quality → refresh |
| **SymptomDetection** | Агент без структуры DPF выдаёт красивый текст «обо всём», но без problem cards, без explicit scope cuts, без mandatory constraints, без governing-pattern cues |
| **ProblemHypothesis** | Команда не использует structured spine E.4.DPF — агент получает задачу «напиши учебник», а не «создай DPF по спецификации E.4.DPF» |
| **ImprovementCheck** | Черновик DPF содержит: context declaration, source pack, PFAD, names, ≥3 problem cards с always-core и conditional fields, relation rows, carrier admission, quality route, refresh route |
| **AcceptanceCriterion** | Файл DPF читается как единый документ; каждая problem card имеет ProblemSignal, ContextGrounding, ScopeCut, NotWishReason и AcceptanceCriterion; все governing-pattern cues ссылаются на FPF Core |
| **MandatoryConstraints** | DPF всегда в файле (не в чате) — это снимает ограничения на размер и позволяет циклы улучшений; DPF всегда depends on FPF Core; запрещён Core landing (DPF не модифицирует FPF Core) |
| **CharacterizationRelation** | Completeness (все ли секции spine заполнены), specificity (насколько ходы предметно-специфичны), usability (может ли агент использовать как контекст) |
| **ValidationBoundary** | Проверка: агент с загруженным DPF даёт предметно-релевантный ответ на ≥3 типовых вопроса из bounded context |
| **FreshnessOrExpiry** | `stale` при изменении FPF Core edition или появлении новых SoTA-источников в предметной области |
| **ProblemFormulationFollowUpReason** | Создать структурированный носитель предметного знания, который можно улучшать итеративно |
| **ReadinessDisposition** | `P2W-ready` как drafting aid для первого часа работы |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| DPF authoring spine | `E.4.DPF` |
| Problem card structure | `C.22.2` |
| Framework architecture decision | `E.4.PFAD` |
| Carrier selection для публикации | `C.33` |
| Source pack formation | `G.2` |

---

### 6.5 `FPFLIT.AgentContextLoad` — Загрузка предметного знания AI-агенту

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | AI-агент даёт «беззубые» ответы — вероятностно «стреляет по площадям», не знает, что в данной предметной области считается сильным ходом, а что — недопустимой ошибкой |
| **ContextGrounding** | Инженер-менеджер работает с AI-агентом в контексте конкретной предметной области; агент имеет доступ к «всему интернету», но не знает, какие из множества подходов являются SoTA для данной области |
| **ScopeCut** | Загрузка FPF + DPF как контекста для агента; не охватывает тонкую настройку модели (fine-tuning) |
| **NotWishReason** | «Агент сам разберётся, он же умный» — игнорирование того, что «в интернете» хорошим мышлением считается и астрология, и аристотелевская логика, и промпт-инженерия вперемешку |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Практикум: агент с FPF принципиально меняет характер ответов — от «попсовых» к инженерно-обоснованным; без FPF агент склонен «понравиться», а не решить задачу |
| **EntityOfConcern** | Контекст AI-агента — многоуровневая память: FPF (уровень надёжности решения в коллективной работе), DPF (уровень знаний предметной области), LPF (уровень организации) |
| **SymptomDetection** | Агент предлагает решения, которые «верны для других, но неверны для вас»; агент использует подходы, признанные устаревшими или ошибочными в данной предметной области |
| **ProblemHypothesis** | Агент не получил явных границ допустимого — он не знает, что вы не астролог и не маркетолог, которому нужно «настроение», а не точность |
| **ImprovementCheck** | После загрузки FPF+DPF агент: (1) отсекает non-admissible ходы, (2) указывает на SoTA-решения, (3) предупреждает о типовых ошибках, (4) спрашивает о локальных ограничениях (LPF), а не сочиняет уверенные рекомендации |
| **AcceptanceCriterion** | Агент использует FPF-паттерны как governing patterns; агент ссылается на DPF problem cards при обосновании хода; агент различает, что решено на уровне DPF, а что требует локального решения (LPF) |
| **MandatoryConstraints** | Запрещено давать агенту DPF без FPF — DPF всегда depends on FPF Core; запрещено заменять чтение DPF человеком на «пусть агент сам читает» без понимания человеком содержания DPF |
| **CharacterizationRelation** | Response specificity (насколько ответ предметно-специфичен), SoTA alignment (соответствие принятым в области решениям), error prevention (предупреждение типовых ошибок) |
| **ValidationBoundary** | A/B тест: один и тот же вопрос агенту без DPF и с DPF — сравнение ответов по characterization criteria |
| **FreshnessOrExpiry** | `stale` при обновлении DPF или смене модели агента |
| **ProblemFormulationFollowUpReason** | Принципиально ограничить агента — из «умного попсовика» сделать инженера, знающего правила предметной области |
| **ReadinessDisposition** | `P2W-ready` для загрузки контекста перед постановкой задачи |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Bounded context и его границы | `C.11` |
| Agent role и responsibility | `E.16` |
| Context engineering levels | `E.4` (framework ecosystem) |
| Intended reader specification | `E.17.EFP` |

---

### 6.6 `FPFLIT.DPFImprovementCycle` — Цикл улучшения черновика DPF

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Черновик DPF полезен, но недостаточно надёжен для ответственной опоры: в нём мало источников SoTA, нет антипаттернов, не проверены границы применимости, отсутствуют связи между паттернами |
| **ContextGrounding** | Команда имеет first-hour DPF и хочет довести его до состояния, пригодного для регулярного использования в проекте |
| **ScopeCut** | Цикл улучшения DPF как артефакта; не охватывает создание нового DPF с нуля |
| **NotWishReason** | «Прокрути цикл улучшений» агенту без задания evaluation characteristics — агент выдаст красивый список идей, но не улучшит DPF |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | FPF содержит встроенные паттерны улучшения: `E.22` (framing evaluation purpose), `E.21` (pattern-quality evaluation), `E.23` (improvement loop), `E.19` (admission review) |
| **EntityOfConcern** | DPF как улучшаемый артефакт — его характеристики качества и процесс улучшения |
| **SymptomDetection** | Попытка улучшить DPF без evaluation characteristics приводит к «улучшению ради улучшения» — агент меняет формулировки, но не устраняет структурные дефекты |
| **ProblemHypothesis** | Команда не задала характеристики для оценки DPF — нельзя улучшать то, что не умеешь измерять |
| **ImprovementCheck** | Каждый цикл улучшения: (1) заданы evaluation characteristics, (2) проведена оценка текущего состояния, (3) выбран конкретный аспект для улучшения, (4) выполнено улучшение, (5) проверен результат |
| **AcceptanceCriterion** | DPF проходит `E.21` evaluation с acceptable scores; отдельный reviewer (не автор) подтверждает улучшение; refresh route актуален |
| **MandatoryConstraints** | Улучшать можно только что-то конкретное и по явно заданным характеристикам; нужен отдельный оценщик (reviewer) и отдельный разработчик — «сам себя не проверишь»; цикл требует указания целевого уровня («до пятёрочек» или «на троечки») |
| **CharacterizationRelation** | Discoverability, source fidelity, ontology clarity, thin affordance, refreshability — из `E.4.DA` и `E.21` |
| **ValidationBoundary** | Как минимум два прохода цикла улучшения с разными reviewer |
| **FreshnessOrExpiry** | Цикл возобновляется при изменении FPF Core, появлении новых SoTA-источников, или обнаружении misuse patterns |
| **ProblemFormulationFollowUpReason** | Превратить «красивый черновик» в рабочий инструмент, на который можно опираться в проекте |
| **ReadinessDisposition** | `P2W-ready` когда evaluation characteristics заданы, а reviewer назначен |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Evaluation characteristics definition | `A.19.ECS` |
| Framing evaluation purpose | `E.22` |
| Pattern quality evaluation | `E.21` |
| Improvement loop execution | `E.23` |
| Admission review gate | `E.19` |
| Reviewer/author separation | `E.16` (agent roles) |
| Quality route для DPF | `E.4.DA` |

---

### 6.7 `FPFLIT.SoTARecognition` — Распознавание SoTA-решения в проблемной ситуации

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Агент предлагает решение, которое выглядит разумным, но не является SoTA в предметной области — либо устарело, либо применимо в другой области, либо просто «попсовое» |
| **ContextGrounding** | Инженер-менеджер формулирует проблему в предметной области, но не может самостоятельно отличить SoTA-ход от красивого, но неработающего |
| **ScopeCut** | Идентификация SoTA-решения для проблемной ситуации через FPF+DPF; не охватывает создание нового SoTA (исследование) |
| **NotWishReason** | «Агент предложил — значит, это работает» — слепое доверие к output агента без проверки на SoTA |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | FPF-паттерн: «Принцип указывает на то место, которое в известной проблемной ситуации прошло принципиальные проверки и указывает на SoTA-решение проблемы» |
| **EntityOfConcern** | SoTA-ход (state-of-the-art move) — наилучший из известных методов решения проблемы в данном контексте, подтверждённый источниками |
| **SymptomDetection** | Агент предлагает решение без ссылок на источники; решение противоречит known principles; решение «работает в теории», но не имеет evidence реализации |
| **ProblemHypothesis** | Агент не различает «часто упоминаемое в интернете» и «подтверждённое SoTA» — он оптимизирует вероятность, а не инженерную обоснованность |
| **ImprovementCheck** | Каждое предложенное решение имеет: (1) ссылку на SoTA-источник, (2) указание problem frame, в котором оно является SoTA, (3) границы применимости, (4) known limitations |
| **AcceptanceCriterion** | SoTA-echoing: для каждого решения указан источник (литература, стандарт, авторитетная практика); решение размечено по problem frame из DPF |
| **MandatoryConstraints** | Запрещено принимать решение как SoTA без source reference; «общее знание» агента не является evidence SoTA |
| **CharacterizationRelation** | Source authority (уровень источника), evidence strength (теория vs практика vs испытания), domain specificity (насколько решение предметно-специфично) |
| **ValidationBoundary** | Проверка: эксперт предметной области подтверждает, что предложенное решение действительно является SoTA для данного problem frame |
| **FreshnessOrExpiry** | `stale` при появлении новых SoTA-источников или опровержении текущих |
| **ProblemFormulationFollowUpReason** | Отделить инженерно-обоснованные решения от «попсовых» — не дать агенту ввести команду в заблуждение красивой формой без содержания |
| **ReadinessDisposition** | `P2W-ready` для проверки ответов агента на SoTA-соответствие |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| SoTA-echoing и source reference | `G.2` |
| Problem card как frame для SoTA | `C.22.2` |
| Evidence и assurance для claim | `A.10`, `B.3` |
| Comparison frame для альтернатив | `G.0`, `G.9` |
| Refresh при устаревании | `G.11` |

---

### 6.8 `FPFLIT.CarrierFirstEntry` — Выбор носителя для первой публикации DPF

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда пытается создать DPF в чате с агентом — вывод обрезается, структура теряется, невозможно вернуться к предыдущей версии и править |
| **ContextGrounding** | Создание первого DPF с AI-агентом; нужно сохранить результат для последующего чтения, обсуждения и циклов улучшения |
| **ScopeCut** | Выбор формата и носителя для first-entry carrier DPF; не охватывает долгосрочное управление версиями и публикациями |
| **NotWishReason** | «Напиши мне DPF» в чат — вывод обрезается, агент пишет «нрзбрчво» (сокращённо), структура теряется |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Правило практикума: «В файле — это важно, это снимает ограничения на размер, а ещё — можно потом править-улучшать» |
| **EntityOfConcern** | First-entry carrier — файл (markdown), содержащий полный текст DPF как локальный монолит с извлекаемыми секциями |
| **SymptomDetection** | Ответ агента в чат обрезан; структура DPF неполна; невозможно отличить, где кончается ответ агента и начинаются следующие сообщения |
| **ProblemHypothesis** | Чат как carrier не подходит для structured artifacts размером больше нескольких абзацев — он оптимизирован для диалога, а не для документов |
| **ImprovementCheck** | DPF сохранён как файл; файл можно открыть, прочитать полностью, отредактировать, передать другому агенту, загрузить в новую сессию |
| **AcceptanceCriterion** | DPF — markdown-файл; содержит все секции spine; может быть загружен агенту как контекст; может быть отредактирован человеком или агентом по запросу «отредактируй файл» |
| **MandatoryConstraints** | Первая публикация DPF — всегда в файл, не в чат; файл должен быть в формате, допускающем редактирование (markdown, не PDF); файл должен содержать explicit version/status |
| **CharacterizationRelation** | Completeness (полнота содержания), editability (возможность правок), portability (переносимость между сессиями/агентами), shareability (возможность передачи коллегам) |
| **ValidationBoundary** | Проверка: агент может прочитать файл DPF и использовать его как контекст для ответа на предметный вопрос |
| **FreshnessOrExpiry** | `stale` при структурных изменениях DPF, требующих новой публикации |
| **ProblemFormulationFollowUpReason** | Выбрать правильный carrier до начала работы — иначе результат будет потерян или неполон |
| **ReadinessDisposition** | `P2W-ready` для выбора носителя перед созданием DPF |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Carrier admission criteria | `C.33` |
| Publication unit и scope | `E.17.EFP` |
| First-entry carrier для framework | `E.4.DPF` |
| Relation records carrier | `E.4.PFR` |

---

## 7. Relation Records (`E.4.PFR` stub)

### Relation Map

| Source | Target | Relation Function |
|---|---|---|
| `FPFLIT.VanillaVsFPF` | `FPFLIT.AgentContextLoad` | Различение типов ответов — предпосылка для правильной загрузки контекста |
| `FPFLIT.FrameworkEcosystemPlacement` | `FPFLIT.AgentContextLoad` | Уровень экосистемы определяет, какой контекст загружать агенту |
| `FPFLIT.PrincipleAsMoveExclusion` | `FPFLIT.SoTARecognition` | Принцип как move exclusion — механизм отличения SoTA от не-SoTA |
| `FPFLIT.FirstHourDPFRoute` | `FPFLIT.CarrierFirstEntry` | Маршрут создания DPF предписывает выбор файла как carrier |
| `FPFLIT.FirstHourDPFRoute` | `FPFLIT.DPFImprovementCycle` | First-hour DPF — вход для цикла улучшений |
| `FPFLIT.AgentContextLoad` | `FPFLIT.SoTARecognition` | Загрузка контекста — условие для распознавания агентом SoTA-решений |
| `FPFLIT.DPFImprovementCycle` | → *all pattern cards* | Цикл улучшения применим к каждой problem card DPF |

### Edition Dependency

| Слот | Значение |
|---|---|
| **FrameworkEditionRef** | `FPFLiteracyPrincipleFramework@Draft` |
| **DependsOnEditionRefs** | `FPFCorePatternSet@current` |
| **DependencyReason** | Все governing‑pattern cues ссылаются на FPF Core |
| **CompatibilityBoundary** | При изменении `E.4.DPF`, `C.22.2`, `E.8`, `G.2`, `E.21`, `E.23` — пересмотреть ProblemCard‑поля |
| **E53ConformanceNote** | Требуется проверка после стабилизации имён паттернов |

---

## 8. Publication

| Слот | Значение |
|---|---|
| **ThisFile** | Локальный монолит первого входа |
| **PublicationScope** | Engineering team, инженеры-менеджеры, технические лиды, резиденты программ рабочего развития |
| **FirstEntryCarrier** | `FPF-Literacy-dpf.md` — читается как единый документ |
| **RelationRecordsCarrier** | Секция 7; подлежит извлечению в отдельный PFR‑файл при росте |
| **NonPublicationNote** | `FPF-Spec.md` не модифицируется; Core не расширяется |

---

## 9. Quality Route

### Evaluation Characteristics

| Характеристика | Вопрос |
|---|---|
| **Discoverability** | Может ли инженер-менеджер найти нужный ProblemCard за `≤2 минуты`? |
| **WorkshopFidelity** | Восстановимы ли идеи практикума 28.06.2026 в problem signals и acceptance criteria? |
| **OntologyClarity** | Разделены ли problem‑side record, решение и work planning? Различимы ли уровни FPPS/FPF/DPF/LPF? |
| **ThinAffordance** | Каждый ProblemCard читается за `≤5 минут` экспертом? |
| **Refreshability** | Видны ли explicit stale/refresh условия для каждого ProblemCard? |
| **AgentUsability** | Может ли AI-агент использовать DPF как контекст для предметно-релевантных ответов? |

### Quality Framework

| Шаг | Владелец | Назначение |
|---|---|---|
| 1 | `E.22` | Framing evaluation purpose |
| 2 | `E.21` | Pattern‑quality evaluation каждого ProblemCard |
| 3 | `E.23` | Improvement loop — добавление worked slices, anti‑patterns, SoTA‑Echoing |
| 4* | `E.19` | Admission review (при росте фреймворка) |

---

## 10. Currentness Route (`G.11`)

### Refresh Triggers

- Изменение FPF Core edition (особенно `E.4.DPF`, `C.22.2`, `E.8`, `G.2`)
- Проведение новых семинаров/практикумов по FPF, добавляющих материал в bounded context
- Adoption telemetry: повторяющиеся misuse patterns (использование DPF без FPF, попытка «улучшить всё сразу» без evaluation characteristics)
- Появление новых AI-моделей с качественно иными возможностями (требующими пересмотра agent context load pattern)
- Локальные инциденты: агент с загруженным DPF даёт нерелевантные ответы

### Stale Indicators

- Каждый ProblemCard содержит explicit freshness condition
- Ревизия всего фреймворка: ежегодно или при major Core edition change
- Deprecation: через `superseding` relation record при замене ProblemCard

### Ownership

| Роль | Владелец |
|---|---|
| **FrameworkEditionOwner** | Инженерно-методологическая функция организации/проекта |
| **SourcePackOwner** | Тот же |
| **RelationRecordsOwner** | Тот же |
| **RefreshPlanOwner** | Технический лид / ведущий методолог |

---

## Authorship Annotation

| Слот | Значение |
|---|---|
| **AuthorshipNote** | Создан как first‑hour route в соответствии с `E.4.DPF:4` по материалам практикума «Предметный учебник для AI-агента за 90 минут» (Левенчук, 28.06.2026) |
| **FPFCompliance** | Spine: context → source pack → PFAD → names → patterns → relations → quality → refresh; `C.22.2` ProblemCard@Context для каждого паттерна; governing‑pattern cues для всех out‑of‑scope claims; `C.33` carrier admission |

### Pending Work

- Полные `E.8` паттерные тела с worked slices, local anti‑patterns и near‑miss examples
- `E.4.PFR` полные записи отношений между паттернами (сейчас stub)
- `F.18` name card для публичного имени после апробации
- SoTA‑Echoing таблицы с exact source refs на Alexander, Bohr и другие указанные источники
- `E.21` evaluation scores первого драфта
- `E.23` improvement loop с adoption telemetry
- Включение материалов будущих семинаров серии (5 семинаров) как дополнительных источников
- Проверка на conformance с актуальной версией FPF Core после стабилизации имён паттернов
