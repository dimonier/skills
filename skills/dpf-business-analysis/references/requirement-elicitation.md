# BAR.RequirementElicitation: Выявление требований

> **Trigger:** Стейкхолдеры не могут сформулировать, что им нужно; скрытые (tacit) требования не выявляются, потому что стейкхолдер считает их «очевидными»
> **Governing patterns:** 
>   → `../fpf-core/references/A.3.4-transformation.md`
>   → `../fpf-core/references/A.10-evidence.md`
>   → `../fpf-core/references/A.2.1-role.md`
>   → `../fpf-core/references/A.15-role.md`
>   → `../fpf-core/references/A.3.2-method.md`
>   → `../fpf-core/references/B.3-assurance.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Стейкхолдеры не могут сформулировать, что им нужно, или формулируют противоречиво; бизнес-аналитик проводит интервью, но получает «всё должно работать хорошо»; скрытые (tacit) требования не выявляются, потому что стейкхолдер считает их «очевидными» |
| **ContextGrounding** | Фаза elicitation в работе с требованиями: первичный сбор информации от стейкхолдеров, документов, legacy-систем и других источников |
| **ScopeCut** | Выявление требований через подбор и применение техник elicitation; не охватывает их последующую спецификацию и валидацию |
| **NotWishReason** | «Проведём интервью и запишем, что скажут» — без подготовки структуры интервью, без кросс-валидации источников, без выявления невысказанных требований |

## Conditional Fields

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

## Worked Examples

**Positive Worked Slice:** В проекте автоматизации больничного отделения бизнес-аналитик применил комбинацию structured interview (дневная смена) и observation (ночная смена). Дневное интервью с начальником отделения описывало «идеальный» процесс; observation выявил, что ночная смена ведёт параллельный бумажный журнал, обходя систему — «требуется 5-минутный перезапуск при пересменке, ночью нет времени». Tacit knowledge зафиксировано как требование: время перезапуска ≤ 30 сек. Результат: требование, не выявляемое интервью, предотвратило отторжение системы ночной сменой и дорогостоящую доработку.

**Near-Miss Example:** Бизнес-аналитик провёл интервью с 5 стейкхолдерами, document analysis и prototyping. Через 2 месяца стейкхолдер: «не учли, что ночная смена выполняет операцию X иначе» — начальник смены описал дневной процесс. Это не проблема elicitation (техники подобраны), а stakeholder identification: «оператор ночной смены» не идентифицирован. Применяется `BAR.StakeholderIdentification`.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Interview monoculture** | Аналитик применяет только интервью для всех классов требований; НФТ записаны со слов пользователей без измерения | MandatoryConstraints запрещают единственную технику. НФТ не выявляются интервью — нужен observation и document analysis |
| **Tacit knowledge extraction theatre** | Протокол: «наблюдение — 2 часа». Зафиксировано «оператор выполняет X», но не выявлено ПОЧЕМУ он делает Y до Z вопреки инструкции | AcceptanceCriterion требует выявления tacit требований. Формальное наблюдение без probing — misuse |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.REQ-1` | Для каждого требования зафиксированы: источник, техника elicitation, дата, контекст получения | Прослеживаемость до источника |
| `CC-BAR.REQ-2` | Применено ≥2 различные техники elicitation; ни один класс не опирается только на интервью | Запрет единственной техники |
| `CC-BAR.REQ-3` | Высокорисковые требования (capacity, security, regulatory) кросс-валидированы с независимым источником | Кросс-валидация |
| `CC-BAR.REQ-4` | Tacit требования выявлены через observation/prototyping/T-shirt sizing; результат зафиксирован | Tacit knowledge |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 4 (Elicitation and Collaboration) | 50+ техник elicitation с guidelines по matching technique to source; elicitation event = prepare → conduct → confirm | **Adopted** — MandatoryConstraints требуют техники под тип источника; ImprovementCheck проверяет coverage классов требований | **Extended:** BABOK описывает техники как каталог; BAPF добавляет explicit запрет единственной техники (MandatoryConstraints) и кросс-валидацию для высокорисковых требований. Anti-pattern «Interview monoculture» называет misuse, не выделенный в BABOK |
| IREB CPRE FL, ch. 4 (Requirements Elicitation) | Классификация техник по типам источников (stakeholder, document, system); criteria for technique selection | **Adopted** — ImprovementCheck: для каждого класса требований определён источник и техника | Операционализация: Conformance Checklist CC-BAR.REQ-1/2/3 превращает IREB-классификацию в проверяемые требования. IREB классифицирует, BAPF enforcement через checklist |
| BABOK v3, ch. 10.32 (Observation) | Observation technique: active/passive observation для выявления tacit knowledge и реального (не декларируемого) поведения | **Adopted** — AcceptanceCriterion требует observation/prototyping/T-shirt sizing для tacit требований | Добавлен anti-pattern «Tacit knowledge extraction theatre»: формальное наблюдение без probing — misuse, не описанный в BABOK. BABOK даёт технику, BAPF предупреждает о misuse техники |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Elicitation как трансформация (Transformation) | `A.3.4` |
| Источник требований как источник evidence | `A.10` (Evidence Graph) |
| Роль бизнес-аналитика в elicitation | `A.2.1`, `A.15` |
| Техника elicitation как MethodDescription | `A.3.2` |
| Кросс-валидация источников | `B.3` (Trust Calculus) |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L294-L362
