# BAR.UseCaseModeling: Моделирование вариантов использования

> **Trigger:** Use cases пишутся как «пользователь нажимает кнопку X, система показывает экран Y» — UI-спецификация, а не описание цели пользователя; альтернативные потоки пропущены
> **Governing patterns:** 
>   → `../fpf-core/references/A.2-role.md`
>   → `../fpf-core/references/A.2.1-role.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/A.21-gate-decision.md`
>   → `../fpf-core/references/C.25-q-bundle.md`
>   → `../fpf-core/references/C.27-temporal.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Use cases пишутся как «пользователь нажимает кнопку X, система показывает экран Y» — UI-спецификация, а не описание цели пользователя; основной успешный сценарий описан, но альтернативные потоки пропущены; pre/post-conditions не проверяемы; use case не отвечает на вопрос «какую цель достигает actor?» |
| **ContextGrounding** | Проект с use case modelling как техникой спецификации функциональных требований; система имеет ≥3 типов акторов с различными целями |
| **ScopeCut** | Use case modelling как техника спецификации функциональных требований через цели акторов; не охватывает UML-нотацию как таковую, генерацию кода, сценарное тестирование |
| **NotWishReason** | «Use case — это просто текстовое описание, напишем как получится» — без структуры Кокбёрна, без goal-driven подхода, без проверяемых pre/post-conditions |

## Conditional Fields

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

## Characterization Measures

| Characteristic | Measurement protocol | Target threshold |
|---|---|---|
| **Goal clarity** | Независимый читатель (не автор use case) по тексту use case формулирует цель актора одним предложением; проверяется соответствие заявленному goal statement автора; доля совпадений по выборке из ≥10 use cases | `≥ 0.90` совпадений |
| **Extension completeness** | Для каждого use case: доля шагов main success, для которых зафиксированы extension conditions (бизнес-правила, системные отказы, таймауты), от общего числа шагов main success | `≥ 0.85` extension-covered steps / total steps |

## Worked Examples

**Positive Worked Slice:** В страховой компании бизнес-аналитик начал с вопроса «какую цель преследует актор?» для каждого use case. Актор «Андеррайтер» заявил потребность в «быстром расчёте тарифа». Аналитик построил goal-driven use case «Рассчитать страховой тариф»: goal statement — андеррайтер получает тариф за ≤30 сек; pre-condition — заявка укомплектована; post-condition — тариф рассчитан и сохранён с историей. В процессе моделирования актор запросил «экран сравнения тарифов» — аналитик проверил: цель «сравнить» не заявлена бизнесом, сравнение не меняет решение о тарифе. Use case не был расширен под UI-желание; разработка ненужного экрана предотвращена. Через месяц актор подтвердил: цель достигнута без «сравнения».

**Transfer:** в телекоме goal-driven подход к use case предотвратил реализацию 12 UI-экранов «админки биллинга», которые менеджеры запросили «для удобства», но которые не соответствовали ни одной документированной цели актора — экономия 6 человеко-месяцев.

**Near-Miss Example:** Use case «Оформить полис» описан без UI-деталей: актор — Страхователь, цель — получить полис, post-condition — полис выпущен и отправлен. Extension scenarios: «Страхователь не прошёл скоринг» — система отказывает. Через месяц выясняется: скоринг возвращает не «да/нет», а три уровня риска; для среднего уровня риска требуется ручное согласование андеррайтером. Это не misuse UseCaseModeling (структура корректна), а дефект `BAR.RequirementElicitation` — бизнес-правило скоринга не было выявлено как источник требований. Применяется elicitation, а не переписывание use case.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Use case как UI flow** | Use case описывает последовательность экранов: «пользователь открывает форму X, выбирает из выпадающего списка Y, нажимает кнопку Z»; цель актора не указана | MandatoryConstraints запрещают описание как последовательность UI-действий. Паттерн требует goal statement и шаги в формате «actor intention → system responsibility» |
| **Счастливый путь без extensions** | Use case содержит только main success scenario; альтернативные потоки не описаны или описаны как «если ошибка — показать сообщение» без specific failure condition | MandatoryConstraints запрещают use case без extension scenarios. Без extensions тестировщик не может написать тесты для failure modes — до 40% сценариев не покрыто |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| CC-BAR.UCM-1 | Каждый use case имеет goal statement: «Actor X достигает цели Y посредством системы» | Операционализирует AcceptanceCriterion п. (1): goal-driven подход |
| CC-BAR.UCM-2 | Use case не содержит UI-специфичных деталей; шаги в формате «actor intention → system responsibility» | Операционализирует MandatoryConstraints и AcceptanceCriterion п. (7): UI-neutrality |
| CC-BAR.UCM-3 | Для каждого шага main success зафиксированы extension conditions, покрывающие бизнес-правила, системные отказы, таймауты | Операционализирует AcceptanceCriterion пп. (5)-(6): extension completeness |
| CC-BAR.UCM-4 | Тестировщик по use case пишет test cases для main success и всех extensions без дополнительных разъяснений | Операционализирует ValidationBoundary: testability через use case |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 10.50 (Use Cases and Scenarios) | Use cases как техника спецификации: описание взаимодействия актора с системой для достижения цели; main success + alternative flows | **Extended** — BABOK описывает use cases как технику спецификации; BAPF добавляет mandatory goal-driven структуру по Кокбёрну и explicit запрет UI-flow описаний | BABOK treats use case as one of many specification techniques; BAPF elevates goal-driven framing to mandatory structure (goal statement, actor intention → system responsibility steps) and names anti-pattern «Use case как UI flow», не выделенный в BABOK |
| Cockburn, *Writing Effective Use Cases* (2000) | Каноническая структура: goal, pre/post-conditions, extensions, UI-neutrality; use case как контракт между стейкхолдерами | **Adopted** — Cockburn-структура воспроизведена как MandatoryConstraints (goal statement, проверяемые pre/post-conditions, extensions, запрет UI-деталей) | Adopted as-is; BAPF operationalization adds conformance checklist and anti-pattern catalog but no novel practice beyond Cockburn. Anti-pattern «Счастливый путь без extensions» является прямым следствием Cockburn-требования extension completeness, не нововведением |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Actor как Role с целью | `A.2`, `A.2.1` |
| Use case goal как problem signal (потребность актора) | `C.22.2` |
| Pre/Post-conditions как acceptance probes | `C.22.2`, `A.21` |
| Extension scenario как branching (альтернатива main success) | `C.25`, `C.27` |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L815-L892
