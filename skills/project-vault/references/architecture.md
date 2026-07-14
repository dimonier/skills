### 1. Structure

```text
project-vault/
  README.md
  state/
  sources/
    _index.md
    _digest-template.md
    captures/
    digests/
  decisions/
  risks/
  open-questions/
  contradictions/
  events/
  archive/
  work/
  vocabulary/
  reports/
  scripts/
  dependencies.md
  agenda-next.md
```

### 2. Key Files and Directories

| Path | Purpose |
|------|---------|
| `README.md` | Rules for vault structure and maintenance. |
| `state/` | Canonical current project state. |
| `sources/` | Captured originals and short analysis digests. Unified index — `sources/_index.md`, digest templates — `templates/digest-meeting.md` and `templates/digest-dialogue.md`. |
| `sources/captures/` | Captured originals "as-is" (transcripts, articles, pages). |
| `sources/digests/` | Short analysis digests of any sources; links to atomic files. |
| `decisions/` | Atomic decision cards (DEC-NNNN-slug.md) + summary `_index.md`. |
| `risks/` | Atomic risk cards (RISK-NNNN.md) + summary `_index.md`. |
| `open-questions/` | Atomic open question cards (Q-NNNN.md) + summary `_index.md`. |
| `contradictions/` | Atomic contradiction cards (CON-NNNN.md) + summary `_index.md`. |
| `events/` | Event chronicle (YYYY-MM-DD-NN.md) + summary `_index.md`. |
| `archive/` | Mirror structure for closed entities (risks, questions, contradictions, events). |
| `work/` | Working contour: tasks, questions, backlog. |
| `vocabulary/` | Project glossary of terms. |
| `reports/` | Derived summaries and reports. |
| `scripts/` | Utility scripts for vault maintenance. |
| `dependencies.md` | Registry of dependencies and blockers. |
| `agenda-next.md` | Next meeting agenda. |

### 3. General `.md` File Layout

Most `.md` files consist of two parts: YAML frontmatter on top with fields like `id`, `status`, `updated`, `sources`, followed by regular Markdown per template. YAML is for machine-readable traceability; Markdown is for human-readable description.
