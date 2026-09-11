---
id: ASB.SecurityAndTrust
title: "Security & trust: scripts as attack surface, third-party skills"
status: seed
keywords: [security, trust, attack-surface, third-party, awesome-lists, allowed-tools, permission]
dependencies:
  builds_on:
    - E.5.3
    - C.33
---

## ASB.SecurityAndTrust - Security & trust: scripts as attack surface, third-party skills

> **Trigger:** When installing a third-party skill, adding `scripts/` to a skill, or deciding how much to trust a downloaded skill bundle.
> **Governing patterns:**
>   → `AS.11` (Security & Trust — the AS-DPF pattern this card specializes)
>   → `E.5.3` (guard-rails)
>   → `C.33` (carrier admission — third-party carriers)
> **Skill dependencies:**
>   → none

---

### ASB.SecurityAndTrust:1 - Problem frame

Use this pattern as a guard-rail: treat every bundled script as code that runs with
the agent's permissions and every third-party skill as an untrusted carrier to be
studied, not installed wholesale.

### ASB.SecurityAndTrust:2 - Problem

Downloading an "awesome-agent-skills" repository installs foreign workflows with
unknown provenance and a live scripts attack surface; the agent then runs that code
with its own permissions. Bulk installation also adds noise to skill selection
(more skills → harder to pick the right one) and worsens triggering accuracy.

### ASB.SecurityAndTrust:3 - Forces

| Force | Settlement |
|---|---|
| Reuse vs trust | Learn from third-party skills; write your own; install only base utilities. |
| Convenience vs attack surface | Every script is an attack surface; install selectively. |
| Breadth vs selection accuracy | More installed skills worsen skill selection and triggering. |
| Capability vs permission | Bound scripts by the target agent's permission model / `allowed-tools`. |

### ASB.SecurityAndTrust:4 - Solution

1. **Do not bulk-install.** Treat awesome-lists as study material: learn patterns,
   write your own skills, install only base utilities (official Anthropic skills,
   `agent-browser`).
2. **Treat bundled scripts as an attack surface.** A skill with `scripts/` runs code
   with the agent's permissions — review before use; prefer skills whose scripts you
   can read and trust.
3. **Be selective with global skills** (`ASB.Placement`): install only what you trust
   and need daily.
4. **Constrain capability.** Where the target agent supports it, bound a skill's
   scripts/tools via its permission model or `allowed-tools`.
5. **Record provenance.** When a third-party carrier is used as evidence, state
   captured structure, lost structure, admissible use, and the return owner (`G.2`,
   `C.33`); verify currency (`G.11`).
6. **No legal/security verdict for third-party code** — route such claims to the
   agent product's own permission model and to `G.11`.

### ASB.SecurityAndTrust:5 - Archetypal Grounding

**Show.** A downloaded skill ships `scripts/sync.sh` that exfiltrates environment
variables. A first pass had installed it globally "to try". Repair: remove it, study
its structure, and re-author the useful procedure with a reviewed script; constrain
the new script via `allowed-tools`.

### ASB.SecurityAndTrust:6 - Bias-Annotation

The temptation is convenience: "install the whole list and move on", treating a large
skill library as maturity. The counterweight is that each script is an attack surface
and each extra skill degrades selection. Study, re-author, install selectively.

### ASB.SecurityAndTrust:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-ST.1 | No bulk install of awesome-lists; third-party skills are studied, not installed wholesale. |
| CC-ST.2 | Bundled scripts are treated as an attack surface and reviewed before use. |
| CC-ST.3 | Global skills are installed selectively (trusted, daily-used). |
| CC-ST.4 | Where supported, scripts/tools are bounded by the agent's permission model / `allowed-tools`. |
| CC-ST.5 | Third-party carrier use records captured/lost structure, admissible use, and return owner. |

### ASB.SecurityAndTrust:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Downloading awesome-lists wholesale | Study patterns; write your own; install base utilities only. |
| Running unreviewed `scripts/` | Review the script; treat it as an attack surface. |
| Many global skills "just in case" | Install selectively; each is an attack surface and selection noise. |
| Fake security verdict on third-party code | Route to the agent's permission model and `G.11`. |

### ASB.SecurityAndTrust:9 - Consequences

Selective trust keeps the agent's execution surface small and skill selection sharp,
at the cost of re-authoring useful procedures yourself and reviewing scripts. It
trades convenience for control.

### ASB.SecurityAndTrust:10 - Rationale

`AS.11` fixes scripts-as-attack-surface and third-party trust; `E.5.3` frames this as
a guard-rail; `C.33` treats a third-party bundle as a carrier whose structure is
captured, not adopted. The framework issues no legal/security verdict.

### ASB.SecurityAndTrust:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` Anti-Pattern "Downloading Awesome Lists" + security note | Adopt | Study-don't-install, selective global install, attack surface | Reopen on a skill-payload edition change |
| AS-DPF `AS.11` Security & Trust | Adopt | Permission gating, carrier provenance, no verdict | Reopen on `AS.11` revision |
| cool-repo "awesome-agent-skills" as install-and-go | Reject as architecture | Studied as patterns; not installed wholesale | Reopen if provenance/quality guarantees emerge |

Best-known line: study third-party skills, install selectively. Rejected rival:
"bulk-install awesome-lists" — rejected as a foreign workflow + attack surface.

### ASB.SecurityAndTrust:12 - Relations

- **Builds on (DPF):** `AS.11` (security & trust).
- **Builds on (FPF):** `E.5.3` (guard-rails), `C.33` (carrier admission).
- **Coordinates with (DPF):** `AS.9` (global placement security surface).
- **Coordinates with (LPF):** `ASB.Placement` (selective global install is stated in both).

### ASB.SecurityAndTrust:End
