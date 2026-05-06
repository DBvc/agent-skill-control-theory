#!/usr/bin/env python3
"""Lightweight checks for the ASCT repository.

This is intentionally dependency-free. It checks:
- required files exist;
- example SKILL.md files have frontmatter with name and description;
- example skill directory name matches frontmatter name;
- JSON eval fixtures parse.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "docs/theory.md",
    "docs/zh-CN/theory.md",
    "docs/glossary.md",
    "docs/zh-CN/glossary.md",
    "docs/control-surfaces.md",
    "docs/zh-CN/control-surfaces.md",
    "docs/design-laws.md",
    "docs/zh-CN/design-laws.md",
    "docs/value-function.md",
    "docs/zh-CN/value-function.md",
    "docs/safety.md",
    "docs/zh-CN/safety.md",
    "docs/influences.md",
    "docs/zh-CN/influences.md",
    "templates/skill-ir.yaml",
    "templates/skill-design-brief.md",
    "templates/skill-review-rubric.md",
    "templates/eval-plan.md",
    "templates/patch-hypothesis.md",
    "LICENSE",
]

FRONTMATTER_RE = re.compile(r"^---\n(?P<body>.*?)\n---\n", re.DOTALL)
FIELD_RE = re.compile(r"^(?P<key>[a-zA-Z0-9_-]+):\s*(?P<value>.*)$")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter")
    fields: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        field = FIELD_RE.match(line)
        if field:
            fields[field.group("key")] = field.group("value").strip().strip('"')
    return fields


def check_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")


def check_example_skills(errors: list[str]) -> None:
    examples = ROOT / "examples"
    for skill_md in examples.glob("*/SKILL.md"):
        try:
            fields = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{skill_md.relative_to(ROOT)}: {exc}")
            continue
        name = fields.get("name", "")
        description = fields.get("description", "")
        if not name:
            errors.append(f"{skill_md.relative_to(ROOT)}: missing name")
        elif not NAME_RE.match(name):
            errors.append(f"{skill_md.relative_to(ROOT)}: invalid name {name!r}")
        elif skill_md.parent.name != name:
            errors.append(
                f"{skill_md.relative_to(ROOT)}: frontmatter name {name!r} does not match directory {skill_md.parent.name!r}"
            )
        if not description:
            errors.append(f"{skill_md.relative_to(ROOT)}: missing description")
        elif len(description) > 1024:
            errors.append(f"{skill_md.relative_to(ROOT)}: description exceeds 1024 chars")


def check_json(errors: list[str]) -> None:
    for path in list((ROOT / "examples").glob("**/*.json")) + list((ROOT / "templates").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_example_skills(errors)
    check_json(errors)

    if errors:
        print("ASCT repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("ASCT repository checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
