"""
Machine frontmatter check for the project-vault skill (PLAS CC-QR.6).

Fails on any YAML parse error or missing required field, so the skill cannot be
"relied on" without a passing check. Covers the routing-only SKILL.md
(description YAML-safety) and every E.8 body in references/ (id/title/status/
readiness), plus the INDEX.md <-> references/ consistency.

Usage:
  python check_frontmatter.py [--path <skill-dir>]
Exit code 0 = pass, 1 = fail.
"""

import argparse
import os
import re
import sys

import yaml


def parse_frontmatter(path):
    """Return (frontmatter_dict, body_text) for a markdown file, or raise."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('\ufeff'):
        raise ValueError('file has a UTF-8 BOM (breaks YAML frontmatter parsing)')
    if not content.startswith('---'):
        raise ValueError('no YAML frontmatter')
    m = re.match(r'^---\r?\n(.*?)\r?\n---', content, re.DOTALL)
    if not m:
        raise ValueError('invalid frontmatter delimiters')
    fm = yaml.safe_load(m.group(1))
    if not isinstance(fm, dict):
        raise ValueError('frontmatter is not a YAML mapping')
    return fm, content[m.end():]


def check_skill_md(path):
    fm, _ = parse_frontmatter(path)
    for key in ('name', 'description'):
        if key not in fm:
            raise ValueError(f"SKILL.md missing required key '{key}'")
    name = fm['name']
    if not isinstance(name, str) or not re.match(r'^[a-z0-9-]+$', name):
        raise ValueError(f"SKILL.md name '{name}' is not kebab-case")
    desc = fm['description']
    if not isinstance(desc, str) or not desc.strip():
        raise ValueError('SKILL.md description is empty or not a string')
    if '<' in desc or '>' in desc:
        raise ValueError('SKILL.md description contains angle brackets')


REQUIRED_BODY_KEYS = ('id', 'title', 'status', 'readiness')
VALID_READINESS = ('source-faithful', 'case-validated')


def check_body(path):
    fm, _ = parse_frontmatter(path)
    for key in REQUIRED_BODY_KEYS:
        if key not in fm:
            raise ValueError(f"missing required key '{key}'")
    pid = fm['id']
    fname = os.path.splitext(os.path.basename(path))[0]
    if not re.match(r'^[A-Za-z0-9]+\.[A-Za-z0-9]+$', str(pid)):
        raise ValueError(f"id '{pid}' is not a <Code>.<Name> PatternID")
    if pid != fname:
        raise ValueError(f"id '{pid}' != filename '{fname}'")
    if fm['readiness'] not in VALID_READINESS:
        raise ValueError(f"readiness '{fm['readiness']}' not in {VALID_READINESS}")


def check_index(path, body_ids):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    listed = re.findall(r'`(PV\.[A-Za-z0-9]+)`', content)
    missing = sorted(set(body_ids) - set(listed))
    extra = sorted(set(listed) - set(body_ids))
    if missing:
        raise ValueError(f"INDEX.md missing pattern IDs: {missing}")
    if extra:
        raise ValueError(f"INDEX.md lists unknown pattern IDs: {extra}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', default=None, help='path to the skill directory')
    args = parser.parse_args()

    skill_dir = args.path or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    refs_dir = os.path.join(skill_dir, 'references')

    problems = []

    def run(label, fn):
        try:
            fn()
            print(f'PASS {label}')
        except Exception as e:
            problems.append(f'{label}: {e}')
            print(f'FAIL {label}: {e}')

    run('SKILL.md', lambda: check_skill_md(os.path.join(skill_dir, 'SKILL.md')))

    body_files = sorted(
        f for f in os.listdir(refs_dir)
        if f.startswith('PV.') and f.endswith('.md')
    )
    body_ids = [os.path.splitext(f)[0] for f in body_files]
    for f in body_files:
        run(f, lambda f=f: check_body(os.path.join(refs_dir, f)))

    run('INDEX.md', lambda: check_index(os.path.join(refs_dir, 'INDEX.md'), body_ids))

    if problems:
        print('\nFrontmatter check FAILED:', file=sys.stderr)
        for p in problems:
            print(f'  - {p}', file=sys.stderr)
        sys.exit(1)
    print('\nFrontmatter check passed.')


if __name__ == '__main__':
    main()
