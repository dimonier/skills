# EWA.MonolithInSkill: Канонический монолит в `assets/` скилла

> **Trigger:** При размещении DPF/LPF в скилл — до экстракции reference-файлов, при обнаружении расхождения между монолитом и references
> **Governing patterns:** 
>   → `../fpf-core/references/C.33-carrier-admission.md`
>   → `../fpf-core/references/E.17.EFP-first-entry.md`
>   → `../fpf-core/references/E.4-ecosystem-family.md`
>   → `../fpf-core/references/E.17-multi-view.md`

---

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

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `EWA.SkillAsFrameworkCarrier` | `EWA.MonolithInSkill` | Carrier selection предписывает размещение монолита в `assets/` |
| `EWA.MonolithInSkill` | `EWA.SkillDispatcher` | Монолит — source для references; SKILL.md — routing к ним |

---

> **Source:** `assets/FPF-Ecosystem-Workspace-dpf.md` lines L227-L261
