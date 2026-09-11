---
id: ASB.SkillAnatomy
title: "Skill anatomy & bundled resources: folder layout and frontmatter"
status: seed
keywords: [anatomy, folder-structure, frontmatter, scripts, references, templates, assets, naming]
dependencies:
  builds_on:
    - C.33
    - F.18
    - E.10
---

## ASB.SkillAnatomy - Skill anatomy & bundled resources: folder layout and frontmatter

> **Trigger:** When scaffolding a new skill folder, or deciding which files it must/may contain and how to name them.
> **Governing patterns:**
>   → `AS.5` (Skill Anatomy & Bundled Resources — the AS-DPF pattern this card specializes)
>   → `C.33` (carrier admission)
>   → `F.18` (naming)
>   → `E.10` (kind discipline)
> **Skill dependencies:**
>   → `create-agent-skill` (skill anatomy)

---

### ASB.SkillAnatomy:1 - Problem frame

Use this pattern to lay out a skill folder: the mandatory `SKILL.md`, its YAML
frontmatter, and the optional bundled resource directories — each with a distinct
role.

### ASB.SkillAnatomy:2 - Problem

The folder drifts into two failures: an over-full folder that carries empty
`scripts/`/`templates/` "for completeness", and a mis-shaped folder whose resource
roles are confused (docs in `assets/`, output skeletons in `references/`). Frontmatter
also drifts: `name`/`description` missing, or fields the loader does not allow.

### ASB.SkillAnatomy:3 - Forces

| Force | Settlement |
|---|---|
| Required vs optional | `SKILL.md` is mandatory; `scripts/`, `references/`, `templates/`, `assets/` appear only when used. |
| Kind distinction | Each directory has one role; do not blur resources across kinds (`E.10`). |
| Naming vs portability | Kebab-case names; the folder name matches the skill's `name`. |

### ASB.SkillAnatomy:4 - Solution

**Folder layout.**

```text
my-skill/
├── SKILL.md              # YAML frontmatter + instructions (mandatory)
├── scripts/              # executable code (Python, Bash) — run, not loaded
├── references/           # docs loaded on demand (troubleshooting, deep dives)
├── templates/            # output templates, config skeletons
└── assets/               # files used in output (logos, fonts, boilerplate)
```

**`SKILL.md` frontmatter.**

```yaml
---
name: my-skill
description: |
  Clear, concise description of what the skill does and when to use it.
  This is the primary trigger — the agent reads only `name` + `description`
  until it decides to load the full skill.
---
```

- `name` — kebab-case, ≤64 chars, matches the folder name.
- `description` — WHAT + WHEN (≤1024 chars); the trigger, not a summary
  (`ASB.TriggerDesign`).
- Additional fields (e.g. `license`, `allowed-tools`, `metadata`, `compatibility`)
  only if the target loader's schema allows them.

**Resource roles (each directory = one kind).**
- `scripts/` — deterministic/repetitive steps, validators, generators.
- `references/` — deep docs loaded into context on demand.
- `templates/` — output skeletons and config templates.
- `assets/` — static files used in output.

**Proportionality.** Add a resource directory only when a real task needs it; empty
scaffolding is not added for completeness.

### ASB.SkillAnatomy:5 - Archetypal Grounding

**Show.** A `migration` skill: `SKILL.md` (procedure + when to run the generator),
`scripts/generate_migration.py` (deterministic emitter), `templates/migration.php.tpl`
(output skeleton), `references/framework-conventions.md` (deep conventions),
`assets/` absent (nothing used in output). Every folder is present because a task
needs it.

### ASB.SkillAnatomy:6 - Bias-Annotation

The temptation is **apparatus for completeness**: empty `scripts/`/`templates/` that
look mature but add maintenance surface without a task (`E.4.DPF:4`). The symmetry
is misplacing content — docs in `assets/`, output in `references/` — which breaks the
kind roles. Proportionality and one-role-per-directory are the counterweights.

### ASB.SkillAnatomy:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-SA.1 | `SKILL.md` is present with YAML frontmatter (`name`, `description`). |
| CC-SA.2 | `name` is kebab-case (≤64 chars) and matches the folder name; `description` follows `ASB.TriggerDesign`. |
| CC-SA.3 | Each resource directory present has one role: `scripts/`, `references/`, `templates/`, `assets/`. |
| CC-SA.4 | No empty resource directory is added for completeness. |
| CC-SA.5 | Frontmatter contains no fields the target loader disallows. |

### ASB.SkillAnatomy:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Empty `scripts/`/`templates/` for completeness | Add only when a real task needs it. |
| Docs in `assets/` or output in `references/` | Restore the one-role-per-directory mapping. |
| Missing `name`/`description` | Add both; they are the load contract. |
| Folder name diverging from `name` | Align them (kebab-case). |

### ASB.SkillAnatomy:9 - Consequences

A clean layout makes the skill portable across loaders and keeps the artifact kinds
distinct, at the cost of choosing (and justifying) each resource directory. Naming
and carrier discipline (`F.18`, `C.33`) keep the artifact addressable.

### ASB.SkillAnatomy:10 - Rationale

`AS.5` fixes the folder anatomy and frontmatter schema; `C.33` treats the folder as
the access-facing carrier; `F.18` fixes kebab-case naming; `E.10` keeps resource
kinds distinct. Proportionality (`E.4.DPF:4`) forbids empty scaffolding.

### ASB.SkillAnatomy:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` "Anatomy of a Skill" + frontmatter | Adopt | Folder tree and `name`/`description` frontmatter | Reopen on a skill-payload edition change |
| AS-DPF `AS.5` Skill Anatomy & Bundled Resources | Adopt | Frontmatter schema, bundled-resource roles | Reopen on `AS.5` revision |
| Anthropic `quick_validate.py` schema (`ALLOWED_PROPERTIES`) | Adopt | Allowed frontmatter fields | Reopen on a schema-rule release |

Best-known line: mandatory `SKILL.md` + role-distinct optional resources. Rejected
rival: "empty scaffolding for completeness" — rejected as premature apparatus.

### ASB.SkillAnatomy:12 - Relations

- **Builds on (DPF):** `AS.5` (skill anatomy).
- **Builds on (FPF):** `C.33` (carrier admission), `F.18` (naming), `E.10` (kind discipline).
- **Coordinates with (DPF):** `AS.2` (frontmatter description), `AS.4` (resource load).
- **Specialized by (LPF):** `ASB.ProgressiveDisclosure` (resource roles implement the three levels), `ASB.Placement` (the folder is the thing placed).

### ASB.SkillAnatomy:End
