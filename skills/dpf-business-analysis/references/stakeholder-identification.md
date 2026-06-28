# BAR.StakeholderIdentification: Идентификация стейкхолдеров и их concerns

> **Trigger:** Требования собираются только от одного-двух «громких» стейкхолдеров; упущенные выходят на приёмке с «это не то»
> **Governing patterns:** 
>   → `../fpf-core/references/A.2-role.md`
>   → `../fpf-core/references/A.2.1-role.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/C.11-bounded-context.md`
>   → `../fpf-core/references/C.16-coverage.md`
>   → `../fpf-core/references/G.9-selector.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Требования собираются только от одного-двух «громких» стейкхолдеров; упущенные стейкхолдеры выходят на этапе приёмки с «это не то, что нам нужно»; носители ключевых constraints (безопасник, эксплуатация, регулятор) не опрошены |
| **ContextGrounding** | Проект создания/модификации системы с `≥3` группами интересов: бизнес-пользователи, эксплуатация, безопасность, регулятор, интеграция со смежными системами |
| **ScopeCut** | Идентификация и классификация стейкхолдеров на старте работы с требованиями; не охватывает управление ожиданиями на всём жизненном цикле |
| **NotWishReason** | «Мы и так знаем всех заинтересованных» — без явного stakeholder map/onion model пропуск holders constraints необнаружим |

## Conditional Fields

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

## Worked Examples

**Positive Worked Slice:** В проекте внедрения ERP бизнес-аналитик на старте построил stakeholder onion model: 4 слоя (core team, direct users, constraint holders, external). Идентифицировал инженера эксплуатации ЦОД (constraint holder) и офицера ИБ — роли, которые заказчик не назвал при первых интервью. При попытке добавить серверный компонент эксплуатация указала: «физического места в стойке нет, расширение — через 6 месяцев». Ранняя идентификация предотвратила блокировку приёмки: перепроектирование заняло 1 день вместо 2 недель.

**Near-Miss Example:** Команда провела stakeholder workshop. Stakeholder map построен, concerns зафиксированы. Через месяц эксплуатация блокирует приёмку: система не влезает в дата-центр — constraint «10 000 пользователей» зафиксирован со слов бизнес-заказчика, но носитель constraint (инженер эксплуатации) не был идентифицирован как стейкхолдер. Это проблема разделения concern ownership, а не идентификации — применяется `BAR.RequirementValidation`.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Stakeholder proxy substitution** | Бизнес-аналитик опрашивает Product Owner как «представителя всех»; требования эксплуатации и безопасности записываются со слов PO | PO не является role-holder для constraint-bearing ролей. Паттерн требует прямой идентификации holder каждого concern |
| **Positive-stakeholder bias** | Stakeholder register содержит только «дружественных» стейкхолдеров; holders constraints (безопасник, DBA, compliance) пропущены — «они всё равно скажут нет» | MandatoryConstraints прямо запрещают ограничиваться позитивными стейкхолдерами |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.SIH-1` | Stakeholder register содержит: идентификатор, роль, concern(ы), канал коммуникации, полномочия по приёмке | Операционализирует AcceptanceCriterion |
| `CC-BAR.SIH-2` | Каждая функциональная область имеет ≥1 стейкхолдера-носителя требования и ≥1 стейкхолдера-носителя constraint | Coverage функциональных областей |
| `CC-BAR.SIH-3` | Holders constraints (безопасность, эксплуатация, регулятор) явно идентифицированы | Запрет ограничения позитивными стейкхолдерами |
| `CC-BAR.SIH-4` | Негативные стейкхолдеры идентифицированы; при ограниченном доступе зафиксирована причина | MandatoryConstraints: негативные обязательны |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 2 (Business Analysis Key Concepts) | Классификация стейкхолдеров: влияние × интерес, RACI — кто и с каким весом участвует в проекте | **Adopted** — ролевая классификация отражается в AcceptanceCriterion (владелец требований, владелец constraints, консультант, информируемый) | **Extended:** BABOK классифицирует по влиянию, BAPF добавляет constraint-holder dimension (носитель constraints обязателен независимо от политического веса). Операционализация: CC-BAR.SIH-3/4 — constraint holders и негативные стейкхолдеры обязательны к выявлению |
| BABOK v3, ch. 3 (BA Planning and Monitoring) | Stakeholder identification — первая задача планирования, выполняется до elicitation | **Adopted as-is** — ScopeCut воспроизводит: идентификация строго до elicitation | Добавлен explicit freshness condition (stale при изменении оргструктуры), не присутствующий в BABOK. Anti-pattern «Stakeholder proxy substitution» называет misuse, не описанный в BABOK |
| IREB CPRE FL, ch. 2 (System and Context Boundaries) | Context boundary analysis: идентификация всех источников воздействия на систему, включая внешние системы и constraint holders | **Adopted** — MandatoryConstraints требуют идентификации holders constraints | Добавлена coverage characterization (доля типов стейкхолдеров с представителем) и explicit negative stakeholder requirement. IREB фиксирует необходимость, BAPF даёт измеримую проверку через conformance checklist |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Stakeholder как роль (Role) и её concern | `A.2`, `A.2.1` |
| Concern как problem signal до превращения в требование | `C.22.2` |
| BoundedContext для локализации значения concern | `C.11` |
| Coverage как характеризация полноты | `C.16` |
| Приоритизация стейкхолдеров и их concerns | `G.9` |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L154-L222
