---
name: fpf-core
description: First Principles Framework core patterns. Use when doing engineering, research, management, or mixed human/AI work. ALWAYS use as governing patterns for any DPF or LPF work. Load individual patterns from references/ as needed — never read the full spec unless doing deep audit.
---

# FPF Core Pattern Library

**Depends on:** nothing (root of dependency chain)
**Source of truth:** `assets/FPF-Spec.md` — canonical specification (103K+ lines)

## How to Use

Do NOT read `assets/FPF-Spec.md` in full. Identify the situation and load the relevant reference:

The table below is a fast index mirroring FPF's 15 canonical practical-use cards (`E.11`). When the situation is ambiguous, start from the entry-point row: load the cards, compare the plausible ones by their first-result difference, then open the direct pattern.

| You are doing... | Load |
|---|---|
| Unsure where to start / picking a pattern for a situation | `_ctx.Practical-Use-Cards.md`, `E.11.md`, `E.11.PUR.md`, `E.11.PUA.md` |
| Developing or reviewing architecture | `C.32.P2S.md`, `C.30.md`, `A.22.md`, `A.22.CGUS.md`, `C.32.md`, `C.32.PAD.md`, `C.32.ADR.md`, `C.33.md`, `C.34.md`, `C.35.md`, `C.30.ASV.md`, `C.30.AD.md`, `C.31.md`, `C.32.CONWAY.md`, `B.2.md`, `B.2.P.md` |
| Writing rules, methods, work-process documents | `A.6.md`, `A.6.B.md`, `A.6.C.md`, `A.15.md`, `A.15.1.md`, `A.15.2.md`, `A.15.3.md`, `A.15.4.md`, `E.18.md`, `E.18.1.md`, `E.18.2.md`, `E.18.3.md`, `E.8.md`, `E.19.md` |
| Comparing alternatives, making a local choice | `A.19.md`, `A.19.ECS.md`, `C.11.md`, `C.18.md`, `C.19.md`, `G.0.md`, `G.5.md` |
| Turning a vague situation into a problem statement | `C.22.2.md`, `C.2.2a.md`, `A.16.md`, `A.16.1.md`, `A.16.2.md`, `B.4.1.md`, `B.5.2.0.md` |
| Defining "better" and running improvement | `A.19.ECS.md`, `E.22.md`, `E.23.md`, `C.16.md`, `C.25.md`, `E.21.md`, `E.9.DA.md`, `E.2.DA.md` |
| Preparing evidence, assurance, gate decisions | `A.10.md`, `B.3.md`, `A.20.md`, `A.21.md`, `C.11.md`, `C.28.md` |
| Checking timing, freshness, rhythm, action windows | `C.27.md`, `A.10.md`, `A.20.md`, `A.21.md`, `C.11.md` |
| Using causal explanations, interventions, model outputs | `C.28.md`, `A.10.md`, `B.3.md`, `A.20.md`, `A.21.md`, `C.11.md` |
| Comparing descriptions, dashboards, explanations, views of the same thing | `E.17.md`, `E.17.0.md`, `E.17.EFP.md`, `A.15.4.md`, `A.7.md`, `C.30.AD.md` |
| Giving things better names | `F.17.md`, `F.18.md`, `F.19.md`, `E.10.md`, `E.10.ARCH.md` |
| Repairing wording in technical documents | `E.10.md`, `E.10.ARCH.md`, `F.18.md`, `F.19.md`, `A.6.P.md`, `C.2.P.md`, `C.16.P.md`, `C.16.Q.md`, `C.30.P.md`, `A.6.F.md`, `A.6.M.md` |
| Deciding whether mathematics / formal modeling would help | `C.29.md`, `A.6.0.md`, `A.6.1.md`, `E.18.1.md`, `C.16.md`, `C.27.md`, `C.30.LCA.md`, `C.30.ILC.md` |
| Building a state-of-the-art or option portfolio | `G.0.md`, `G.1.md`, `G.2.md`, `G.5.md`, `G.10.md`, `G.11.md`, `C.18.md`, `C.19.md`, `A.19.md`, `A.19.ECS.md` |
| Building a domain or local FPF-grounded framework | `E.4.md`, `E.4.PFAD.md`, `E.4.DPF.md`, `E.4.PFR.md`, `G.2.md`, `E.8.md`, `E.11.md`, `E.17.md`, `F.18.md`, `G.11.md` |
| Creating a DPF or LPF | `E.4.DPF.md` |
| Deciding what belongs in Core vs DPF/LPF | `E.4.md` + `E.5.3.md` |
| Recording relations between frameworks | `E.4.PFR.md` |
| Choosing a carrier for publication | `C.33.md` |
| Looking up a pattern by name | `INDEX.md` |
| Audit, deep reference, refactoring | `assets/FPF-Spec.md` (last resort only) |

## Dependency Rule

If a loaded reference links to other FPF patterns (governing-pattern cues),
load those too from `references/`. Each reference lists its own dependencies.

## Source for Agent vs Human

- **Agent**: always use `references/` — the primary source of patterns. Do NOT read `assets/FPF-Spec.md`.
- **Human**: read and edit the canonical monolith `assets/FPF-Spec.md` (source of truth). After edits, run `spec-decomposer` to rebuild `references/`.

## References Status

**Ready** — 295 pattern reference files + INDEX + 36 context sections.
