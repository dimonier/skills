# EWA.ProjectContext: Проектный AGENTS.md

> **Trigger:** При старте нового проекта или при создании AGENTS.md, когда агент путает DPF/LPF-правила с проектной спецификой
> **Governing patterns:** 
>   → `../dpf-fpf-literacy/references/5-agent-context-load.md`
>   → `../fpf-core/references/C.11-bounded-context.md`
>   → `../fpf-core/references/E.17.EFP-first-entry.md`
>   → `../fpf-core/references/E.4-ecosystem-family.md`
>   → `../fpf-core/references/E.5.3-unidirectional.md`

---

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

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `EWA.DependencyChain` | `EWA.ProjectContext` | Project → LPF → DPF → FPF chain начинается в Project AGENTS.md |
| `EWA.LPFvsProject` | `EWA.ProjectContext` | Критерий различения определяет, что попадает в LPF, а что — в Project |

---

> **Source:** `assets/FPF-Ecosystem-Workspace-dpf.md` lines L340-L375
