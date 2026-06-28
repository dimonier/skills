# BAR.ProblemVsSolutionSeparation: Разделение проблемы и решения

> **Trigger:** Стейкхолдер формулирует требование как «постройте мне кнопку X» (решение), а не «я не могу сделать Y за Z минут» (проблема)
> **Governing patterns:** 
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/A.7-strict-distinction.md`
>   → `../fpf-core/references/A.0-episteme.md`
>   → `../fpf-core/references/C.2.1-episteme.md`
>   → `../fpf-core/references/G.9-selector.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Стейкхолдер формулирует требование как «постройте мне кнопку X» (решение), а не «я не могу сделать Y за Z минут» (проблема); команда начинает проектировать и реализовывать решение, не поняв проблему; реализованное решение не решает действительную проблему стейкхолдера |
| **ContextGrounding** | Работа бизнес-аналитика на входе в проект/итерацию: получение входа от стейкхолдеров и превращение его в требования, пригодные для передачи в разработку |
| **ScopeCut** | Разделение problem description и solution description на этапе elicitation и analysis; не охватывает архитектурное проектирование решения |
| **NotWishReason** | «Заказчик сказал — делаем» — принятие solution-shaped request как требования без анализа проблемы |

## Conditional Fields

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

## Worked Examples

**Positive Worked Slice:** В fintech-проекте стейкхолдер запросил «кнопку экспорта данных в Excel с фильтрацией и группировкой». Бизнес-аналитик применил problem framing: выяснил, что менеджер тратит 3 часа в неделю на ручную сверку данных из трёх систем (CRM, биллинг, бухгалтерия). Отделённая от решения проблема — противоречивость данных, а не отсутствие экспорта — привела к реализации scheduled reconciliation pipeline. Результат: время сверки сокращено с 3 часов до 5 минут; реализована не кнопка, а устранение корневой проблемы.

**Near-Miss Example:** Стейкхолдер: «Нужен экспорт данных в Excel с фильтрацией и группировкой». Бизнес-аналитик записал problem statement, стейкхолдер подтвердил. Выяснилось: проблема не в отсутствии экспорта (он есть), а в противоречивости данных между системами. Это не ошибка problem framing, а ошибка elicitation — не выявлен root cause. Применяется `BAR.RequirementElicitation`.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Specification disguised as problem statement** | Problem statement: «система должна обеспечивать время отклика ≤ 2 сек» — спецификация под видом problem framing | AcceptanceCriterion требует наблюдаемую проблему, субъекта и текущее состояние. Спецификация без текущего измерения — антипаттерн |
| **Problem framing as infinite regress** | Аналитик строит цепочку «five whys» до стратегии компании; команда ждёт спецификацию третью неделю | ScopeCut: problem framing на этапе анализа, не стратегический консалтинг. Достаточно одного уровня problem context |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.PVS-1` | Для каждого требования зафиксирован problem statement: наблюдаемая проблема, кто испытывает, как измеряется сейчас | AcceptanceCriterion пп. (1)-(3) |
| `CC-BAR.PVS-2` | Для каждого требования зафиксировано, что считается решением (acceptance criteria) | AcceptanceCriterion п. (4) |
| `CC-BAR.PVS-3` | Для каждого требования зафиксированы rejected alternatives с причинами отклонения | AcceptanceCriterion п. (5) |
| `CC-BAR.PVS-4` | Ни одно требование не зафиксировано как «реализовать F» без указания потребности | MandatoryConstraints |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 6 (Strategy Analysis) | Problem framing — отделение потребности от решения до определения scope; strategy analysis предшествует solution design | **Adopted** — AcceptanceCriterion требует problem statement раньше solution description | **Extended:** BABOK описывает framing как аналитическую деятельность; BAPF даёт конкретную 5-элементную структуру (problem statement, who, current measure, acceptance, rejected alternatives) и запрещает requirement без problem context через MandatoryConstraints. BABOK — guideline, BAPF — gate |
| BABOK v3, ch. 7 (Requirements Analysis and Design Definition) | Различение need и solution в спецификации требования: требование описывает потребность, не реализацию | **Adopted** — MandatoryConstraints запрещают solution-shaped request как требование без problem context | Операционализация через CharacterizationRelation: solution neutrality как измеримая характеристика. Anti-pattern «Specification disguised as problem statement» — BABOK описывает различение, BAPF даёт detection rule |
| IREB CPRE FL, ch. 3 (Requirements Elicitation) | Problem analysis vs solution design как раздельные этапы: анализ проблемы предшествует проектированию решения | **Adopted** — ScopeCut воспроизводит разделение этапов | Added freshness condition (stale при изменении бизнес-процесса) и ReadinessDisposition `P2W-ready` как gate. IREB разделяет этапы концептуально, BAPF даёт критерий готовности к переходу |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Различение Problem и Solution | `C.22.2` (ProblemCard@Context) |
| Различение описания (Description) и описываемого (EntityOfConcern) | `A.7` (Strict Distinction) |
| Requirement как эпистемический артефакт | `A.0` (Episteme), `C.2.1` |
| Приёмочный критерий как acceptance probe | `C.22.2` (acceptance probe) |
| Rejected alternatives | `G.9` (parity) |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L224-L292
