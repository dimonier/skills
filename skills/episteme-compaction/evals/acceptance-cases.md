# Acceptance Cases (dev-only test fixtures)

> Not part of the edition; not loaded at runtime. Referenced from `references/relations.md` (refresh route) and the `E.4.DPF.DA` first-repair disposition.

Heterogeneous probes to test the pattern set across unlike rendering situations.

| # | Case | Consumer | Formality | Typical sections | Bracketed | Anti-case (what to reject) |
|---|---|---|---|---|---|---|
| 1 | Diagnostic output | AI agent | F4-F5 | RootCause, Trigger, Path, Fix | [reasoning], [evidence] | Bare assertion without evidence anchors or ADI cycle |
| 2 | Architecture Decision | AI agent, FPF-literate human | F4-F5 | Decision, Context, Rationale, Tradeoffs | [assurance], [evidence] | Unmarked "probably" instead of F-G-R-CL tuple |
| 3 | Hybrid Status | Mixed (agent + human PM) | F3 hybrid | Progress, Done, InProgress, Blocked, Overall | none | Plain text contradicts or broadens episteme block; episteme notation leaks into plain summary |
| 4 | Strict-Distinction Repair | Agent generating episteme notation | F4-F5 | — | — | Episteme-agency: "the analysis concluded" without acting System#Role:Context |
| 5 | Round-Trip Stability | Three agents, no shared state | F4-F5 | Source-derived sections | [aggregation] | Metadata leakage in prose (F_eff, R_eff, Quintet, emergence); [confidence]/[pending] markers in prose; fpfMetadata drift in Episteme₂ |
| 6 | Non-Aggregatable Source | Agent receiving pattern body | F4-F5 | Source-derived sections | none | Fabricated [evidence], [assurance], [aggregation], [reasoning]; only 1-2 claims preserved |

Test method: apply ECPF.1 → ECPF.6 sequentially per case. Verify output against case-specific anti-case patterns. Expected verdict per ECPF.6: admitted or requires-repair with named repair action.
