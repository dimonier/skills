"""
Export DEC decision cards from a project-vault/ directory to an external folder.

By default only `decision_type: adr` cards are exported; use `--type` to select
other types or `--type all` to disable the type filter.

For every card in `decisions/DEC-*.md` the script:

0. Keeps only cards whose `decision_type` matches the requested types (default
   `adr`). Cards of other types are silently filtered out.

1. Strips the YAML frontmatter down to a fixed allow-list of fields:
     id, title, updated, status, decision_owner, decision_date,
     evidence_captured_at, characteristic, supersedes, superseded_by,
     related_decisions
   Fields outside this set (sources, source_kind, references, linked_tasks,
   decision_type, fpf_kind, intended_readers, publication_carrier, revisit_by,
   review_by, ...) are removed. A field that is absent is simply not added.

2. Checks the *resulting* card (filtered frontmatter + body) for references to
   internal entities by ID prefix. Only references to other DEC- cards are
   allowed. Any other entity ID prefix (Q-, RISK-, CON-, TRK-, WRK-, TASK-, FR-,
   INV-) causes the card to be SKIPPED with a warning, so internal entities never
   leak into the external copy.

Usage:
  python export_dec.py --output "D:/path/to/external/folder"
  python export_dec.py --output "D:/out" --path "D:/path/to/project-vault"
  python export_dec.py --output "D:/out" --id DEC-0139
  python export_dec.py --output "D:/out" --id DEC-0030 --id DEC-0139
  python export_dec.py --output "D:/out" --type process
  python export_dec.py --output "D:/out" --type adr,strategy
  python export_dec.py --output "D:/out" --type all
  python export_dec.py --output "D:/out" --dry-run

The optional `--path` (or `-p`) argument points at the project-vault directory
(the one containing `decisions/`). When omitted, the script assumes it lives at
`<vault>/scripts/` and uses its parent directory.

`--id` (repeatable) exports only the listed cards instead of all of them.

`--type` (or `-t`) filters by `decision_type` (comma-separated; `all` disables
the filter). Default: `adr`.

`--dry-run` reports what would be exported/skipped without writing anything.
"""

import os
import re
import sys
import argparse

import yaml

OUTPUT_ENCODING = 'utf-8'

# Frontmatter fields kept on export (original file order is preserved).
ALLOWED_FIELDS = (
    'id',
    'title',
    'updated',
    'status',
    'decision_owner',
    'decision_date',
    'evidence_captured_at',
    'characteristic',
    'supersedes',
    'superseded_by',
    'related_decisions',
)

# Internal entity ID prefixes. A DEC card may reference only other DEC- cards,
# so any of these prefixes followed by a digit is a leak of an internal entity.
NON_DEC_ENTITY_PREFIXES = ('Q', 'RISK', 'CON', 'TRK', 'WRK', 'TASK', 'FR', 'INV')

# Web links are allowed (guardrail 14); mask them before scanning so a URL that
# happens to contain an entity-like token does not produce a false hit.
URL_RE = re.compile(r'\b(?:https?|ftp)://[^\s)\]"\']+', re.IGNORECASE)

ENTITY_ID_RE = re.compile(
    r'\b(?:' + '|'.join(NON_DEC_ENTITY_PREFIXES) + r')-[0-9][0-9A-Za-z-]*'
)


def resolve_vault_dir(cli_path):
    """Return the project-vault directory (the one containing decisions/)."""
    if cli_path:
        return os.path.abspath(cli_path)
    # Default: the script sits in <vault>/scripts/ (deployed copy).
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(script_dir, '..'))


def parse_frontmatter(content):
    """Split markdown content into (frontmatter dict, body text)."""
    if not content.startswith('---\n') and not content.startswith('---\r'):
        return {}, content
    m = re.match(r'^---\r?\n(.*?)\r?\n---', content, re.DOTALL)
    if not m:
        return {}, content
    fm_text = m.group(1)
    body = content[m.end():]
    try:
        # BaseLoader keeps all scalar values as strings (dates stay strings).
        fm = yaml.load(fm_text, Loader=yaml.BaseLoader) or {}
    except yaml.YAMLError:
        fm = {}
    if not isinstance(fm, dict):
        fm = {}
    return fm, body


def filter_frontmatter(fm):
    """Keep only allowed fields, preserving original file order."""
    return {k: fm[k] for k in ALLOWED_FIELDS if k in fm}


def render_card(fm, body):
    """Serialize filtered frontmatter + body back into a markdown document."""
    yaml_text = yaml.safe_dump(
        fm, allow_unicode=True, sort_keys=False, default_flow_style=False
    )
    body = body.strip('\r\n').strip()
    return '---\n' + yaml_text + '---\n\n' + body + '\n'


def find_internal_references(text):
    """Return a list of (kind, matched_text) internal references in `text`."""
    findings = []
    scrubbed = URL_RE.sub(' ', text)
    for m in ENTITY_ID_RE.finditer(scrubbed):
        findings.append(('internal-entity-id', m.group(0).rstrip('-')))
    return findings


def list_dec_files(vault_dir):
    """Return sorted DEC-*.md filenames from <vault>/decisions/."""
    decisions_dir = os.path.join(vault_dir, 'decisions')
    if not os.path.isdir(decisions_dir):
        return []
    return sorted(
        f for f in os.listdir(decisions_dir)
        if f.startswith('DEC-') and f.endswith('.md')
    )


def main():
    parser = argparse.ArgumentParser(
        description='Export DEC decision cards to an external folder, '
                    'stripping internal frontmatter and skipping cards that '
                    'still reference internal entities by ID prefix.'
    )
    parser.add_argument(
        '--output', '-o', dest='output', required=True,
        help='destination folder for the exported DEC cards',
    )
    parser.add_argument(
        '--path', '-p', dest='project_vault', default=None,
        help='path to the project-vault directory (containing decisions/). '
             'Default: parent of the script location.',
    )
    parser.add_argument(
        '--id', dest='ids', action='append', default=None,
        help='export only this DEC id (repeatable, e.g. --id DEC-0139)',
    )
    parser.add_argument(
        '--type', '-t', dest='types', default='adr',
        help="comma-separated decision_type values to export, or 'all' to "
             'disable the type filter (default: adr)',
    )
    parser.add_argument(
        '--dry-run', dest='dry_run', action='store_true',
        help='check only; do not write exported files',
    )
    args = parser.parse_args()

    vault_dir = resolve_vault_dir(args.project_vault)
    if not os.path.isdir(os.path.join(vault_dir, 'decisions')):
        print(
            f'Error: decisions/ not found under project-vault: {vault_dir}',
            file=sys.stderr,
        )
        sys.exit(1)

    wanted = {i.strip().upper() for i in args.ids} if args.ids else None

    if args.types.strip().lower() == 'all':
        requested_types = None
    else:
        requested_types = {
            t.strip().lower() for t in args.types.split(',') if t.strip()
        }

    exported = 0
    skipped = 0
    filtered = 0

    for fname in list_dec_files(vault_dir):
        filepath = os.path.join(vault_dir, 'decisions', fname)
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()

        fm, body = parse_frontmatter(content)
        card_id = fm.get('id') or fname[:-3]

        if wanted and str(card_id).upper() not in wanted:
            continue

        decision_type = str(fm.get('decision_type') or '').strip().lower()
        if requested_types is not None and decision_type not in requested_types:
            filtered += 1
            continue

        filtered_fm = filter_frontmatter(fm)
        rendered = render_card(filtered_fm, body)

        refs = find_internal_references(rendered)
        if refs:
            skipped += 1
            print(f'SKIP {card_id}: internal references found', file=sys.stderr)
            for kind, token in refs:
                print(f'      {kind}: {token!r}', file=sys.stderr)
            continue

        out_path = os.path.join(args.output, f'{card_id}.md')
        if args.dry_run:
            exported += 1
            print(f'EXPORT (dry-run) {card_id} -> {out_path}')
            continue

        os.makedirs(args.output, exist_ok=True)
        with open(out_path, 'w', encoding=OUTPUT_ENCODING) as f:
            f.write(rendered)
        exported += 1
        print(f'EXPORT {card_id} -> {out_path}')

    print(
        f'Exported: {exported}, skipped (internal refs): {skipped}, '
        f'filtered by type: {filtered}'
    )
    if skipped:
        sys.exit(2)


if __name__ == '__main__':
    main()
