from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SKILL_NAME = "defense-beating-simulator"
MAX_DESCRIPTION_LENGTH = 1024
REQUIRED_FILES = [
    "SKILL.md",
    "AGENTS.md",
    "agents/openai.yaml",
    "references/question-patterns.md",
    "references/project-rubrics.md",
    "assets/project-summary.template.md",
    "assets/question-bank.template.md",
    "assets/weakness-report.template.md",
    "assets/defense-cheatsheet.template.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(skill_md: str) -> dict[str, str]:
    if not skill_md.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        frontmatter, _body = skill_md[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter must end with a standalone --- line") from exc

    data: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def find_repo_root(path: Path | None) -> Path:
    if path is not None:
        return path.resolve()
    return Path(__file__).resolve().parents[1]


def collect_files(root: Path) -> list[Path]:
    ignored = {".git", ".venv", "__pycache__", ".pytest_cache"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in ignored for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return files


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        try:
            skill_md = read_text(skill_path)
            frontmatter = parse_frontmatter(skill_md)
        except Exception as exc:  # noqa: BLE001 - report validation error text
            errors.append(str(exc))
            frontmatter = {}
            skill_md = ""

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if name != SKILL_NAME:
            errors.append(f"SKILL.md name must be {SKILL_NAME!r}, got {name!r}")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
            errors.append("SKILL.md name must be lowercase hyphen-case and under 64 chars")
        if not description:
            errors.append("SKILL.md description is required")
        if len(description) > MAX_DESCRIPTION_LENGTH:
            errors.append("SKILL.md description is too long")
        if "<" in description or ">" in description:
            errors.append("SKILL.md description must not contain angle brackets")
        if len(skill_md.splitlines()) > 500:
            errors.append("SKILL.md should stay under 500 lines")

    openai_path = root / "agents" / "openai.yaml"
    if openai_path.is_file():
        openai_yaml = read_text(openai_path)
        for token in [
            'display_name: "答辩挨打模拟器"',
            "short_description:",
            "default_prompt:",
            "$defense-beating-simulator",
        ]:
            if token not in openai_yaml:
                errors.append(f"agents/openai.yaml missing token: {token}")

    for path in collect_files(root):
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            errors.append(f"File is not valid UTF-8 text: {path.relative_to(root)}")
            continue
        rel = path.relative_to(root).as_posix()
        if "\ufffd" in text:
            errors.append(f"File contains replacement characters: {rel}")
        unfinished_markers = [r"\bTO" + "DO\\b", "place" + "holder", "Replace " + "with"]
        if re.search("|".join(unfinished_markers), text, re.IGNORECASE):
            errors.append(f"File contains unfinished template-marker text: {rel}")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the defense-beating-simulator skill package.")
    parser.add_argument("path", nargs="?", help="Repository or skill root. Defaults to this repository root.")
    args = parser.parse_args(argv)

    root = find_repo_root(Path(args.path) if args.path else None)
    errors = validate(root)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
