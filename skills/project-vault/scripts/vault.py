"""
Generate work/_index.md and tracks/_index.md from frontmatter of
corresponding atomic files in a project-vault/ directory.
Also: allocate next entity IDs, and check for duplicate/mismatched IDs.

Usage:
  python vault.py [work|tracks|all]      # regenerate indexes (default: all)
  python vault.py next-id [TYPE]         # next free ID per type (or one type)
  python vault.py check                  # detect duplicate / mismatched IDs

  python vault.py all --path "D:/path/to/project-vault"

The optional `--path` (or `-p`) argument points at the project-vault directory
(the one containing `work/` and `tracks/`). When omitted, the script derives the
location from its own install path (`skills/project-vault/scripts` inside a repo).

Call this after every WRK creation to keep indexes in sync with sources.

ID allocation (`next-id`) and duplicate detection (`check`) assume a FLAT vault:
each entity type lives in ONE directory (`decisions/`, `open-questions/`,
`risks/`, `contradictions/`, `tracks/`). Closed entities stay in place with
`status` set in frontmatter — there is no separate `archive/` mirror.
IDs are monotonic and never reused; `next-id` returns `max + 1` over the flat
directory, which is therefore collision-free by construction.
"""

import os
import sys
import re
import argparse
import yaml
from datetime import datetime

OUTPUT_ENCODING = 'utf-8'

# Entity types that carry a sequential numeric ID (single flat directory each).
ENTITY_TYPES = {
    'DEC': 'decisions',
    'Q': 'open-questions',
    'RISK': 'risks',
    'CON': 'contradictions',
    'TRK': 'tracks',
}


def resolve_vault_dir(cli_path):
    """Return the project-vault directory (containing work/ and tracks/)."""
    if cli_path:
        return os.path.abspath(cli_path)
    # Fallback: scripts → project-vault → skills → .agents → repo-root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))))
    return os.path.join(repo_root, 'project-vault')


def parse_frontmatter(content):
    """Parse YAML frontmatter block from markdown content."""
    if not content.startswith('---\n') and not content.startswith('---\r'):
        return {}, content
    m = re.match(r'^---\r?\n(.*?)\r?\n---', content, re.DOTALL)
    if not m:
        return {}, content
    fm_text = m.group(1)
    body = content[m.end():].strip()
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


def extract_essence(body, max_len=250):
    """Extract first continuous text paragraph as essence, skipping headings."""
    lines = body.split('\n')
    paragraphs = []
    current = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            if current:
                paragraphs.append(' '.join(current))
                current = []
            continue
        if not stripped:
            if current:
                paragraphs.append(' '.join(current))
                current = []
            continue
        if stripped.startswith('|') or stripped.startswith('- ') or stripped.startswith('* '):
            if current:
                paragraphs.append(' '.join(current))
                current = []
            continue
        current.append(stripped)
    if current:
        paragraphs.append(' '.join(current))

    essence = paragraphs[0] if paragraphs else ''
    if len(essence) > max_len:
        essence = essence[:max_len] + '…'
    return essence


def generate_work_index(work_dir):
    """Generate <vault>/work/_index.md from WRK-*.md files."""
    wrk_files = sorted([
        f for f in os.listdir(work_dir)
        if f.startswith('WRK-') and f.endswith('.md') and f != '_index.md'
    ])

    rows = []
    for fname in wrk_files:
        filepath = os.path.join(work_dir, fname)
        with open(filepath, 'r', encoding=OUTPUT_ENCODING) as f:
            content = f.read()

        fm, body = parse_frontmatter(content)
        wrk_id = fm.get('id', fname.replace('.md', ''))
        track = fm.get('performed_under', '—')
        if track is None:
            track = '—'
        method = fm.get('enacted_method', '—')
        if method is None:
            method = '—'
        if isinstance(method, list):
            method = ', '.join(method)
        essence = extract_essence(body)

        rows.append({
            'id': str(wrk_id),
            'filename': fname,
            'track': str(track),
            'method': str(method),
            'essence': essence,
        })

    today = datetime.now().strftime('%Y-%m-%d')

    lines = []
    lines.append('---')
    lines.append(f'updated: "{today}"')
    lines.append('generated: true')
    lines.append('---')
    lines.append('')
    lines.append('# Журнал выполненной работы (ходов)')
    lines.append('')
    lines.append(
        'Сквозной хронологический журнал: датированные вхождения работы '
        '(`U.Work`, A.15.1) в рамках треков проекта. '
        'Атомарные записи — в файлах `WRK-YYYY-MM-DD-hhmmss.md`.'
    )
    lines.append('')
    lines.append(
        '> Сгенерировано автоматически из frontmatter WRK-файлов '
        'скриптом `scripts/vault.py`. '
        'Вызывается после каждого завершённого WRK (Procedure W.2).'
    )
    lines.append('')
    lines.append('## Сводка')
    lines.append('')
    lines.append('| ID | Трек | FPF-паттерн | Суть |')
    lines.append('|----|------|-------------|------|')

    for r in rows:
        lines.append(
            f'| [{r["id"]}]({r["filename"]}) | {r["track"]} '
            f'| {r["method"]} | {r["essence"]} |'
        )

    return '\n'.join(lines) + '\n'


def generate_tracks_index(tracks_dir):
    """Generate <vault>/tracks/_index.md from TRK-*.md files."""
    trk_files = sorted([
        f for f in os.listdir(tracks_dir)
        if f.startswith('TRK-') and f.endswith('.md') and f != '_index.md'
    ])

    rows = []
    for fname in trk_files:
        filepath = os.path.join(tracks_dir, fname)
        with open(filepath, 'r', encoding=OUTPUT_ENCODING) as f:
            content = f.read()

        fm, body = parse_frontmatter(content)
        trk_id = fm.get('id', fname.replace('.md', ''))
        essence = extract_essence(body, max_len=200)

        rows.append({
            'id': str(trk_id),
            'filename': fname,
            'essence': essence,
        })

    today = datetime.now().strftime('%Y-%m-%d')

    lines = []
    lines.append('---')
    lines.append(f'updated: "{today}"')
    lines.append('generated: true')
    lines.append('---')
    lines.append('')
    lines.append('# Индекс треков проработки')
    lines.append('')
    lines.append(
        'Сводная карта проработки проекта. Трек — операциональная линия '
        'работы: от сигнала до выполненной работы и оценки результата.'
    )
    lines.append('')
    lines.append(
        '> Сгенерировано автоматически из frontmatter TRK-файлов '
        'скриптом `scripts/vault.py`.'
    )
    lines.append('')
    lines.append('## Сводка')
    lines.append('')
    lines.append('| Трек | Суть |')
    lines.append('| ---- | ---- |')

    for r in rows:
        lines.append(f'| [{r["id"]}]({r["filename"]}) | {r["essence"]} |')

    return '\n'.join(lines) + '\n'


# --- ID allocation and duplicate detection (flat vault) ---

def _default_prefix(type_code):
    if type_code == 'DEC':
        return 'DEC-'
    return f"{type_code}-{datetime.now().year}-"


def parse_id_parts(id_str):
    """Split an entity id like 'Q-2026-0274' / 'DEC-0057' into (prefix, number)."""
    s = str(id_str).strip()
    m = re.search(r'^(.*?)(\d+)$', s)
    if not m:
        return None, None
    return m.group(1), int(m.group(2))


def _collect_ids(vault_dir, type_code):
    """Return list of (filename, id_str, prefix, number) for a flat entity dir."""
    dirname = ENTITY_TYPES[type_code]
    d = os.path.join(vault_dir, dirname)
    items = []
    if not os.path.isdir(d):
        return items
    for fn in sorted(os.listdir(d)):
        if not fn.endswith('.md') or fn.startswith('_'):
            continue
        eid = None
        try:
            with open(os.path.join(d, fn), 'r', encoding=OUTPUT_ENCODING) as f:
                fm, _ = parse_frontmatter(f.read())
            eid = fm.get('id')
        except Exception:
            eid = None
        if not eid:
            eid = fn[:-3]
        prefix, num = parse_id_parts(str(eid))
        items.append((fn, str(eid), prefix, num))
    return items


def next_id(vault_dir, type_code):
    """Return the next free ID for a type (max number + 1, prefix reused)."""
    items = _collect_ids(vault_dir, type_code)
    max_n = 0
    max_prefix = _default_prefix(type_code)
    for _fn, _eid, prefix, num in items:
        if num is None:
            continue
        if num > max_n:
            max_n = num
            if prefix is not None:
                max_prefix = prefix
    return f"{max_prefix}{max_n + 1:04d}"


def check_duplicates(vault_dir):
    """Return a list of duplicate-id and filename/id-mismatch problems."""
    problems = []
    for type_code, dirname in ENTITY_TYPES.items():
        items = _collect_ids(vault_dir, type_code)
        by_id = {}
        for fn, eid, _prefix, _num in items:
            by_id.setdefault(eid, []).append(fn)
        for eid, files in by_id.items():
            if len(files) > 1:
                problems.append(
                    f"duplicate id '{eid}' in {dirname}/: {', '.join(files)}"
                )
        for fn, eid, _prefix, _num in items:
            base = fn[:-3]
            if base != eid and not base.startswith(str(eid) + '-'):
                problems.append(
                    f"filename/id mismatch in {dirname}/{fn}: file '{base}' vs id '{eid}'"
                )
    return problems


def main():
    parser = argparse.ArgumentParser(
        description='Generate work/_index.md and tracks/_index.md for a project-vault; '
                    'allocate next IDs; check for duplicate IDs.'
    )
    parser.add_argument(
        'command', nargs='?', default='all',
        choices=['work', 'tracks', 'all', 'next-id', 'check'],
        help="'work'|'tracks'|'all' — regenerate indexes (default: all); "
             "'next-id [TYPE]' — print next free ID; 'check' — duplicate detection",
    )
    parser.add_argument(
        'entity_type', nargs='?', default=None,
        help="for 'next-id': one of DEC, Q, RISK, CON, TRK (omit to list all)",
    )
    parser.add_argument(
        '--path', '-p', dest='project_vault', default=None,
        help='path to the project-vault directory (containing work/ and tracks/). '
             'Default: derived from the script install location.',
    )
    args = parser.parse_args()

    vault_dir = resolve_vault_dir(args.project_vault)
    if not os.path.isdir(vault_dir):
        print(f'Error: project-vault directory not found: {vault_dir}', file=sys.stderr)
        sys.exit(1)

    if args.command == 'next-id':
        if args.entity_type:
            t = args.entity_type.upper()
            if t not in ENTITY_TYPES:
                print(f'Error: unknown entity type "{args.entity_type}"', file=sys.stderr)
                sys.exit(1)
            print(next_id(vault_dir, t))
        else:
            for t in ENTITY_TYPES:
                print(f"{t:5s} {next_id(vault_dir, t)}")
        return

    if args.command == 'check':
        problems = check_duplicates(vault_dir)
        if problems:
            for p in problems:
                print(f'ERROR: {p}', file=sys.stderr)
            sys.exit(1)
        print('OK: no duplicate or mismatched IDs')
        return

    # Index generation (work/tracks/all). Also run a warning-only duplicate check.
    for p in check_duplicates(vault_dir):
        print(f'WARNING: {p}', file=sys.stderr)

    work_dir = os.path.join(vault_dir, 'work')
    tracks_dir = os.path.join(vault_dir, 'tracks')

    if args.command in ('work', 'all'):
        if not os.path.isdir(work_dir):
            print(f'Error: work directory not found: {work_dir}', file=sys.stderr)
            sys.exit(1)
        work_index = generate_work_index(work_dir)
        work_path = os.path.join(work_dir, '_index.md')
        with open(work_path, 'w', encoding=OUTPUT_ENCODING) as f:
            f.write(work_index)
        print(f'Generated: {work_path}')

    if args.command in ('tracks', 'all'):
        if not os.path.isdir(tracks_dir):
            print(f'Error: tracks directory not found: {tracks_dir}', file=sys.stderr)
            sys.exit(1)
        tracks_index = generate_tracks_index(tracks_dir)
        tracks_path = os.path.join(tracks_dir, '_index.md')
        with open(tracks_path, 'w', encoding=OUTPUT_ENCODING) as f:
            f.write(tracks_index)
        print(f'Generated: {tracks_path}')


if __name__ == '__main__':
    main()
