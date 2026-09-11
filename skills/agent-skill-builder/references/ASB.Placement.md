---
id: ASB.Placement
title: "Placement & portability: global vs project-local, symlink strategy"
status: seed
keywords: [placement, global, project-local, symlink, portability, security-surface]
dependencies:
  builds_on:
    - E.4
    - E.5.3
    - C.33
---

## ASB.Placement - Placement & portability: global vs project-local, symlink strategy

> **Trigger:** When deciding where a skill should live (global user directory vs project-local) and how to expose one source of truth to several agent products.
> **Governing patterns:**
>   → `AS.9` (Placement & Portability — the AS-DPF pattern this card specializes)
>   → `E.4` (family architecture — where a skill lives in the ecosystem)
>   → `E.5.3` (acyclicity)
>   → `C.33` (carrier admission)
> **Skill dependencies:**
>   → none

---

### ASB.Placement:1 - Problem frame

Use this pattern to place a skill so the right audience gets it and one source of
truth feeds every agent that should load it.

### ASB.Placement:2 - Problem

A skill placed globally that is only relevant to one repository taxes every session
of every project; a skill that should be shared but lives project-local is
re-authored (and drifts) per project. Duplicating the skill into several agent
directories forks the single surface.

### ASB.Placement:3 - Forces

| Force | Settlement |
|---|---|
| Global vs project-local | Cross-cutting/base utilities global; framework/deployment specifics project-local. |
| One source vs many agents | One source directory, symlinked into per-agent paths. |
| Portability vs specificity | A portable skill avoids repo-specific facts; repo facts go to `AGENTS.md`. |
| Convenience vs security | Each global skill with scripts is an attack surface — install selectively. |

### ASB.Placement:4 - Solution

**Global skills** (available to all agents / all projects):
- Base utilities: official skills (PDF, XLSX, DOCX, `skill-creator`), `agent-browser`.
- Cross-cutting concerns: `go-packages`, `news-digest`.
- Store in: `~/.agents/skills/`, `~/.claude/skills/`, etc.

**Project-local skills** (specific to one repository):
- Framework patterns (`model`, `migration`, `controller` for Laravel).
- Architecture documentation (outbox pattern, CQRS, error handling).
- Deployment procedures.
- Store in: `<project>/.claude/skills/`, `<project>/.codex/skills/`.

**Symlink strategy (recommended).** Keep one source directory and symlink it into
each per-agent path:

```text
~/.agents/skills/           # source of truth
~/.claude/skills/           → symlink to ~/.agents/skills/
~/.codex/skills/            → symlink to ~/.agents/skills/
```

Some agents (e.g. opencode) natively read multiple directories — check their
documentation before symlinking.

**Security.** Be selective with global skills: each skill with scripts is an attack
surface; install only what you trust and need daily (`ASB.SecurityAndTrust`).

**Portability.** Keep repo-specific facts out of a portable skill; route them to
`AGENTS.md` (`ASB.Atomicity`, `ASB.LayerRouting`).

### ASB.Placement:5 - Archetypal Grounding

**Show.** A global `pdf` skill (base utility, useful in every project) vs a
project-local `outbox-pattern` skill (architecture doc relevant only to one
repository). The global skill lives once and is symlinked into each agent directory;
the project-local skill lives in the repository's own skills directory.

### ASB.Placement:6 - Bias-Annotation

The temptation is to make everything global ("so it is always available"), which
multiplies the security surface and loads irrelevant context; the symmetry is to
duplicate a skill into several agent directories, forking the single surface. One
source + symlinks, and role-based placement, are the counterweights.

### ASB.Placement:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-PL.1 | Global vs project-local is chosen by audience and portability. |
| CC-PL.2 | One source directory; per-agent paths are symlinks (or native multi-dir read), not copies. |
| CC-PL.3 | Repo-specific facts are not baked into a portable skill. |
| CC-PL.4 | Global skills with scripts are installed selectively (security surface considered). |

### ASB.Placement:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Everything global | Keep project-specific skills project-local. |
| Copying a skill into several agent dirs | One source + symlinks. |
| Repo facts inside a portable skill | Move them to `AGENTS.md`. |
| Bulk-installing global skills | Install only trusted, daily-used skills. |

### ASB.Placement:9 - Consequences

Correct placement keeps always-loaded context and the security surface lean while one
source feeds every agent, at the cost of maintaining symlinks and per-product
discovery rules. Portability requires keeping repo facts out of the skill.

### ASB.Placement:10 - Rationale

`AS.9` fixes placement by audience and portability; `E.4`/`E.5.3` place skills as
family artifacts with a unidirectional dependency; `C.33` treats each installed
location as a carrier returning to the single source. Symlinks preserve one
authoritative surface.

### ASB.Placement:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` "Placement Guide" (global vs project-local, symlink strategy) | Adopt | Placement table, symlink layout, security note | Reopen on a skill-payload edition change |
| AS-DPF `AS.9` Placement & Portability | Adopt | Audience-based placement, one-source discipline | Reopen on `AS.9` revision |
| opencode multi-directory skill loading | Adopt | "Check the product's discovery rules before symlinking" | Reopen on a product-discovery change |

Best-known line: one source, symlinked outward. Rejected rival: "duplicate into every
agent directory" — rejected as a forked single surface.

### ASB.Placement:12 - Relations

- **Builds on (DPF):** `AS.9` (placement).
- **Builds on (FPF):** `E.4` (family architecture), `E.5.3` (acyclicity), `C.33` (carrier admission).
- **Coordinates with (DPF):** `AS.11` (security surface of global skills).
- **Coordinates with (LPF):** `ASB.SecurityAndTrust` (selective global install is stated in both).

### ASB.Placement:End
