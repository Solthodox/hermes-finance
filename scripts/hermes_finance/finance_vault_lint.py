#!/usr/bin/env python3
from __future__ import annotations
import re
import sys
from pathlib import Path

VAULT = Path('{{HERMES_FINANCE_VAULT}}')
REQUIRED = ['id','title','type','tags','status','created','updated','source_quality']

def frontmatter(text: str):
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---\n', 4)
    if end < 0:
        return None
    return text[4:end], text[end+5:]

def main() -> int:
    errors = []
    if not VAULT.exists():
        print(f'MISSING vault: {VAULT}', file=sys.stderr)
        return 2
    mds = sorted(VAULT.rglob('*.md'))
    by_stem = {}
    for p in mds:
        by_stem.setdefault(p.stem, []).append(p)
    index_path = VAULT / 'index.md'
    schema_path = VAULT / 'SCHEMA.md'
    index = index_path.read_text(encoding='utf-8') if index_path.exists() else ''
    schema = schema_path.read_text(encoding='utf-8') if schema_path.exists() else ''
    taxonomy = set(re.findall(r'`#([a-z0-9-]+)`', schema))
    if not taxonomy:
        errors.append('SCHEMA.md has no tag taxonomy')
    for p in mds:
        text = p.read_text(encoding='utf-8')
        parsed = frontmatter(text)
        if parsed is None:
            errors.append(f'{p.relative_to(VAULT)}: missing or invalid frontmatter')
            continue
        fm, rest = parsed
        for key in REQUIRED:
            if not re.search(rf'^{key}:', fm, re.M):
                errors.append(f'{p.relative_to(VAULT)}: missing frontmatter key {key}')
        m = re.search(r'^tags:\s*\[([^\]]*)\]', fm, re.M)
        if not m:
            errors.append(f'{p.relative_to(VAULT)}: tags must be inline list')
        else:
            for tag in [t.strip() for t in m.group(1).split(',') if t.strip()]:
                if tag not in taxonomy:
                    errors.append(f'{p.relative_to(VAULT)}: unknown tag {tag}')
        if not re.search(r'^#\s+', rest, re.M):
            errors.append(f'{p.relative_to(VAULT)}: missing H1')
        for link in re.findall(r'\[\[([^\]|#]+)', text):
            if link not in by_stem:
                errors.append(f'{p.relative_to(VAULT)}: broken wikilink [[{link}]]')
    for p in mds:
        if p.name == 'index.md':
            continue
        if f'[[{p.stem}]]' not in index:
            errors.append(f'index.md missing [[{p.stem}]]')
    content_pages = [p for p in mds if p.name not in {'index.md','SCHEMA.md','log.md'}]
    if len(content_pages) < 80:
        errors.append(f'only {len(content_pages)} content pages, expected >=80')
    if len(content_pages) > 130:
        errors.append(f'{len(content_pages)} content pages, expected <=130')
    if errors:
        print('FAIL finance vault lint')
        for err in errors:
            print(f'- {err}')
        return 1
    print(f'PASS finance vault lint: {len(content_pages)} content pages, {len(mds)} markdown files')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
