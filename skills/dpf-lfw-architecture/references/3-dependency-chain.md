# EWA.DependencyChain: Однонаправленная цепочка загрузки

> **Trigger:** При навигации агента между уровнями фреймворков (Project → LPF → DPF → FPF) — до применения DPF/LPF-паттерна без governing-pattern discipline
> **Governing patterns:** 
>   → `../fpf-core/references/E.5.3-unidirectional.md`
>   → `../fpf-core/references/E.4-ecosystem-family.md`
>   → `../fpf-core/references/E.4.PFR-relations.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../dpf-fpf-literacy/references/2-ecosystem-placement.md`

---

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

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `EWA.DependencyChain` | `EWA.SkillDispatcher` | Dispatcher направляет к reference; reference содержит governing cues для chain |
| `EWA.DependencyChain` | `EWA.ProjectContext` | Project → LPF → DPF → FPF chain начинается в Project AGENTS.md |
| `EWA.LPFvsProject` | `EWA.DependencyChain` | LPF — звено в цепочке между Project и DPF |
| → `FPFLIT.AgentContextLoad` | `EWA.DependencyChain` | Agent context load — grounding для цепочки загрузки |

---

> **Source:** `assets/FPF-Ecosystem-Workspace-dpf.md` lines L264-L299
