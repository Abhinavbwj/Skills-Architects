#!/usr/bin/env python3
"""Lint skill descriptions against org upload limits.

- plugin.json description: max 500 chars
- SKILL.md description field: max 1024 chars
"""

import json
import sys
import re
from pathlib import Path

ROOT = Path(__file__).parent
SKILLS_DIR = ROOT / "skills"
PLUGIN_JSON = ROOT / ".claude-plugin" / "plugin.json"

PLUGIN_DESC_MAX = 500
SKILL_DESC_MAX = 1024

errors = []


def extract_skill_description(content: str) -> str | None:
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return None
    frontmatter = fm_match.group(1)

    inline = re.search(r"^description:\s+(.+)$", frontmatter, re.MULTILINE)
    if inline and not inline.group(1).strip().startswith(">"):
        return inline.group(1).strip()

    block = re.search(
        r"^description:\s*[>|][^\n]*\n((?:[ \t]+[^\n]*\n?)+)",
        frontmatter,
        re.MULTILINE,
    )
    if block:
        lines = block.group(1).splitlines()
        return " ".join(line.strip() for line in lines).strip()

    return None


# Check plugin.json
if PLUGIN_JSON.exists():
    data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    desc = data.get("description", "")
    length = len(desc)
    rel = PLUGIN_JSON.relative_to(ROOT)
    if length > PLUGIN_DESC_MAX:
        errors.append(f"FAIL {rel}: description is {length} chars (max {PLUGIN_DESC_MAX})")
    else:
        print(f"OK   {rel} ({length} chars)")
else:
    errors.append(f"FAIL .claude-plugin/plugin.json: file not found")

# Check SKILL.md files
for skill_file in sorted(SKILLS_DIR.rglob("SKILL.md")):
    content = skill_file.read_text(encoding="utf-8")
    desc = extract_skill_description(content)
    rel = skill_file.relative_to(ROOT)

    if desc is None:
        errors.append(f"FAIL {rel}: missing or unparseable description field")
        continue

    length = len(desc)
    if length > SKILL_DESC_MAX:
        errors.append(f"FAIL {rel}: description is {length} chars (max {SKILL_DESC_MAX})")
    else:
        print(f"OK   {rel} ({length} chars)")

if errors:
    print()
    for e in errors:
        print(e)
    sys.exit(1)
