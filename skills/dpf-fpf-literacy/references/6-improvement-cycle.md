# FPFLIT.DPFImprovementCycle: Цикл улучшения черновика DPF

> **Trigger:** После получения first-hour DPF — до того как опираться на него в ответственных проектных решениях
> **Governing patterns:** 
>   → `../fpf-core/references/E.22-evaluation-purpose.md`
>   → `../fpf-core/references/E.21-pattern-quality.md`
>   → `../fpf-core/references/E.23-improvement-loop.md`
>   → `../fpf-core/references/E.19-admission-review.md`
>   → `../fpf-core/references/E.16-agent-roles.md`
>   → `../fpf-core/references/E.4.DA-quality-route.md`

---

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Черновик DPF полезен, но недостаточно надёжен для ответственной опоры: в нём мало источников SoTA, нет антипаттернов, не проверены границы применимости, отсутствуют связи между паттернами |
| **ContextGrounding** | Команда имеет first-hour DPF и хочет довести его до состояния, пригодного для регулярного использования в проекте |
| **ScopeCut** | Цикл улучшения DPF как артефакта; не охватывает создание нового DPF с нуля |
| **NotWishReason** | «Прокрути цикл улучшений» агенту без задания evaluation characteristics — агент выдаст красивый список идей, но не улучшит DPF |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | FPF содержит встроенные паттерны улучшения: `E.22` (framing evaluation purpose), `E.21` (pattern-quality evaluation), `E.23` (improvement loop), `E.19` (admission review) |
| **EntityOfConcern** | DPF как улучшаемый артефакт — его характеристики качества и процесс улучшения |
| **SymptomDetection** | Попытка улучшить DPF без evaluation characteristics приводит к «улучшению ради улучшения» — агент меняет формулировки, но не устраняет структурные дефекты |
| **ProblemHypothesis** | Команда не задала характеристики для оценки DPF — нельзя улучшать то, что не умеешь измерять |
| **ImprovementCheck** | Каждый цикл улучшения: (1) заданы evaluation characteristics, (2) проведена оценка текущего состояния, (3) выбран конкретный аспект для улучшения, (4) выполнено улучшение, (5) проверен результат |
| **AcceptanceCriterion** | DPF проходит `E.21` evaluation с acceptable scores; отдельный reviewer (не автор) подтверждает улучшение; refresh route актуален |
| **MandatoryConstraints** | Улучшать можно только что-то конкретное и по явно заданным характеристикам; нужен отдельный оценщик (reviewer) и отдельный разработчик — «сам себя не проверишь»; цикл требует указания целевого уровня («до пятёрочек» или «на троечки») |
| **CharacterizationRelation** | Discoverability, source fidelity, ontology clarity, thin affordance, refreshability — из `E.4.DA` и `E.21` |
| **ValidationBoundary** | Как минимум два прохода цикла улучшения с разными reviewer |
| **FreshnessOrExpiry** | Цикл возобновляется при изменении FPF Core, появлении новых SoTA-источников, или обнаружении misuse patterns |
| **ProblemFormulationFollowUpReason** | Превратить «красивый черновик» в рабочий инструмент, на который можно опираться в проекте |
| **ReadinessDisposition** | `P2W-ready` когда evaluation characteristics заданы, а reviewer назначен |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Evaluation characteristics definition | `A.19.ECS` |
| Framing evaluation purpose | `E.22` |
| Pattern quality evaluation | `E.21` |
| Improvement loop execution | `E.23` |
| Admission review gate | `E.19` |
| Reviewer/author separation | `E.16` (agent roles) |
| Quality route для DPF | `E.4.DA` |

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `FPFLIT.FirstHourDPFRoute` | `FPFLIT.DPFImprovementCycle` | First-hour DPF — вход для цикла улучшений |
| `FPFLIT.DPFImprovementCycle` | → *all pattern cards* | Цикл улучшения применим к каждой problem card DPF |

---

> **Source:** `assets/FPF-Literacy-dpf.md` lines L299-L337
