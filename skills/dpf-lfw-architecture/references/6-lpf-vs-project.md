# EWA.LPFvsProject: Различение LPF и Project

> **Trigger:** При решении, куда поместить правило — в LPF (организационный уровень) или в проектный AGENTS.md (уровень исполнения)
> **Governing patterns:** 
>   → `../fpf-core/references/E.4-ecosystem-family.md`
>   → `../dpf-fpf-literacy/references/2-ecosystem-placement.md`
>   → `../fpf-core/references/E.5.3-unidirectional.md`
>   → `../fpf-core/references/C.11-bounded-context.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`

---

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

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `EWA.LPFvsProject` | `EWA.ProjectContext` | Критерий различения определяет, что попадает в LPF, а что — в Project |
| `EWA.LPFvsProject` | `EWA.DependencyChain` | LPF — звено в цепочке между Project и DPF |
| → `FPFLIT.FrameworkEcosystemPlacement` | `EWA.LPFvsProject` | Ecosystem placement — grounding для различения уровней |

---

> **Source:** `assets/FPF-Ecosystem-Workspace-dpf.md` lines L378-L413
