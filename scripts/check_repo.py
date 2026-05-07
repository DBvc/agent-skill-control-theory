#!/usr/bin/env python3
"""Lightweight repository checks for Agent Skill Control Theory."""

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
    "docs/foundations.md",
    "docs/control-surfaces.md",
    "docs/design-laws.md",
    "docs/placement.md",
    "docs/host-artifacts.md",
    "docs/collection-design.md",
    "docs/value-function.md",
    "docs/evaluation.md",
    "docs/safety.md",
    "docs/glossary.md",
    "docs/influences.md",
    "templates/skill-ir.yaml",
    "templates/collection-ir.yaml",
    "templates/placement-decision.md",
    "examples/frontend-debug/SKILL.md",
    "examples/frontend-debug/evals/triggers.json",
]

ZH_MIRRORS = [
    "theory.md",
    "foundations.md",
    "control-surfaces.md",
    "design-laws.md",
    "placement.md",
    "host-artifacts.md",
    "collection-design.md",
    "value-function.md",
    "evaluation.md",
    "safety.md",
    "glossary.md",
    "influences.md",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_required_files() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            fail(f"Missing required file: {rel}")
    for rel in ZH_MIRRORS:
        path = ROOT / "docs" / "zh-CN" / rel
        if not path.exists():
            fail(f"Missing Chinese mirror: {path.relative_to(ROOT)}")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        _, fm, _body = text.split("---", 2)
    except ValueError:
        fail("SKILL.md frontmatter is not closed")
    data: dict[str, str] = {}
    for line in fm.strip().splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def check_example_skill() -> None:
    path = ROOT / "examples/frontend-debug/SKILL.md"
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    name = fm.get("name")
    description = fm.get("description")
    if name != "frontend-debug":
        fail("Example skill name must be frontend-debug")
    if not description:
        fail("Example skill description is missing")
    if len(description) > 1024:
        fail("Example skill description exceeds 1024 characters")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("Example skill name is not spec-compatible")


def check_json_files() -> None:
    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def check_local_links() -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in list(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            if not str(target_path).startswith(str(ROOT.resolve())):
                fail(f"Link escapes repo in {path.relative_to(ROOT)}: {target}")
            if target.split("#", 1)[0] and not target_path.exists():
                fail(f"Broken local link in {path.relative_to(ROOT)}: {target}")


def main() -> None:
    check_required_files()
    check_example_skill()
    check_json_files()
    check_local_links()
    print("ASCT repository checks passed.")


if __name__ == "__main__":
    main()
