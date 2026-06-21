### 1. Structure

```text
project-vault/
  README.md
  index.md
  state/
  meetings/
  transcripts/raw/
  inputs/briefings/
  decisions/
  work/
  vocabulary/
  reports/
  scripts/
  dependencies.md
  risks.md
  contradictions.md
  open-questions.md
  agenda-next.md
```

### 2. Key files and folders

| Path | Purpose |
|------|---------|
| `README.md` | Rules for structuring and maintaining the entire vault. |
| `index.md` | Main index and entry point into the vault. |
| `state/` | Canonical current project state. |
| `meetings/` | Analyzed meetings and their indices/templates. |
| `transcripts/raw/` | Raw transcripts as primary source material. |
| `inputs/briefings/` | Short entries from chat or from the owner. |
| `decisions/` | Key decision cards and their statuses. |
| `work/` | Working contour: tasks, questions, backlog. |
| `vocabulary/` | Project glossary of terms. |
| `reports/` | Derived summaries and reports. |
| `scripts/` | Utility scripts for vault maintenance. |
| `dependencies.md` | Registry of dependencies and blockers. |
| `risks.md` | Risk registry. |
| `contradictions.md` | Registry of contradictions. |
| `open-questions.md` | List of active open questions. |
| `agenda-next.md` | Next meeting agenda. |

### 3. General `.md` layout

Most `.md` files consist of two parts: YAML frontmatter at the top with fields like `id`, `status`, `updated`, `sources`, and regular Markdown below following a template. YAML is for machine-readable traceability; Markdown is for substantive description.
