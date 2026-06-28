# BAR.RequirementValidation: Валидация требований

> **Trigger:** На демо стейкхолдер говорит «это не то, что я имел в виду»; разработка обнаруживает нереализуемое ограничение через месяц
> **Governing patterns:** 
>   → `../fpf-core/references/A.7-strict-distinction.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/C.24-safe-probe.md`
>   → `../fpf-core/references/A.21-gate-decision.md`
>   → `../fpf-core/references/C.16-coverage.md`
>   → `../fpf-core/references/C.25-q-bundle.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда потратила спринт на реализацию требования, а на демо стейкхолдер говорит: «это не то, что я имел в виду»; требование задокументировано, но не проверено на выполнимость — разработка обнаруживает нереализуемое ограничение через месяц; тестировщик не может написать test case, потому что acceptance criteria не тестируемы |
| **ContextGrounding** | Фаза validation: проверка требований на корректность, полноту, выполнимость и тестируемость до передачи в разработку |
| **ScopeCut** | Валидация требований (правильные ли требования?) — в отличие от верификации (правильно ли реализованы требования?); не охватывает приёмочное тестирование |
| **NotWishReason** | «Мы записали требования со слов заказчика, значит, они правильные» — отказ от валидации под видом «заказчик всегда прав» |

## Conditional Fields

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

## Worked Examples

**Positive Worked Slice:** Международная логистическая компания интегрирует систему с таможенным API перевозчика. Требование: «растаможивание груза в реальном времени с откликом ≤ 5 секунд». Бизнес-аналитик настаивает на feasibility spike до фиксации требования в бэклоге. Архитектор строит тонкий прототип за 2 дня и обнаруживает: под нагрузкой таможенный API отвечает 12–18 секунд — требование физически недостижимо с текущим вендором. Бизнес-аналитик пересогласовывает требование: «асинхронное растаможивание с уведомлением в течение 5 секунд после ответа API». Три месяца wasted development на тупиковую интеграцию предотвращены; стейкхолдер signed off пересмотренное требование с измеримыми acceptance criteria.

**Near-Miss Example:** Стейкхолдер на демо rejected функциональность — ожидал локального сохранения, а система отправляла на сервер. Acceptance criteria были signed off, feasibility проверен, test cases написаны. Проблема не в validation — скрытое ожидание не было выявлено при elicitation. Паттерн валидации применим, но не защищает от требований, отсутствующих в спецификации.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Валидация = демо прототипа** | Команда показывает прототип; стейкхолдер: «выглядит хорошо»; требование считается валидированным — acceptance criteria не проверены, feasibility не оценён | Подменяет structured validation на UX-показ. Паттерн требует проверки problem statement + testability + consistency, а не approval wireframe |
| **Валидация без разработчика** | Аналитик и стейкхолдер согласовали требование; через 2 недели разработчик: «невыполнимо на текущем стеке» | Нарушает MandatoryConstraint об участии implementer role. Feasibility без того, кто будет реализовывать — гадание |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.VAL-1` | Acceptance criteria signed off стейкхолдером с подтверждением «критерии описывают мою потребность» | Предотвращает «это не то, что я имел в виду» |
| `CC-BAR.VAL-2` | Feasibility check пройден — разработчик/архитектор подтвердил реализуемость; при высоком риске — architecture spike | Предотвращает обнаружение нереализуемых требований через недели разработки |
| `CC-BAR.VAL-3` | Test-case derivation выполнен — тестировщик написал test case без дополнительных разъяснений | Предотвращает «нетестируемые» требования |
| `CC-BAR.VAL-4` | В валидации участвовал implementer role (разработчик или архитектор) | Предотвращает «валидацию без разработчика» |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 5 (Requirements Life Cycle Management) — Validate Requirements | Проверка требований на alignment с потребностями стейкхолдера, feasibility, testability, consistency до передачи в разработку | **Adopted** — AcceptanceCriterion требует signed-off acceptance criteria + feasibility check + test-case derivation | **Extended:** BABOK описывает validation как activity аналитика; BAPF добавляет mandatory участие implementer role (разработчик/архитектор) — «Валидация без разработчика» как anti-pattern. BABOK validation — stakeholder-side, BAPF добавляет implementer-side check |
| IREB CPRE FL, ch. 8 (Requirements Validation) | Различение validation (правильные ли требования?) и verification (правильно ли реализовано?); критерии качества для validation | **Adopted** — ScopeCut фиксирует strict distinction validation vs verification; AcceptanceCriterion operationalizes quality criteria | Добавлен anti-pattern «Валидация = демо прототипа» и explicit unknown-handling tactic (safe-probe-needed → architecture spike). IREB определяет validation концептуально, BAPF даёт misuse detection и тактику работы с неизвестным |
| Pohl, 2010, ch. 3 (Validation vs Verification) | Boehm (1981) различение: validation = «are we building the right system?», verification = «are we building the system right?» | **Adopted as-is** — strict distinction в ScopeCut и governing-pattern cues восходит к Boehm/Pohl | **Adopted as-is; BAPF operationalization adds conformance checklist but no novel practice.** Значение — встраивание академического различения в operational framework с gate decision и freshness condition |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Различение validation (строим правильную систему?) и verification (правильно строим?) | `A.7` (Strict Distinction) |
| Acceptance criteria как acceptance probe | `C.22.2` |
| Feasibility check как risk condition | `C.24` (safe probe) |
| Stakeholder sign-off как gate decision | `A.21` |
| Test-case derivation как проверка testability | `C.16` |
| Конфликт требований как inconsistency в Q-bundle | `C.25` |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L523-L593
