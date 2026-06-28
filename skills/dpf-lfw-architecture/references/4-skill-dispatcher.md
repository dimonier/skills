# EWA.SkillDispatcher: SKILL.md как диспетчер, не хранилище знаний

> **Trigger:** При создании или правке SKILL.md скилла — до того как тело скилла раздуется предметными паттернами
> **Governing patterns:** 
>   → `../fpf-core/references/C.33-carrier-admission.md`
>   → `../fpf-core/references/E.17.EFP-first-entry.md`
>   → `../fpf-core/references/E.4.DA-quality-route.md`

---

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

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `EWA.SkillAsFrameworkCarrier` | `EWA.SkillDispatcher` | Carrier architecture требует routing-only SKILL.md |
| `EWA.MonolithInSkill` | `EWA.SkillDispatcher` | Монолит — source для references; SKILL.md — routing к ним |
| `EWA.DependencyChain` | `EWA.SkillDispatcher` | Dispatcher направляет к reference; reference содержит governing cues для chain |

---

> **Source:** `assets/FPF-Ecosystem-Workspace-dpf.md` lines L303-L337
