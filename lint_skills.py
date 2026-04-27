#!/usr/bin/env python3
"""Lint SKILL.md files: description must be at most 1024 characters."""

import sys
import re
from pathlib import Path

DESCRIPTION_MAX = 1024
SKILLS_DIR = Path(__file__).parent / "skills"

def extract_description(content: str) -> str | None:
    """Extract description value from YAML frontmatter, handling block scalars."""
    # Isolate frontmatter block
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return None
    frontmatter = fm_match.group(1)

    # Match inline: description: some text
    inline = re.search(r"^description:\s+(.+)$", frontmatter, re.MULTILINE)
    if inline and not inline.group(1).strip().startswith(">"):
        return inline.group(1).strip()

    # Match block scalar: description: >\n  indented lines...
    block = re.search(
        r"^description:\s*[>|][^\n]*\n((?:[ \t]+[^\n]*\n?)+)",
        frontmatter,
        re.MULTILINE,
    )
    if block:
        lines = block.group(1).splitlines()
        # Strip leading indentation and join (folded scalar collapses newlines to spaces)
        stripped = [line.strip() for line in lines]
        return " ".join(stripped).strip()

    return None


errors = []

for skill_file in sorted(SKILLS_DIR.rglob("SKILL.md")):
    content = skill_file.read_text(encoding="utf-8")
    desc = extract_description(content)
    rel = skill_file.relative_to(SKILLS_DIR.parent)

    if desc is None:
        errors.append(f"FAIL {rel}: missing or unparseable description field")
        continue

    length = len(desc)
    if length > DESCRIPTION_MAX:
        errors.append(f"FAIL {rel}: description is {length} chars (max {DESCRIPTION_MAX})")
    else:
        print(f"OK   {rel} ({length} chars)")

if errors:
    print()
    for e in errors:
        print(e)
    sys.exit(1)
