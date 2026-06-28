---
name: dpf-lfw-architecture
description: |
  LFW Architecture. Use when: organizing the FPF/DPF/LPF workspace, deciding where
  to place a new framework, setting up the skill-carrier structure, or resolving
  LPF vs Project boundary questions. Depends on fpf-core.
---

# DPF: Layered Framework Workspace Architecture

**Governed value:** `LayeredFrameworkWorkspace` (LFW)
**Depends on:** `fpf-core`, `dpf-fpf-literacy`
**Bounded context:** FPF ecosystem @ AI-assisted work environment
**Source of truth:** `assets/FPF-Ecosystem-Workspace-dpf.md`

## When to load each pattern

| Situation | Load | Governing cues → fpf-core |
|---|---|---|
| Packaging a DPF/LPF as a skill | `references/1-skill-as-carrier.md` | E.4.DPF, C.33 |
| Placing a monolith inside a skill | `references/2-monolith-in-skill.md` | C.33, E.17.EFP |
| Building a dependency chain | `references/3-dependency-chain.md` | E.5.3, E.4 |
| SKILL.md as a dispatcher (routing-only) | `references/4-skill-dispatcher.md` | C.33, E.4.DA |
| Project-level AGENTS.md (what to put in it) | `references/5-project-context.md` | FPFLIT.AgentContextLoad |
| Distinguishing LPF from Project | `references/6-lpf-vs-project.md` | E.4, E.5.3 |

## Source for agent vs human

- **Agent**: always use `references/`. DO NOT read `assets/FPF-Ecosystem-Workspace-dpf.md`.
- **Human**: read and edit the canonical monolith `assets/FPF-Ecosystem-Workspace-dpf.md`. After edits — rebuild `references/`.

## references/ status

**Ready** — 6 problem cards + INDEX + relations.
