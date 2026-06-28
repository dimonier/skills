# BAR.DataRequirements: Выявление и спецификация требований к данным

> **Trigger:** Требования к данным — «перечень атрибутов без бизнес-правил валидации, жизненного цикла данных, privacy/retention требований»; модель данных создаётся разработчиком без участия аналитика
> **Governing patterns:** 
>   → `../fpf-core/references/C.16-coverage.md`
>   → `../fpf-core/references/C.25-q-bundle.md`
>   → `../fpf-core/references/A.7-strict-distinction.md`
>   → `../fpf-core/references/C.27-temporal.md`
>   → `../fpf-core/references/A.2-role.md`
>   → `../fpf-core/references/A.2.1-role.md`
>   → `../fpf-core/references/A.10-evidence.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Требования к данным — «система должна хранить поля: ФИО, дата рождения, телефон» — перечень атрибутов без business rules валидации, без жизненного цикла данных, без privacy/retention требований; модель данных создаётся разработчиком без участия аналитика; миграция данных с legacy-систем не учтена |
| **ContextGrounding** | Проект, где данные — центральный актив (учётная система, CRM, ERP, реестр, витрина данных); требования к данным — обязательная часть спецификации |
| **ScopeCut** | Выявление, анализ и спецификация требований к данным как подмножества требований к системе; не охватывает проектирование БД, администрирование, ETL-разработку |
| **NotWishReason** | «Данные — забота разработчика, аналитик описывает только экраны» — отказ от работы с данными, приводящий к разрыву между бизнес-требованиями и моделью данных |

## Conditional Fields

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

## Characterization Measures

| Characteristic | Measurement protocol | Target threshold |
|---|---|---|
| **Data requirement completeness** | Для каждой бизнес-сущности проверяется наличие каждого из 5 аспектов: (1) атрибуты с типами/constraints, (2) правила валидации, (3) жизненный цикл, (4) целевые метрики качества, (5) privacy/retention классификация. Оценка: доля покрытых аспектов от 5 на сущность, усреднённая по всем сущностям | `≥ 0.90` (среднее 4.5/5 аспектов на сущность) |
| **Validation rule coverage** | Для каждой сущности: число зафиксированных правил валидации, делённое на число атрибутов сущности. Для ключевых атрибутов (ИНН, телефон, email, дата) проверяется наличие ≥1 правила; нулевое значение допустимо для неключевых атрибутов (например, комментарий) | `≥ 0.50` правил на атрибут (в среднем); `= 1.00` для ключевых атрибутов |
| **CDE quality target measurability** | Для каждого Critical Data Element (CDE): наличие quantified quality target по ≥3 dimensions ISO 25012 (accuracy, completeness, consistency, timeliness, uniqueness); доля CDE с quantified targets от общего числа CDE | `≥ 0.95` CDE с quantified targets |

## Worked Examples

**Positive Worked Slice:** В медицинской информационной системе бизнес-аналитик специфицировал data requirements для сущности «Пациент»: атрибуты с типами и constraints, правила валидации (СНИЛС — regex + контрольная сумма), классификация персональных данных по 152-ФЗ (категория «специальные» — медицинские данные). Для каждого critical data element зафиксирован срок хранения: медкарта — 25 лет с даты последнего обращения (приказ Минздрава), согласие на обработку — 5 лет после отзыва. Retention policy в data requirements позволила: (1) настроить автоматическое удаление просроченных согласий, (2) на аудите Роскомнадзора предъявить documented policy — штраф по 152-ФЗ предотвращён.

**Transfer:** в розничной торговле quantified data quality targets для CDE «Цена» и «Остаток» (по ISO 25012) предотвратили каскадную ошибку ценообразования при синхронизации ERP с 200 точками продаж — 0 инцидентов цены vs 15 инцидентов в месяц до внедрения data requirements.

**Near-Miss Example:** Data requirements для сущности «Заявка» содержат: атрибуты, правила валидации, retention = 3 года. Через год аудит обнаруживает: в заявках хранятся персональные данные заявителей, срок истёк у 15% записей, но данные не удалены — retention policy задана на уровне сущности «Заявка», а не на уровне персональных данных внутри неё. Это не misuse DataRequirements (policy есть), а дефект классификации: privacy classification выполнена на уровне сущности, а не атрибута. Применяется уточнение по `BAR.RequirementSpecification` (atomicity data requirements), а не переписывание всего data requirements пакета.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Data requirements = перечень полей** | «Система хранит ФИО, телефон, email» — плоский список атрибутов без типов, constraints, правил валидации, без жизненного цикла и privacy classification | AcceptanceCriterion требует: атрибуты с типами/constraints, правила валидации, жизненный цикл, качество, privacy. Перечень полей покрывает ≤20% требований к данным |
| **Модель данных без аналитика** | Разработчик создал схему БД по «здравому смыслу»; бизнес-правила (уникальность ИНН, формат ОГРН, кросс-проверка дат) реализованы частично или неверно; privacy requirements отсутствуют | MandatoryConstraints запрещают проектирование модели данных без участия аналитика. Разработчик не знает business rules и regulatory constraints — результат: до 40% валидаций не реализованы |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| CC-BAR.DRQ-1 | Для каждой сущности зафиксированы: атрибуты (имя, тип, обязательность, уникальность), правила валидации, владелец данных | Операционализирует AcceptanceCriterion п. (1): структура сущности |
| CC-BAR.DRQ-2 | Для персональных данных зафиксированы: категория, срок хранения, условие удаления; источник требования (закон, регламент) указан | Операционализирует AcceptanceCriterion пп. (2)-(3) и MandatoryConstraints: privacy/retention |
| CC-BAR.DRQ-3 | Legacy-данные профилированы до миграции: documented issues, план очистки | Операционализирует AcceptanceCriterion п. (6): миграция без сюрпризов |
| CC-BAR.DRQ-4 | Разработчик по data requirements создаёт схему БД; тестировщик по data quality targets пишет тесты | Операционализирует ValidationBoundary: data requirements реализуемы и тестируемы |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| BABOK v3, ch. 10.16 (Data Modeling) | Data Modeling как техника анализа требований: ERD, class diagrams, data dictionary; моделирование структуры данных как part of requirements analysis | **Extended** — BABOK описывает моделирование данных как технику; BAPF добавляет mandatory privacy/retention requirements, legacy profiling и обязательное участие аналитика в проектировании модели данных | Substantial extension: BABOK covers data structure modeling; BAPF adds 3 dimensions absent in BABOK — (1) privacy/retention lifecycle per attribute, (2) legacy data profiling with documented issues, (3) mandatory analyst sign-off on database schema. Anti-pattern «Модель данных без аналитика» называет misuse, не описанный в BABOK |
| DAMA-DMBOK2, ch. 3 (Data Governance) / ISO 25012 (Data Quality Model) | DAMA-DMBOK2: data governance framework — data owner, data classification, stewardship. ISO 25012: 15 dimensions качества данных | **Adopted** — DAMA data owner/classification concept и ISO 25012 dimensions использованы как source reference для AcceptanceCriterion и CharacterizationRelation | Операционализация: DAMA задаёт governance-контекст, BAPF превращает его в проверяемые требования (data quality targets для CDE, верификация через тестировщика по data quality targets). DAMA — framework, BAPF — conformance gate |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Data quality dimensions как характеризация | `C.16` |
| Business rule как constraint | `C.25`, `A.7` |
| Жизненный цикл данных как temporal states | `C.27` |
| Data owner как Role с ответственностью | `A.2`, `A.2.1` |
| Data requirement traceability до источника (закон, регламент) | `A.10` |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L894-L973
