---
name: episteme-compaction
description: |
  Lossless compaction of epistemes: prose ↔ compact typed-slot notation (F4-F5,
  ~65% token savings) with a source-claims vs [bracketed] split and
  reconstruction back to source. Use for AI-agent or FPF-literate-human output
  needing token economy and auditability. NOT narrativization. Depends on
  fpf-core.
---

# Episteme Compaction — Dispatcher

**Bounded context:** lossless compaction of epistemes — prose ↔ compact typed-slot notation (F4-F5), governed by the FPF A.6.3 (Epistemic Viewing) family.

This skill is the access-facing carrier bearing the `EpistemeCompactionPrinciplesFramework` edition. The edition is recoverable from `references/` (the canonical pattern bodies). There is no monolith and no separate reader-facing publication form.

## Routing table

| Situation | Load | Governing cues |
|---|---|---|
| Decide formality level (F0 vs F4-F5 vs F3 hybrid) for an output | `references/ECPF.1.md` | C.2.3, A.6.3, A.6.3.CR, A.6.3.CSC |
| Render prose claims as typed slots (the core move) | `references/ECPF.2.md` | A.6.3.RT, A.6.3, E.10.D2, C.2.1, A.6.5 |
| Render Γ aggregation / F-G-R-CL trust metrics | `references/ECPF.3.md` | B.1, B.3, C.2.3 |
| Render evidence provenance / ADI reasoning | `references/ECPF.4.md` | A.10, B.3.4, B.5 |
| Check strict distinctions / category errors | `references/ECPF.5.md` | A.7, A.12, A.14 |
| Evaluate a rendering before admission | `references/ECPF.6.md` | E.21, E.22, E.23 |
| Reconstruct prose from a compact episteme (reverse render) | `references/ECPF.7.md` | A.6.3.RT, A.6.3.CR, A.6.3.CSC, A.6.3.NAR, E.17.EFP |
| Govern the episteme↔prose round-trip / drift | `references/ECPF.TG.md` | A.6.3 |

## Navigation rule

The dominant chain is a rendering pipeline: start at `references/ECPF.1.md` (formality gates everything), then `references/ECPF.2.md` (the core typed-slot render), then `references/ECPF.3.md` / `references/ECPF.4.md` for aggregation/trust and evidence/reasoning, then `references/ECPF.5.md` for distinction compliance, closing with `references/ECPF.6.md` for admission. For the reverse direction (notation → prose), load `references/ECPF.7.md`; load `references/ECPF.TG.md` when the round-trip across passes must stay drift-free. The full pattern index is `references/INDEX.md`; source/edition citation and the dependency graph are `references/relations.md`.

## Single surface

`references/*.md` is canonical. No `assets/` monolith and no "generated → do not edit" projection exists; `SKILL.md` (this file) is routing-only.
