# Episteme Compaction — Source, Edition, and Relation Records

> **Canonical home.** This file is the canonical home for the source/edition citation
> and the *intra-DPF* dependency graph (edges between `ECPF.*` patterns). FPF-dependency
> edges live in each body's frontmatter `dependencies` (`builds_on`, `coordinates_with`)
> and in the body's "Governing FPF patterns" block — not here.
>
> **Edge direction.** A `From → To` row reads "From depends on / is placed by / follows To".

## Identity and source citation

- **Framework:** `EpistemeCompactionPrinciplesFramework` (Episteme Compaction Principles Framework, ECPF).
- **Edition ref:** `EpistemeCompactionPrinciplesFramework@2026-08-26`.
- **Kind:** Domain Principle Framework (DPF). A specialization of the Narrativization and Narrative Studies DPF (`NSTD.*`) for the FPF language domain.
- **Carrier:** this skill directory (`skill/episteme-compaction/`) is the access-facing carrier bearing the edition; the edition (a `C.2.1` episteme) is recoverable from `references/`.
- **Sources:** FPF Core (`FPF-Spec.md`); Narrativization DPF (`Narrativization-and-Narrative-Studies-Principles-Framework.md`); instruction file `Инструкция_для_ИИ_агента_Полная_FPF_нотация_с_Γ_операторами_и_U.md` (kept in `project-vault/sources/`).
- **Package status:** `beta` — pattern bodies are drafted through `E.8`, structurally complete, marked `source-faithful` (not yet `case-validated`; not field-tested against target models; not reliance-bearing).

## Purpose and non-use boundary

**Purpose.** Govern lossless episteme compaction: the act of replacing free-form prose (F0) with compact, typed, auditable episteme notation (F4-F5) for consumption by AI agents or FPF-literate humans. Every claim keeps its information; the carrier changes from sentences to typed slots.

**Intended users.** AI agents generating compact episteme output for other agents; FPF authors designing or evaluating such output.

**Non-use boundary.** Not FPF Core, not an FPF vocabulary reference, not a general writing guide, not a narratology course, and not evidence or assurance for the claims rendered. The rendered compact episteme is a carrier — the claims it carries are governed by the FPF pattern or evidence source that owns them.

**Distinction from narrativization.** This DPF is a notation compactor, not a storyteller. `NSTD`-narrativization builds a connected narrative (A.6.3.NAR + A.6.3.CSC); this DPF builds a notational episteme (A.6.3.RT with A.6.3.CR/CSC fidelity discipline). Both re-express, but into different target kinds.

## Intra-DPF dependency graph

| From (→) | To | Relation function |
|---|---|---|
| `ECPF.2` | `ECPF.1` | follows — formality is selected before typed-slot rendering |
| `ECPF.3` | `ECPF.2` | follows — slots are typed before aggregation/trust is applied |
| `ECPF.4` | `ECPF.3` | follows — trust metrics reference evidence chains |
| `ECPF.5` | `ECPF.2` | follows — slots are typed before distinctions are checked |
| `ECPF.6` | `ECPF.1`, `ECPF.2`, `ECPF.3`, `ECPF.4`, `ECPF.5` | applies to — quality evaluation covers the compliance of the other five |
| `ECPF.7` | `ECPF.2` | inverse-of — the reverse render (notation → prose), the mirror of the forward typed-slot render |
| `ECPF.TG` | `ECPF.2`, `ECPF.7` | coordinates-with — governs the round-trip boundary over the forward/reverse composition (idempotence) |

The dependency chain is unidirectional (`E.5.3`): `episteme-compaction` → `FPF Core` and `Narrativization DPF` → (nothing upward). This DPF never edits FPF Core.

## Source use and refresh map

| Source | Adopted payload | Rejected or bounded reading | Currentness trigger | Refresh route |
|---|---|---|---|---|
| FPF Core `FPF-Spec.md` | U.-type taxonomy, Γ operators, F-G-R-CL calculus, A.7 distinctions, A.6.3 family, A.10 evidence graph, B.5 ADI cycle | Full FPF vocabulary not rendered — only types used in the bodies are exposed | FPF Core edition change | `G.2` → update U.-type references, Γ flavors, formulas, governing cues |
| Narrativization DPF | NSTD.1-8 pattern structure, narrative quality dimensions, audience analysis | Full narratology theory — this DPF specializes only the rendering concern | Upstream DPF edition change | `G.2` → verify specialization relations still hold |
| Instruction file (see `project-vault/sources/`) | Full episteme notation specification | Instructional framing and Russian-language exposition — rendered as English pattern bodies | File update | Direct source update → body revision |
| `samples/` (repo-level) | Worked F0↔F4-F5 cases and the drift mechanism | — | Sample drift | `E.23` → improve worked cases and TG rules |

## Refresh route

| Trigger | What to refresh | Owner |
|---|---|---|
| FPF Core edition change | Verify U.-type references, Γ flavors, formulas, A.6.3 family, governing cues | `G.2` → update bodies |
| Narrativization DPF edition change | Verify specialization relations in `:12`; check for new NSTD patterns to specialize | `G.2` → update bodies |
| Instruction file update | Update bodies to reflect new notation, templates, or rules | Direct source update |
| Repeated rendering failures in agent use | Improve worked cases, anti-patterns, checklist items | `E.23` |
| Package adequacy evaluation | Full `E.4.DPF.DA` against DPF quality characteristics | `E.22` / `E.4.DPF.DA` |
| Pattern quality evaluation | Individual `E.21` evaluation of each `ECPF.*` body | `E.21` |
| New FPF pattern affecting rendering | Decide new `ECPF.*` pattern vs Solution update | `E.4.PFAD` |
| Target-model capability change | Verify templates, rules, self-check still hold for target model size | `E.23` |
| episteme↔prose semantic drift in field use | Verify TG-1/TG-2; add reconstruction examples | `E.23` |

Acceptance cases (heterogeneous probes across diagnostic, ADR, hybrid-status, distinction-repair, round-trip, and non-aggregatable-source cases) are dev-only fixtures in `evals/acceptance-cases.md`.
