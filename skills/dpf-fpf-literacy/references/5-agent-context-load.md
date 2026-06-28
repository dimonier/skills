# FPFLIT.AgentContextLoad: Загрузка предметного знания AI-агенту

> **Trigger:** Перед постановкой содержательной задачи AI-агенту в конкретной предметной области
> **Governing patterns:** 
>   → `../fpf-core/references/C.11-bounded-context.md`
>   → `../fpf-core/references/E.16-agent-roles.md`
>   → `../fpf-core/references/E.4-ecosystem-family.md`
>   → `../fpf-core/references/E.17.EFP-first-entry.md`

---

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | AI-агент даёт «беззубые» ответы — вероятностно «стреляет по площадям», не знает, что в данной предметной области считается сильным ходом, а что — недопустимой ошибкой |
| **ContextGrounding** | Инженер-менеджер работает с AI-агентом в контексте конкретной предметной области; агент имеет доступ к «всему интернету», но не знает, какие из множества подходов являются SoTA для данной области |
| **ScopeCut** | Загрузка FPF + DPF как контекста для агента; не охватывает тонкую настройку модели (fine-tuning) |
| **NotWishReason** | «Агент сам разберётся, он же умный» — игнорирование того, что «в интернете» хорошим мышлением считается и астрология, и аристотелевская логика, и промпт-инженерия вперемешку |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Практикум: агент с FPF принципиально меняет характер ответов — от «попсовых» к инженерно-обоснованным; без FPF агент склонен «понравиться», а не решить задачу |
| **EntityOfConcern** | Контекст AI-агента — многоуровневая память: FPF (уровень надёжности решения в коллективной работе), DPF (уровень знаний предметной области), LPF (уровень организации) |
| **SymptomDetection** | Агент предлагает решения, которые «верны для других, но неверны для вас»; агент использует подходы, признанные устаревшими или ошибочными в данной предметной области |
| **ProblemHypothesis** | Агент не получил явных границ допустимого — он не знает, что вы не астролог и не маркетолог, которому нужно «настроение», а не точность |
| **ImprovementCheck** | После загрузки FPF+DPF агент: (1) отсекает non-admissible ходы, (2) указывает на SoTA-решения, (3) предупреждает о типовых ошибках, (4) спрашивает о локальных ограничениях (LPF), а не сочиняет уверенные рекомендации |
| **AcceptanceCriterion** | Агент использует FPF-паттерны как governing patterns; агент ссылается на DPF problem cards при обосновании хода; агент различает, что решено на уровне DPF, а что требует локального решения (LPF) |
| **MandatoryConstraints** | Запрещено давать агенту DPF без FPF — DPF всегда depends on FPF Core; запрещено заменять чтение DPF человеком на «пусть агент сам читает» без понимания человеком содержания DPF |
| **CharacterizationRelation** | Response specificity (насколько ответ предметно-специфичен), SoTA alignment (соответствие принятым в области решениям), error prevention (предупреждение типовых ошибок) |
| **ValidationBoundary** | A/B тест: один и тот же вопрос агенту без DPF и с DPF — сравнение ответов по characterization criteria |
| **FreshnessOrExpiry** | `stale` при обновлении DPF или смене модели агента |
| **ProblemFormulationFollowUpReason** | Принципиально ограничить агента — из «умного попсовика» сделать инженера, знающего правила предметной области |
| **ReadinessDisposition** | `P2W-ready` для загрузки контекста перед постановкой задачи |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Bounded context и его границы | `C.11` |
| Agent role и responsibility | `E.16` |
| Context engineering levels | `E.4` (framework ecosystem) |
| Intended reader specification | `E.17.EFP` |

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `FPFLIT.VanillaVsFPF` | `FPFLIT.AgentContextLoad` | Различение типов ответов — предпосылка для правильной загрузки контекста |
| `FPFLIT.FrameworkEcosystemPlacement` | `FPFLIT.AgentContextLoad` | Уровень экосистемы определяет, какой контекст загружать агенту |
| `FPFLIT.AgentContextLoad` | `FPFLIT.SoTARecognition` | Загрузка контекста — условие для распознавания агентом SoTA-решений |
| `FPFLIT.DPFImprovementCycle` | → *all pattern cards* | Цикл улучшения применим к каждой problem card DPF |

---

> **Source:** `assets/FPF-Literacy-dpf.md` lines L260-L296
