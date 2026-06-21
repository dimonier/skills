# Journal — Q registry cross-reference with meeting analyses

**Purpose:** record that during the analysis of a **specific** `processed.md`, the agent held the active registry from [`../open-questions.md`](../open-questions.md) in context and performed a cross-reference (not "iterating through all Qs later in a separate pass").

## How to add a row

After publishing or updating `meetings/.../processed.md`:

1. Fill in the **"Q Registry Cross-Reference"** section in that `processed.md` (see [`meetings/_template.md`](../meetings/_template.md)).
2. Add **one** row to the table below.

| processed (path from `project-vault/`) | review_at (ISO date) | scope | q_with_signal (ids or `—`) | note (1 line) |
|----------------------------------------|----------------------|-------|-------------------------------|---------------------|

- **scope**: `all_active` — context contained **all** rows with `status: open` from `open-questions.md`; `subset` — only a portion (acceptable under emergency context compression; then list `subset_ids` in the note and prioritize a **full** cross-reference at the next source).
- **q_with_signal**: comma-separated list of **`Q-YYYY-…`** for which this source yielded a **verifiable** shift toward an answer (including partial); if no signal — `—`.

## How to find questions "not yet checked for closure" against new sources

There is no strict mathematical "coverage × Q set" in the table — avoid unnecessary bookkeeping. Working heuristics:

1. **High priority:** a Q in [`open-questions.md`](../open-questions.md) has this **same** meeting or an earlier line in the **sources** column, and the **latest** `processed.md` after that date has **no** mention of this `id` in the cross-reference section → needs an explicit pass at the next analysis.
2. **Artifact search:**  
   `rg 'Q-YYYY-NNNN' project-vault/meetings` — if the id appears only in general text but has never appeared in cross-reference / closure note sections, consider it a candidate for review.
3. **Watermark:** the last row **below** in the table with `scope: all_active` — everything added to the registry **after** that analysis date must be cross-referenced at the **very first** next suitable `processed` or briefing.

When a question is closed, the row is removed from `open-questions.md`; past rows in this journal should not be changed.
