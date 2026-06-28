---
name: dpf-fpf-literacy
description: |
  FPF Literacy & DPF Authoring. Use when: helping an agent understand the FPF/DPF/LPF
  stack, creating a new DPF, loading domain knowledge into an agent, distinguishing
  FPF-grounded answers from generic AI responses, or choosing a carrier for publication.
  Depends on fpf-core.
---

# DPF: FPF Literacy & DPF Authoring

**Depends on:** `fpf-core` (all governing-pattern cues reference FPF Core)
**Bounded context:** AI-assisted engineering and management work grounded in FPF
**Source of truth:** `assets/FPF-Literacy-dpf.md`

## When to load each pattern

| Situation | Load | Governing cues → fpf-core |
|---|---|---|
| Agent gives a "nice but useless" answer | `references/1-vanilla-vs-fpf.md` | C.22.2, E.17, A.10 |
| Team confuses FPF/DPF/LPF levels | `references/2-ecosystem-placement.md` | B.2, C.11, E.4.PFAD |
| Time is wasted on clearly unsuitable options | `references/3-move-exclusion.md` | E.8, G.2, A.21 |
| Need to draft a DPF in one hour | `references/4-first-hour-route.md` | E.4.DPF, C.22.2, C.33 |
| Agent doesn't know the domain | `references/5-agent-context-load.md` | C.11, E.16, E.4 |
| Need to improve an existing DPF | `references/6-improvement-cycle.md` | E.22, E.21, E.23, E.19 |
| Agent proposes a mainstream/shallow solution | `references/7-sota-recognition.md` | G.2, C.22.2, A.10 |
| Choosing whether to publish in a file or in chat | `references/8-carrier-first-entry.md` | C.33, E.17.EFP |
| Need a map of relationships between patterns | `references/relations.md` | E.4.PFR |

## Navigation rule

First load `references/2-ecosystem-placement.md` — it determines which level
(FPF/DPF/LPF) the problem belongs to. Then load the specific pattern.

## Source for agent vs human

- **Agent**: always use `references/`. DO NOT read `assets/FPF-Literacy-dpf.md`.
- **Human**: read and edit the canonical monolith `assets/FPF-Literacy-dpf.md`. After edits — rebuild `references/`.

## references/ status

**Ready** — 8 problem cards + INDEX + relations.
