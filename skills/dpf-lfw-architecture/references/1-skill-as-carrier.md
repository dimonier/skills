# EWA.SkillAsFrameworkCarrier: Упаковка DPF/LPF как скиллов

> **Trigger:** При наличии нескольких DPF/LPF-монолитов и необходимости загружать их агенту атомарно, не перерасходуя контекстное окно
> **Governing patterns:** 
>   → `../fpf-core/references/E.4.DPF-authoring.md`
>   → `../fpf-core/references/C.33-carrier-admission.md`
>   → `../fpf-core/references/E.17.EFP-first-entry.md`

---

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

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `EWA.SkillAsFrameworkCarrier` | `EWA.MonolithInSkill` | Carrier selection предписывает размещение монолита в `assets/` |
| `EWA.SkillAsFrameworkCarrier` | `EWA.SkillDispatcher` | Carrier architecture требует routing-only SKILL.md |
| → `FPFLIT.CarrierFirstEntry` | `EWA.SkillAsFrameworkCarrier` | Carrier first entry — grounding для выбора skill как carrier |

---

> **Source:** `assets/FPF-Ecosystem-Workspace-dpf.md` lines L189-L225
