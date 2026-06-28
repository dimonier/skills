# Domain Principle Framework: Layered Framework Workspace (LFW) — архитектура рабочей среды для стека FPF/DPF/LPF

> **Governed value:** `LayeredFrameworkWorkspace` (LFW) — переносимая файловая архитектура для сочетания FPF/DPF/LPF/Project в одной рабочей среде
> **Pattern family:** `E.4.DPF` (Domain Principle Framework Authoring)
> **Status:** Draft — First-hour route
> **Normativity:** Локально-нормативный для практики организации AI-ассистируемой инженерной рабочей среды
> **Depends on:** `FPFCorePatternSet@current`
> **DPF public label:** `FPFEcosystemWorkspaceArchitecture` (carrier name for this DPF document)

---

## 1. Context Declaration

| Поле | Значение |
|---|---|
| **BoundedContext** | `FPF-экосистема@AI-ассистируемаяРабочаяСреда` |
| **IntendedReader** | Инженер-менеджер, технический лид — организующий рабочую среду с AI-агентами для себя и команды |
| **FirstUse** | Размещение стека FPF/DPF/LPF и конкретных проектов в одной файловой среде так, чтобы агент загружал ровно нужное без RAG, индексации и конфликтов между уровнями |

### Non‑Use Boundary

- Не заменяет FPF Core — использует его как governing-pattern host (`E.4`, `E.4.DPF`, `E.4.PFAD`, `E.4.PFR`, `E.5.3`)
- Не является руководством по конкретной скилл-платформе (Claude Code, Codex, OpenCode) — формат скилла используется как де-факто переносимый стандарт
- Не охватывает создание самих DPF/LPF — для этого `FPF-Literacy-dpf.md`
- Не является заменой IWE или другой инструментальной платформы — это чисто файловая архитектура

---

## 2. Source Pack (`G.2`)

### Adopted Sources

| Источник | Роль в фреймворке |
|---|---|
| **FPF Core Specification** (Levenchuk, June 2026) | Host framework: governing-pattern cues для `E.4`, `E.5.3`, `E.4.DPF`, `E.4.PFAD`, `E.4.PFR` |
| **FPF-Literacy DPF** (Levenchuk, 28.06.2026) | Source DPF-паттернов agent context load, framework ecosystem placement, carrier first entry |
| **Anthropic Skills Specification** (skill-creator SKILL.md, agent-skill-builder SKILL.md) | Источник концепции progressive disclosure (3 уровня: metadata → body → references) и атомарности скиллов |
| **IWE (Integrated Working Environment), опыт использования** | Источник problem signals: привязка к платформе/программам делает среду непереносимой |

### Rejected Sources

- RAG-решения для индексации фреймворков — решают другую проблему (поиск по большой кодовой базе), а не прямую загрузку паттернов агентом
- Монолитные «единые спецификации» как единый agent context —坍塌 уровней, ведущая к нерелевантным ответам и перерасходу контекстного окна

> **ClaimStatus:** `provisional`

---

## 3. Architecture Decision (`E.4.PFAD`)

**`PFAD-EWA-001`**

| Слот | Значение |
|---|---|
| **FrameworkFamily** | `DomainPrincipleFramework` |
| **Purpose** | Дать архитектурные паттерны для организации рабочей среды, в которой FPF/DPF/LPF и проекты сосуществуют без конфликтов и загружаются агентом атомарно через progressive disclosure (без RAG/индексации) |

### First Pattern Set

1. **`EWA.SkillAsFrameworkCarrier`** — Упаковка DPF/LPF как скиллов с монолитом в `assets/` и извлечёнными паттернами в `references/`
2. **`EWA.MonolithInSkill`** — Канонический монолит DPF/LPF живёт в `assets/` скилла (единственный source of truth); humans читают монолит, agents читают `references/`
3. **`EWA.DependencyChain`** — Однонаправленная цепочка загрузки: Project → LPF → DPF → FPF, каждый файл сам объявляет свои governing-pattern зависимости
4. **`EWA.SkillDispatcher`** — SKILL.md как диспетчер (не содержит знаний — только routing: какая ситуация → какой reference)
5. **`EWA.ProjectContext`** — Проектный AGENTS.md ссылается на LPF/DPF-скиллы, но не содержит предметных паттернов — только project-specific конкретизацию
6. **`EWA.LPFvsProject`** — Различение LPF (организационная конкретизация DPF) и Project (исполнение работ с учётом LPF)

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
| **PrimaryName** | Принциповый фреймворк архитектуры слоистой рабочей среды для экосистемы FPF |
| **PublicLabel** | `FPFEcosystemWorkspaceArchitecture` |
| **ProvisionalAlias** | `FPFEcoWA` |
| **F18NameCard** | См. раздел 4a — Name Card для именуемого governed value (LFW) |
| **NameScope** | Bounded context организации AI-ассистируемой рабочей среды с опорой на FPF |

---

### 4a. F.18 Name Card: Layered Framework Workspace (LFW)

> Цель: дать устойчивое публичное имя архитектуре рабочей среды — переносимой, файловой, скилл-носительской организации стека FPF/DPF/LPF/Project с progressive disclosure, без RAG/индексации, с unidirectional dependency chain.

#### NameCard

| Slot | Value |
|---|---|
| **NameCardId** | `NC-LFW-001` |
| **GovernedValueRef** | `LayeredFrameworkWorkspace@FPF-экосистема` — переносимая файловая архитектура рабочей среды, в которой FPF Core, DPF и LPF упакованы как agent skills с progressive disclosure (metadata → SKILL.md-диспетчер → references/), монолиты живут в `assets/` скиллов, а проекты ссылаются на LPF/DPF-скиллы без дублирования их содержания |
| **GoverningPatternRef** | `E.4` (FPF Ecosystem Family Architecture) — архитектура семейства фреймворков и их carrier |
| **BoundedContextRef** | `FPF-экосистема@AI-ассистируемаяРабочаяСреда` |
| **LocalSenseRef** | Рабочая среда = workspace: папка с файлами, в которой сориентируется любой соображающий AI-агент. Слоистая = layered: FPF → DPF → LPF → Project с unidirectional dependency (E.5.3). Framework = принциповый фреймворк как основная единица знания. Workspace (не Environment) подчёркивает файловую, а не инструментальную природу |
| **TechLabel** | `LayeredFrameworkWorkspace` |
| **PlainLabel** | Layered Framework Workspace / слоистая рабочая среда фреймворков |
| **PublicAbbreviation** | `LFW` («эль-эф-даблю») |
| **CandidateSet** | См. таблицу Candidate Families ниже |
| **RejectedCandidates** | См. таблицу Rejected ниже |
| **SelectionRationale** | См. Selection Rationale ниже |
| **DistinctFrom** | `IWE` (Intellectual Working Environment) — привязан к платформе и инструментам, LFW — чисто файловая архитектура; `FPF Core` — governing pattern host, LFW — архитектура размещения фреймворков; `DPF` — domain knowledge, LFW — workspace architecture для размещения DPF |
| **RefreshCondition** | При изменении `E.4`, `E.5.3`, формата скиллов, или появлении нового уровня фреймворков в экосистеме FPF |

#### Candidate Families (NQD-front)

Оценка кандидатов по четырём характеристикам `F.18:4.3`:
- **SF** — Semantic Fidelity: сохраняет ли governed value без потерь/добавлений
- **RE** — Reader Ergonomics: может ли intended reader сказать и запомнить
- **MF** — Morphology Fit: соответствует ли форма слова именуемому kind (workspace architecture)
- **AR** — Alias Risk: импортирует ли читатель ложный смысл из соседних паттернов

| # | Head Family | Tech Label | Acronym | SF | RE | MF | AR | Комментарий |
|---|---|---|---|---|---|---|---|---|
| **A1** | **Layered** | **Layered Framework Workspace** | **LFW** | ★★★ | ★★★ | ★★★ | ★★★ | **Выбран.** «Слоистый» прямо указывает на FPF→DPF→LPF→Project stack. Workspace ≠ Environment. Аббревиатура чистая. |
| A2 | Layered | Framework Layered Workspace | FLW | ★★ | ★★ | ★★ | ★★ | Перестановка слов ослабляет акцент на «слоистость». |
| B1 | Stack | Framework Stack Workspace | FSW | ★★ | ★★★ | ★★ | ★★ | «Stack» в CS — LIFO/execution, а не dependency layers. Для tech-читателя привычно, но импортирует неверную метафору. |
| B2 | Stack | Principle Stack Workspace | PSW | ★★ | ★★ | ★★ | ★★★ | «Principle» вместо «Framework» теряет связь с FPF-экосистемой. |
| C1 | Strata | Strata Framework Workspace | SFW | ★★★ | ★ | ★★ | ★★ | Геологическая точность («страта» = слой породы), но слово слишком академическое для intended reader (инженер-менеджер). |
| C2 | Strata | Framework Strata Workspace | FSW | ★★ | ★ | ★★ | ★★ | То же + acronym collision с B1. |
| D1 | Progressive | Progressive Framework Workspace | PFW | ★ | ★★ | ★ | ★★ | «Progressive» отсылает к progressive disclosure, но не к layering. Политические коннотации в некоторых контекстах. |
| E1 | Tiered | Tiered Framework Workspace | TFW | ★★ | ★★ | ★★ | ★★ | «Tiered» = ярусный. Точнее, чем «stack», но менее familiar. |
| F1 | Skill-Carrier | Skill-Carrier Framework Workspace | SCFW | ★★ | ★ | ★ | ★★ | Подчёркивает механизм (skill как carrier), но слишком длинно; теряет акцент на layering. |

#### Rejected Candidates

| Candidate | Reason for rejection |
|---|---|
| `Framework Ecosystem Workspace (FEW)` | «Few» (мало) — неудачная acronym, ослабляет восприятие. Экосистема — свойство содержимого, а не архитектуры. |
| `Intellectual Working Environment (IWE)` | Уже занято; привязано к платформе и конкретным программам — антипаттерн, от которого уходим. |
| `FPF Skill Workspace (FSW)` | «FPF» в названии создаёт ложное впечатление, что архитектура — часть FPF Core (Core absorption anti-pattern). |
| `Agent Workspace Stack (AWS)` | Коллизия с Amazon Web Services. «Agent» вместо «Framework» смещает фокус на потребителя, а не на содержимое. |
| `Portable Principle Environment (PPE)` | «Environment» = IWE-ассоциация, от которой уходим. «Portable» — характеристика, а не суть. |
| `Multi-Framework Workspace (MFW)` | «Multi» не передаёт layered/stack природу, просто «много фреймворков в одной папке». |
| `Framework Skill Environment (FSE)` | «Environment» — см. выше. «Skill» — механизм, а не архитектурный принцип. |
| `Nested Framework Workspace (NFW)` | «Nested» (вложенный) — неверная метафора: DPF не вложен в FPF, а зависит от него (unidirectional dependency, не containment). |

#### Selection Rationale

**Выбран `Layered Framework Workspace` (LFW).**

По четырём осям `F.18:4.3`:

| Ось | Оценка | Обоснование |
|---|---|---|
| **Semantic Fidelity** | ★★★ | «Layered» точно передаёт архитектурный принцип: уровни FPF → DPF → LPF → Project с unidirectional dependency (E.5.3). Не «stack» (LIFO), не «nested» (containment), не «progressive» (disclosure mechanism). «Framework» сохраняет связь с FPF-экосистемой. «Workspace» — файловая природа, не инструментальная. |
| **Reader Ergonomics** | ★★★ | «Layered» — everyday word, понятен без словаря. Intended reader (инженер-менеджер) уверенно использует. «LFW» — три буквы, легко произносится. |
| **Morphology Fit** | ★★★ | Форма `Adjective + Noun + Noun` стандартна для именования архитектур и сред. Соответствует kind «workspace architecture» без смещения в role, method, или status morphology. |
| **Alias Risk** | ★★★ | Низкий. Ни одна из частей не имеет устоявшегося значения, конфликтующего с governed value. «LFW» не коллидирует с известными акронимами. |

**Что не совершенно:** «Layered» не передаёт progressive disclosure напрямую — это компенсируется PlainLabel «слоистая рабочая среда фреймворков» и контекстом употребления (всегда в связке с описанием архитектуры).

#### Plain / Tech Twin

| Register | Label |
|---|---|
| **Tech** | `LayeredFrameworkWorkspace` |
| **Plain** | Layered Framework Workspace / слоистая рабочая среда фреймворков |

Аббревиатура `LFW` допустима в обоих регистрах после первого раскрытия.

#### Lineage

| Entry | Note |
|---|---|
| `2026-06-28` | Первичное создание Name Card. Provisional status. |
| Предшественники | `FPFEcosystemWorkspaceArchitecture` (рабочее имя DPF), `FPFEcoWA` (provisional alias — retired) |

## 5. Carrier Admission (`C.33`)

| Слот | Содержание |
|---|---|
| **CapturedStructure** | Контекстная декларация, source pack, архитектурное решение; шесть `ProblemCard@Context` |
| **NotCaptured** | Полные паттерные тела `E.8` с worked slices, anti-patterns, conformance checklists; relation records `E.4.PFR`; quality evaluation `E.21` |
| **AdmissibleUse** | P2W-ready problem-side input для организации рабочей среды под FPF-стек; drafting aid для размещения новых DPF/LPF в существующей среде |
| **NonAdmissibleUse** | Замена изучения FPF Core или FPF-Literacy DPF; скилл-платформенная инструкция |

---

## 6. Problem Cards (`C.22.2`)

### 6.1 `EWA.SkillAsFrameworkCarrier` — Упаковка DPF/LPF как скиллов

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Инженер-менеджер имеет несколько DPF/LPF-монолитов и FPF Core. Агент либо читает всё целиком (перерасход контекста), либо не знает, что читать (нерелевантные ответы). Внешний RAG/индексация добавляют инфраструктурную зависимость и не решают проблему точной загрузки паттерна «под задачу» |
| **ContextGrounding** | Рабочая среда с AI-агентами; несколько предметных областей (бизнес-анализ, архитектура, методология FPF); несколько проектов; стек FPF→DPF→LPF→Project |
| **ScopeCut** | Упаковка каждого DPF и LPF как скилла с progressive disclosure; не охватывает создание самих DPF/LPF |
| **NotWishReason** | «Скилл = весь DPF одним файлом» — это монолит в другом месте, не решающий проблему |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **EntityOfConcern** | Скилл как переносимый carrier для фреймворка: директория, содержащая `SKILL.md` (диспетчер), `references/` (атомарные паттерны), `assets/` (канонический монолит) |
| **SymptomDetection** | Агент читает FPF-Spec.md (60K+ строк) целиком вместо нужного паттерна; агент путает уровни и применяет DPF-паттерн там, где нужен FPF-паттерн |
| **ProblemHypothesis** | Фреймворки опубликованы как монолиты — агент не имеет механизма загрузить ровно нужный паттерн. Скиллы с progressive disclosure решают это: metadata → диспетчер → reference-файл в 200 строк |
| **ImprovementCheck** | Агент загружает reference-файл нужного паттерна за один переход от диспетчера; контекстное окно не раздувается; ответы предметно-релевантны |
| **AcceptanceCriterion** | Каждый DPF/LPF — отдельный skill; `SKILL.md` — только routing (не содержит предметных знаний); каждый паттерн/ProblemCard извлечён в отдельный `references/*.md`; канонический монолит живёт в `assets/` |
| **MandatoryConstraints** | Монолит — единственный source of truth (человек правит его, reference-файлы — производные); SKILL.md не содержит предметных паттернов (только routing); reference-файлы самодостаточны (содержат governing-pattern cues для дальнейшей навигации) |
| **CharacterizationRelation** | Load precision (сколько строк загружено vs сколько реально нужно), routing clarity (находит ли агент нужный reference за 1 шаг), monolith fidelity (соответствие reference-файлов каноническому монолиту) |
| **ValidationBoundary** | A/B тест: агент с монолитным DPF vs агент со skill-упакованным DPF — сравнение контекстной эффективности и релевантности ответов |
| **FreshnessOrExpiry** | `stale` при изменении структуры канонического монолита (требующем пересборки reference-файлов) |
| **ProblemFormulationFollowUpReason** | Дать агенту прямой доступ к атомарным единицам знания без RAG и без загрузки монолитов |
| **ReadinessDisposition** | `P2W-ready` для упаковки существующих DPF/LPF |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Progressive disclosure (3 уровня) | skill-creator SKILL.md, agent-skill-builder SKILL.md |
| DPF authoring spine | `E.4.DPF` |
| Framework carrier selection | `C.33` |
| Publication unit и intended reader | `E.17.EFP` |

---

### 6.2 `EWA.MonolithInSkill` — Канонический монолит в `assets/` скилла

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Монолит DPF/LPF и скилл с extracted references живут в разных местах. Возникает путаница: где source of truth? Человек правит одно, агент читает другое — версии расходятся |
| **ContextGrounding** | Команда поддерживает DPF/LPF: человек читает и правит монолит, агент использует извлечённые reference-файлы. Нужен единый source of truth без дублирования |
| **ScopeCut** | Размещение канонического монолита внутри скилла (`assets/`) как единственного source of truth; не охватывает версионирование (git) |
| **NotWishReason** | «Монолит в `publications/`, references в `skills/`» — две копии одного знания, которые неизбежно разойдутся |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **EntityOfConcern** | Канонический монолит DPF/LPF как единственный source of truth — размещён в `assets/` скилла |
| **SymptomDetection** | Человек правит `DPF/BusinessAnalysis.md`; агент читает `skills/dpf-ba/references/stakeholder-analysis.md`; правки человека не доходят до агента |
| **ProblemHypothesis** | Разнесение монолита и extracted references по разным директориям создаёт две версии истины — человек и агент живут в разных реальностях |
| **ImprovementCheck** | Монолит в `skills/dpf-xxx/assets/dpf.md`. Reference-файлы в `skills/dpf-xxx/references/`. Оба в одной директории скилла. При изменении монолита — пересборка references (скриптом или вручную). Никаких внешних копий |
| **AcceptanceCriterion** | Монолит — единственный файл с полным текстом DPF/LPF; `references/` — извлечённые секции; при расхождении монолит всегда прав; скрипт синхронизации: монолит → references (однонаправленно) |
| **MandatoryConstraints** | Запрещено править reference-файлы напрямую (кроме agent-specific annotations); запрещено держать копию монолита вне скилла; человек всегда читает/правит монолит в `assets/` |
| **CharacterizationRelation** | Source-of-truth uniqueness (один источник или несколько), sync reliability (соответствие references монолиту), human accessibility (может ли человек найти и прочитать монолит) |
| **ValidationBoundary** | Проверка: после правки монолита → пересборка references → агент видит изменения |
| **FreshnessOrExpiry** | `stale` при ручной правке references без обновления монолита |
| **ProblemFormulationFollowUpReason** | Устранить расхождение между «что читает человек» и «что читает агент» |
| **ReadinessDisposition** | `P2W-ready` при размещении первого DPF в скилл |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Framework carrier и publication unit | `C.33`, `E.17.EFP` |
| Source-of-truth ownership | `E.4` (framework family member) |
| Derived artifact vs source | `E.17` (description vs described thing) |

---

### 6.3 `EWA.DependencyChain` — Однонаправленная цепочка загрузки

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Агент загружает DPF-паттерн, но не знает, что тот опирается на FPF-паттерн. Результат: агент применяет DPF, но без governing-pattern discipline — получается «красиво, но не инженерно». Или агент загружает ВСЁ на всякий случай |
| **ContextGrounding** | Стек FPF→DPF→LPF→Project с unidirectional dependency (`E.5.3`). Каждый нижний уровень объявляет зависимости от верхних. Агент должен идти по цепочке, а не гадать |
| **ScopeCut** | Механизм навигации агента по цепочке зависимостей через explicit cues в reference-файлах; не охватывает автоматическое разрешение зависимостей скилл-платформой |
| **NotWishReason** | «Агент сам разберётся, что от чего зависит» — без explicit cues агент не разберётся |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **EntityOfConcern** | Цепочка загрузки: каждый reference-файл в секции «Governing patterns» перечисляет, какие файлы вышестоящих фреймворков нужны для правильного применения этого паттерна |
| **SymptomDetection** | Агент применяет DPF-паттерн «выявляй стейкхолдеров», но не применяет FPF-паттерн «problem card» (C.22.2) — результат: список имён вместо structured problem formulation |
| **ProblemHypothesis** | Без явных governing-pattern cues агент теряет связь между уровнями — DPF применяется как изолированный рецепт, а не как конкретизация FPF-паттернов |
| **ImprovementCheck** | Каждый reference-файл содержит блок «Governing patterns: → fpf-core/references/E.X.md, → dpf-xxx/references/...» в начале. Агент загружает их по мере необходимости. Цепочка: Project → LPF → DPF → FPF |
| **AcceptanceCriterion** | Агент, загрузив DPF-паттерн, видит и загружает governing FPF-паттерны; ответ агента содержит FPF-pattern cues (problem/solution separation, evidence gaps explicit, scope cut); агент не загружает паттерны, не релевантные цепочке |
| **MandatoryConstraints** | Зависимость всегда однонаправленная (нижний уровень → верхний, никогда наоборот); запрещена циклическая зависимость; FPF-паттерны никогда не ссылаются на DPF/LPF |
| **CharacterizationRelation** | Chain completeness (все ли governing cues указаны), load precision (сколько лишнего загружено), dependency direction (нет ли обратных ссылок) |
| **ValidationBoundary** | Проверка: агент получает задачу уровня DPF → проследить, загрузил ли он нужные FPF-паттерны и применил ли их |
| **FreshnessOrExpiry** | `stale` при изменении governing-pattern ссылок в FPF Core или DPF |
| **ProblemFormulationFollowUpReason** | Дать агенту явный маршрут по уровням абстракции вместо надежды на «сам догадается» |
| **ReadinessDisposition** | `P2W-ready` при наличии governing-pattern cues во всех reference-файлах |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Unidirectional dependency | `E.5.3` |
| Framework ecosystem family | `E.4` |
| Framework relation records | `E.4.PFR` |
| Problem card governing cues | `C.22.2` |
| Framework ecosystem placement | `FPFLIT.FrameworkEcosystemPlacement` |

---

### 6.4 `EWA.SkillDispatcher` — SKILL.md как диспетчер, не хранилище знаний

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | SKILL.md скилла содержит и routing-инструкции, и предметные паттерны. Тело скилла раздувается → агент загружает всё при trigger → проблема монолита воспроизводится на уровне скилла |
| **ContextGrounding** | DPF/LPF содержит 6-15 problem cards. SKILL.md должен направлять агента к нужной, но не дублировать их содержание |
| **ScopeCut** | SKILL.md — чисто routing layer: какая ситуация → какой reference. Не содержит предметных знаний. Не охватывает ситуацию, когда routing-таблица становится слишком большой |
| **NotWishReason** | «Запишу все паттерны в SKILL.md, чтобы агент всё видел» — воспроизводит монолит на новом уровне |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **EntityOfConcern** | SKILL.md как диспетчер: `name` + `description` (уровень 1), routing-таблица (уровень 2), ссылки на `references/` (уровень 3) |
| **SymptomDetection** | SKILL.md скилла длиной 500+ строк; содержит problem cards в теле; агент при trigger загружает весь этот объём |
| **ProblemHypothesis** | Смешение routing и knowledge в одном файле отменяет преимущество progressive disclosure |
| **ImprovementCheck** | SKILL.md ≤ 80 строк (routing-таблица + правила навигации). Все предметные знания в `references/`. Агент читает SKILL.md → находит строку в таблице → загружает 1 reference |
| **AcceptanceCriterion** | `description` описывает bounded context и trigger condition; тело SKILL.md содержит только routing-таблицу («ситуация → reference») и правила навигации; нет ни одного problem card в теле SKILL.md |
| **MandatoryConstraints** | Запрещено помещать problem card, pattern body, source pack или relation records в SKILL.md; routing-таблица должна покрывать все reference-файлы; при добавлении нового reference — обязано обновление routing-таблицы |
| **CharacterizationRelation** | Routing table completeness, dispatcher size (строк), first-hit precision (находит ли агент нужный reference за одно чтение routing-таблицы) |
| **ValidationBoundary** | Проверка: агент получает 3 разные задачи в bounded context DPF → в каждом случае загружает ровно нужный reference (не все) |
| **FreshnessOrExpiry** | `stale` при добавлении/удалении problem cards в DPF |
| **ProblemFormulationFollowUpReason** | Не дать progressive disclosure выродиться в монолит на один уровень выше |
| **ReadinessDisposition** | `P2W-ready` для каждого нового DPF/LPF skill |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Progressive disclosure (3 уровня) | skill-creator SKILL.md |
| Carrier admission для разных intended readers | `C.33`, `E.17.EFP` |
| Thin affordance (читается за ≤5 минут) | `E.4.DA` |

---

### 6.5 `EWA.ProjectContext` — Проектный AGENTS.md

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Агент в контексте конкретного проекта не знает, какие фреймворки применимы и какие локальные ограничения действуют. Либо игнорирует DPF/LPF, либо загружает всё подряд |
| **ContextGrounding** | Конкретный проект (CRM-миграция, автоматизация протоколов) выполняется в организации с существующими LPF. Проект не создаёт новых принципов — он конкретизирует LPF и DPF под свою задачу |
| **ScopeCut** | AGENTS.md проекта: список применимых skills + project-specific конкретизация (имена, ссылки, инструменты); не охватывает создание новых паттернов |
| **NotWishReason** | «Запишу все правила проекта в AGENTS.md» — дублирование LPF/DPF и их неявная модификация |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **EntityOfConcern** | Проектный AGENTS.md как точка входа агента в конкретную работу |
| **SymptomDetection** | Проектный AGENTS.md содержит BA-паттерны, архитектурные правила, шаблоны — дублирует DPF; агент не понимает, что правило — из DPF, а что — project-specific |
| **ProblemHypothesis** | Без чёткого различения «это из DPF/LPF» и «это специфика проекта» агент либо теряет governing-pattern discipline, либо переопределяет DPF-правила локально |
| **ImprovementCheck** | AGENTS.md проекта: (1) перечень skills для загрузки, (2) project-specific конкретизация: имена стейкхолдеров, ссылки на Confluence/Jira, стек, ADR-директория; (3) move exclusions проекта. Всё остальное — в LPF/DPF |
| **AcceptanceCriterion** | AGENTS.md ≤ 1 страница; первый блок — «Применимые фреймворки» (перечень skills); второй блок — проектная конкретизация (только то, чего нет в LPF/DPF); нет предметных паттернов |
| **MandatoryConstraints** | Запрещено переопределять DPF/LPF-правила в проектном AGENTS.md; запрещено дублировать содержание DPF/LPF; проектная конкретизация — только инстанциирование (имена, ссылки, инструменты), не новые методы |
| **CharacterizationRelation** | Skill references completeness (все ли нужные skills перечислены), specificity (насколько проектная конкретизация действительно project-specific), non-duplication (отсутствие DPF/LPF-контента) |
| **ValidationBoundary** | Проверка: agent в контексте проекта загружает перечисленные skills и даёт ответ, учитывающий и FPF/DPF/LPF-правила, и проектную специфику |
| **FreshnessOrExpiry** | `stale` при смене LPF, изменении состава команды или инструментов проекта |
| **ProblemFormulationFollowUpReason** | Дать агенту ровно столько контекста, сколько нужно для данного проекта, не дублируя фреймворки |
| **ReadinessDisposition** | `P2W-ready` при старте нового проекта |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Agent context load (многоуровневая память) | `FPFLIT.AgentContextLoad` |
| Bounded context проекта | `C.11` |
| Intended reader для разных носителей | `E.17.EFP` |
| LPF как конкретизация DPF | `E.4`, `E.5.3` |

---

### 6.6 `EWA.LPFvsProject` — Различение LPF и Project

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда не различает LPF (организационные практики, применимые к семейству проектов) и проектную конкретизацию (имена, ссылки, инструменты конкретного проекта). Результат: либо LPF засоряется проектной спецификой, либо проект пытается переопределить организационные правила |
| **ContextGrounding** | Организация выполняет несколько проектов в одной предметной области. LPF фиксирует «как мы применяем DPF в нашей организации». Каждый проект инстанциирует LPF под свою задачу |
| **ScopeCut** | Критерий различения: LPF = правила уровня организации (применимы к ≥2 проектам), Project = инстанциирование под один проект; не охватывает различение DPF и LPF |
| **NotWishReason** | «У нас один проект — запишу все правила в проектный AGENTS.md» — при появлении второго проекта придётся дублировать или извлекать LPF задним числом |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **EntityOfConcern** | Граница между LPF (организационный уровень) и Project (уровень исполнения работ) |
| **SymptomDetection** | В LPF попадают имена конкретных людей («Вася — PO»); в проектном AGENTS.md появляются правила уровня «всегда использовать RACI» (это из DPF); при смене состава команды правят LPF вместо проектного AGENTS.md |
| **ProblemHypothesis** | Критерий не сформулирован явно →坍塌 organisational и project уровней → LPF теряет переиспользуемость, проект теряет управляемость |
| **ImprovementCheck** | LPF: правила, применимые ко всем проектам организации в данной предметной области. Project: инстанциирование — «в этом проекте RACI живёт в Confluence #42, PO — Вася». При добавлении второго проекта LPF не меняется |
| **AcceptanceCriterion** | LPF не содержит имён, ссылок на конкретные проектные артефакты, инструментов конкретного проекта; Project AGENTS.md не содержит методов работы (they are in DPF/LPF); при смене команды проекта правится только Project AGENTS.md |
| **MandatoryConstraints** | LPF должен быть применим к ≥2 проектам (иначе это не LPF, а проектные правила); LPF зависит от DPF, но не от Project; Project зависит от LPF, но LPF не знает о Project |
| **CharacterizationRelation** | Reusability (применим ли LPF к другим проектам), specificity gradient (LPF: более абстрактно, Project: более конкретно), stability (LPF меняется реже, чем Project AGENTS.md) |
| **ValidationBoundary** | Проверка: представить второй проект в той же организации — нужно ли менять LPF? Если да — LPF содержит project-specific |
| **FreshnessOrExpiry** | `stale` при реорганизации, смене инструментов уровня организации или регуляторных требований |
| **ProblemFormulationFollowUpReason** | Удержать границу: организационные правила — в LPF, проектная конкретизация — в Project |
| **ReadinessDisposition** | `P2W-ready` для принятия решения «LPF или Project» |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Framework ecosystem levels (FPPS/FPF/DPF/LPF) | `E.4`, `FPFLIT.FrameworkEcosystemPlacement` |
| Unidirectional dependency (LPF → DPF, Project → LPF) | `E.5.3` |
| Bounded context и его границы | `C.11` |
| Scope cut для problem formulation | `C.22.2` |

---

## 7. Relation Records (`E.4.PFR` stub)

### Relation Map

| Source | Target | Relation Function |
|---|---|---|
| `EWA.SkillAsFrameworkCarrier` | `EWA.MonolithInSkill` | Carrier selection предписывает размещение монолита в `assets/` |
| `EWA.SkillAsFrameworkCarrier` | `EWA.SkillDispatcher` | Carrier architecture требует routing-only SKILL.md |
| `EWA.MonolithInSkill` | `EWA.SkillDispatcher` | Монолит — source для references; SKILL.md — routing к ним |
| `EWA.DependencyChain` | `EWA.SkillDispatcher` | Dispatcher направляет к reference; reference содержит governing cues для chain |
| `EWA.DependencyChain` | `EWA.ProjectContext` | Project → LPF → DPF → FPF chain начинается в Project AGENTS.md |
| `EWA.LPFvsProject` | `EWA.ProjectContext` | Критерий различения определяет, что попадает в LPF, а что — в Project |
| `EWA.LPFvsProject` | `EWA.DependencyChain` | LPF — звено в цепочке между Project и DPF |
| → `FPFLIT.AgentContextLoad` | `EWA.DependencyChain` | Agent context load — grounding для цепочки загрузки |
| → `FPFLIT.FrameworkEcosystemPlacement` | `EWA.LPFvsProject` | Ecosystem placement — grounding для различения уровней |
| → `FPFLIT.CarrierFirstEntry` | `EWA.SkillAsFrameworkCarrier` | Carrier first entry — grounding для выбора skill как carrier |

### Edition Dependency

| Слот | Значение |
|---|---|
| **FrameworkEditionRef** | `FPFEcosystemWorkspaceArchitecture@Draft` |
| **DependsOnEditionRefs** | `FPFCorePatternSet@current`, `FPFLiteracyPrincipleFramework@Draft` |
| **DependencyReason** | Все governing‑pattern cues ссылаются на FPF Core; problem signals используют паттерны из FPF-Literacy DPF |
| **CompatibilityBoundary** | При изменении `E.4`, `E.4.DPF`, `E.5.3`, `C.33`, `E.17.EFP` — пересмотреть ProblemCard‑поля |
| **E53ConformanceNote** | Требуется проверка после стабилизации имён паттернов |

---

## 8. Publication

| Слот | Значение |
|---|---|
| **ThisFile** | Локальный монолит первого входа |
| **PublicationScope** | Инженеры-менеджеры, технические лиды, резиденты программ рабочего развития — организующие AI-ассистированную рабочую среду |
| **FirstEntryCarrier** | `FPF-Ecosystem-Workspace-dpf.md` — читается как единый документ |
| **RelationRecordsCarrier** | Секция 7; подлежит извлечению в отдельный PFR‑файл при росте |
| **NonPublicationNote** | `FPF-Spec.md` не модифицируется; Core не расширяется |

---

## 9. Quality Route

### Evaluation Characteristics

| Характеристика | Вопрос |
|---|---|
| **WorkspaceNavigability** | Может ли агент найти нужный reference-файл за ≤2 шага от проектного AGENTS.md? |
| **SkillDispatcherPrecision** | Находит ли агент нужный reference за одно чтение routing-таблицы в SKILL.md? |
| **DependencyChainFidelity** | Все ли governing-pattern cues в reference-файлах корректны и ведут к существующим файлам? |
| **MonolithReferenceSync** | Соответствуют ли reference-файлы каноническому монолиту в `assets/`? |
| **LPFvsProjectClarity** | Различимы ли LPF (org-level) и Project (instance-level) без坍塌? |
| **PlatformIndependence** | Работает ли структура на ≥2 разных скилл-платформах без модификации? |

### Quality Framework

| Шаг | Владелец | Назначение |
|---|---|---|
| 1 | `E.22` | Framing evaluation purpose |
| 2 | `E.21` | Pattern‑quality evaluation каждого ProblemCard |
| 3 | `E.23` | Improvement loop — добавление worked slices, anti‑patterns, конформных примеров структуры |
| 4* | `E.19` | Admission review (при росте фреймворка) |

---

## 10. Currentness Route (`G.11`)

### Refresh Triggers

- Изменение FPF Core edition (особенно `E.4`, `E.4.DPF`, `E.5.3`, `C.33`)
- Появление новых DPF/LPF в рабочей среде (требующих routing-таблиц в SKILL.md)
- Adoption telemetry: агент систематически загружает не те reference-файлы или пропускает governing-pattern cues
- Изменения в формате скиллов (новый стандарт progressive disclosure)
- Локальные инциденты: расхождение монолита и references

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

## 11. Authorship Annotation

| Слот | Значение |
|---|---|
| **AuthorshipNote** | Создан как first‑hour route в соответствии с `E.4.DPF:4` по материалам FPF Core (Levenchuk, June 2026), FPF-Literacy DPF и практического опыта организации AI-ассистированной рабочей среды |
| **FPFCompliance** | Spine: context → source pack → PFAD → names → patterns → relations → quality → refresh; `C.22.2` ProblemCard@Context для каждого паттерна; governing‑pattern cues для всех out‑of‑scope claims; `C.33` carrier admission |

### Pending Work

- Полные `E.8` паттерные тела с worked slices, local anti‑patterns и near‑miss examples
- `E.4.PFR` полные записи отношений между паттернами (сейчас stub)
- ~~`F.18` name card для публичного имени~~ — выполнено (см. раздел 4a, Name Card `NC-LFW-001`)
- `F.17` UnifiedTermRow для публикации LFW как cross-context термина
- Конформный пример структуры workspace (реальный workspace с расставленными skills)
- Скрипт синхронизации «монолит → references» (извлечение problem cards и паттернов)
- `E.21` evaluation scores первого драфта
- `E.23` improvement loop с adoption telemetry
- Проверка на conformance с актуальной версией FPF Core после стабилизации имён паттернов
- `F.18` Name Card для DPF как framework edition (имя самого DPF-документа, отдельно от governed value LFW)

---

## Appendix A. Конформный пример структуры workspace

```
workspace/
├── AGENTS.md
│
├── skills/
│   ├── fpf-core/
│   │   ├── SKILL.md                  # Диспетчер: ситуация → reference
│   │   ├── references/               # Извлечённые FPF-паттерны
│   │   │   ├── E.4-ecosystem.md
│   │   │   ├── E.4.DPF-authoring.md
│   │   │   ├── E.4.PFAD-decision.md
│   │   │   ├── E.4.PFR-relations.md
│   │   │   ├── E.5.3-unidirectional.md
│   │   │   ├── E.8-pattern-body.md
│   │   │   ├── C.22.2-problem-card.md
│   │   │   ├── C.33-carrier-admission.md
│   │   │   ├── G.2-source-pack.md
│   │   │   ├── G.11-currentness.md
│   │   │   └── INDEX.md
│   │   └── assets/
│   │       └── FPF-Spec.md           # Канонический монолит (source of truth)
│   │
│   ├── dpf-fpf-literacy/
│   │   ├── SKILL.md                  # Диспетчер
│   │   ├── references/               # problem cards
│   │   │   ├── 1-vanilla-vs-fpf.md
│   │   │   ├── 2-ecosystem-placement.md
│   │   │   ├── 3-move-exclusion.md
│   │   │   ├── 4-first-hour-route.md
│   │   │   ├── 5-agent-context-load.md
│   │   │   ├── 6-improvement-cycle.md
│   │   │   ├── 7-sota-recognition.md
│   │   │   ├── 8-carrier-first-entry.md
│   │   │   └── relations.md
│   │   └── assets/
│   │       └── FPF-Literacy-dpf.md   # Канонический монолит
│   │
│   ├── dpf-business-analysis/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── assets/
│   │       └── BABusinessAnalysis-dpf.md
│   │
│   ├── dpf-is-architecture/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── assets/
│   │       └── ISArchitecture-dpf.md
│   │
│   ├── dpf-meeting-protocol/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── assets/
│   │       └── MeetingProtocolAutoGeneration-dpf.md
│   │
│   └── lpf-my-org/
│       ├── SKILL.md
│       ├── references/
│       │   ├── ba-process.md         # "BA в MyOrg: DPF-BA + роль PO + Jira"
│       │   ├── arch-review.md        # "Arch review в MyOrg: DPF-ISA + ADR + комитет"
│       │   └── protocol-rules.md     # "Протоколы в MyOrg: DPF-MP + корп. шаблон"
│       └── assets/
│           └── my-org-lpf.md         # Канонический монолит LPF
│
└── projects/
    ├── crm-migration/
    │   └── AGENTS.md                 # "Skills: lpf-my-org, dpf-ba, dpf-isa"
    └── meeting-automation/
        └── AGENTS.md                 # "Skills: lpf-my-org, dpf-mp"
```

### Цепочка загрузки (пример)

```
Project: projects/crm-migration/AGENTS.md
  → "Use skills: lpf-my-org, dpf-business-analysis"
    → skills/lpf-my-org/SKILL.md (диспетчер)
      → skills/lpf-my-org/references/ba-process.md
        → governing cues: dpf-business-analysis/references/stakeholder-analysis.md
          → governing cues: fpf-core/references/C.22.2-problem-card.md
            → fpf-core/references/E.8-pattern-body.md
```

Ни на одном шаге не требуется RAG, индексация или чтение монолита. Каждый файл ∼200 строк.
