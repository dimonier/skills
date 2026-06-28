# BAR.RequirementSpecification: Спецификация требований

> **Trigger:** Требования записаны в свободной форме — разработчик и тестировщик интерпретируют их по-разному; требование нельзя проверить (нет измеримого acceptance criteria)
> **Governing patterns:** 
>   → `../fpf-core/references/C.16-coverage.md`
>   → `../fpf-core/references/A.19-evaluation-characteristics.md`
>   → `../fpf-core/references/A.19.ECS-evaluation-char-set.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/G.9-selector.md`
>   → `../fpf-core/references/C.25-q-bundle.md`
>   → `../fpf-core/references/A.10-evidence.md`
>   → `../fpf-core/references/C.2.1-episteme.md`
>   → `../fpf-core/references/E.17-multi-view.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Требования записаны в свободной форме на естественном языке — разработчик и тестировщик интерпретируют их по-разному; требование нельзя проверить (нет измеримого acceptance criteria); разные требования противоречат друг другу, но противоречие не обнаружено до кодирования |
| **ContextGrounding** | Фаза specification: превращение сырых материалов elicitation в документированные требования, пригодные для передачи в разработку и тестирование |
| **ScopeCut** | Спецификация отдельного требования или набора требований в рамках одного bounded context; не охватывает архитектурную спецификацию системы |
| **NotWishReason** | «Напишем SRS на 300 страниц, как в ГОСТе» — без учёта, кто и как будет использовать эту спецификацию |

## Conditional Fields

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

## Characterization Measures

| Characteristic | Measurement protocol | Target threshold |
|---|---|---|
| **Unambiguity** | Три независимых читателя (разработчик, тестировщик, стейкхолдер) читают требование и независимо формулируют ожидаемое поведение; pairwise agreement rate — доля пар «читатель A и B дали одинаковую интерпретацию» | `≥ 0.90` pairwise agreement |
| **Atomicity** | Для каждого требования проверка: содержит ли оно ровно одну функцию/ограничение? Критерий: «может ли требование быть независимо приоритизировано и протестировано?» | `≥ 0.95` требований атомарны |
| **Verifiability** | Для выборки из ≥20 требований тестировщик пишет test case ТОЛЬКО по acceptance criteria; доля требований, для которых test case написан без дополнительных разъяснений | `≥ 0.90` успешной test-case derivation |

## Worked Examples

**Positive Worked Slice:** В govtech-проекте разработки реестровой системы бизнес-аналитик для каждого из 120 требований зафиксировал quantified acceptance criteria в формате «stimulus → response → measure». Для требования «реестр должен масштабироваться под пиковую нагрузку» зафиксировано: «при 500 одновременных запросов время ответа ≤ 3 сек для 95% запросов». На приёмке подрядчик заявил «система работает хорошо», но нагрузочное тестирование заказчика показало 15 сек при 200 пользователях. Благодаря измеримым criteria спор разрешён объективно: подрядчик признал несоответствие и выполнил доработку за свой счёт.

**Near-Miss Example:** Требование «система должна формировать отчёт в PDF с группировкой по менеджерам» — однозначно, атомарно, criteria измеримы. На приёмке стейкхолдер: «не то — нужен Excel для сводки». Problem statement правильный, но стейкхолдер не знал, что PDF не позволит обработку. Это не дефект спецификации, а ошибка validation. Применяется `BAR.RequirementValidation`.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Natural-language literature** | Требование — эссе: «Система должна обеспечивать удобный интерфейс, позволяющий быстро и эффективно обрабатывать заявки с гибкой настройкой…» | MandatoryConstraints запрещают «удобно», «быстро», «гибкой» без quantified measure |
| **Atomicity violation** | Одно требование: «регистрировать заявку, отправлять уведомление и формировать отчёт» — три независимые функции | Нарушение атомарности блокирует независимую приоритизацию и тестирование |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.RSP-1` | Каждое требование содержит: уникальный идентификатор, описание функции/ограничения, actor/role | AcceptanceCriterion пп. (1)-(3) |
| `CC-BAR.RSP-2` | Acceptance criteria измеримы; НФТ содержит quantified scenario (stimulus → response → measure) | AcceptanceCriterion п. (4) |
| `CC-BAR.RSP-3` | Требование не содержит неоднозначных терминов («быстро», «удобно», «достаточно») без quantified measure | MandatoryConstraints |
| `CC-BAR.RSP-4` | Одно требование — одна функция/ограничение (атомарность) | MandatoryConstraints: запрет неатомарных |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| Wiegers & Beatty, 3rd Ed., ch. 11 / ISO/IEC/IEEE 29148:2018, ch. 6 | Характеристики качества требования: unambiguous, complete, correct, feasible, necessary, prioritized, verifiable | **Adopted** — MandatoryConstraints и CharacterizationRelation воспроизводят характеристики качества | **Extended:** Wiegers/ISO называют характеристики; BAPF добавляет explicit запрет конкретных неоднозначных терминов («быстро», «удобно», «достаточно», «при необходимости») без quantified measure. Anti-pattern «Natural-language literature» даёт detection rule для violation, отсутствующий в Wiegers |
| IREB CPRE FL, ch. 5 (Requirements Documentation) | Структура спецификации: ID, описание, rationale, acceptance criteria, source; документация как activity | **Adopted** — AcceptanceCriterion воспроизводит IREB-структуру документированного требования | Добавлен mandatory quantified scenario формат для НФТ: stimulus → response → measure. IREB упоминает quantifiability, BAPF задаёт структурный шаблон |
| BABOK v3, ch. 7 (Requirements Analysis and Design Definition) | Quality criteria для требований; проверка спецификации на измеримость, атомарность, непротиворечивость | **Adopted** — ImprovementCheck operationalizes BABOK quality criteria | Added ValidationBoundary: тестировщик по acceptance criteria пишет test case без разъяснений. BABOK говорит о testability, BAPF даёт operational test через внешнюю проверку тестировщиком |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Характеристики качества требования | `C.16`, `A.19` (ECS) |
| Acceptance criteria как acceptance probe | `C.22.2` |
| Приоритет требования | `G.9` (parity/priority), `C.25` (Q-bundle) |
| Трассировка до источника | `A.10` (Evidence Graph) |
| Требование как эпистемический артефакт | `C.2.1` (Episteme), `E.17` (MultiView) |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L364-L440
