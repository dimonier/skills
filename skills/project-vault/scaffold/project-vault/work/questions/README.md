# Questions — layout

## Active vs closed

- **Active (open)** — only rows with `open` status in the root file [`../../open-questions.md`](../../open-questions.md).
- **Closed** — one file per question in [`closed/`](closed/), name: `Q-YYYY-NNNN.md`.

## Cheap close workflow (agent)

1. Ensure the answer is **verifiable** in `meetings/.../processed.md` or `inputs/briefings/*.md` (or `decisions/` when `accepted`).
2. Create `closed/Q-YYYY-NNNN.md` from the template `assets/open-question-resolved.md` (skill root) or from [`closed/_template.md`](closed/_template.md).
3. Fill at minimum: `resolved_by`, `knowledge_refs`, if applicable `claim_type` (see "Knowledge confidence level in vault" section in [README](../../README.md)).
4. Delete the row from the active table in `open-questions.md`; update `updated` in `open-questions.md` frontmatter.

**Knowledge** — 1–3 bullets in the closure card **or** just `knowledge_refs`, if the wording already exists in `state/` / `vocabulary/` / `decisions/`.
