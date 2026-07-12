from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


SKILL_NAME = "defense-beating-simulator"
MAX_DESCRIPTION_LENGTH = 700
REQUIRED_FILES = [
    "SKILL.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "README.md",
    "README.zh-CN.md",
    "README.en.md",
    "agents/openai.yaml",
    "references/question-patterns.md",
    "references/project-rubrics.md",
    "references/domain-ai-projects.md",
    "references/domain-web-showcase.md",
    "references/domain-engineering-simulation.md",
    "references/domain-course-design.md",
    "references/domain-research-prototype.md",
    "assets/project-summary.template.md",
    "assets/question-bank.template.md",
    "assets/weakness-report.template.md",
    "assets/defense-cheatsheet.template.md",
    "examples/campus-energy-system/input-project-summary.md",
    "examples/campus-energy-system/expected-output-chat.md",
    "examples/yolo-pv-defect-detection/input-project-summary.md",
    "examples/yolo-pv-defect-detection/expected-output-chat.md",
    "evals/prompts.csv",
    "evals/expected_checks.yaml",
    "evals/README.md",
]
REQUIRED_SKILL_TOKENS = [
    "## When to use",
    "## Do not use",
    "## Claim-Evidence Matrix",
    "## Evidence labeling rules",
    "Material-supported",
    "Material-implied",
    "Material-missing",
    "Risk-inferred",
    "**One-sentence positioning**",
    "**Top 5 high-risk gaps**",
    "**Safe answer strategies**",
    "**Material repair checklist**",
]
REQUIRED_TEMPLATE_TOKENS = {
    "assets/project-summary.template.md": ["Claim-Evidence Summary", "Evidence label"],
    "assets/question-bank.template.md": ["High-risk Question Chains", "Required material repair"],
    "assets/weakness-report.template.md": ["Overall Risk Level", "Safe Answer Bank"],
    "assets/defense-cheatsheet.template.md": ["Three Things Not to Overclaim", "Final 30-second Summary"],
}
MOJIBAKE_MARKERS = [
    chr(0x6924) + chr(0x572d),
    chr(0x7edb) + chr(0x65c7),
    chr(0x6d93) + chr(0x30e5),
    chr(0x7039) + chr(0x2103),
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
    ignored = {".git", ".venv", "__pycache__", ".pytest_cache", "tmp-agent-install", ".agent-skills", "agent-skills"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in ignored for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return files


def validate_skill_md(root: Path, errors: list[str]) -> None:
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return
    try:
        skill_md = read_text(skill_path)
        frontmatter = parse_frontmatter(skill_md)
    except Exception as exc:  # noqa: BLE001 - report validation error text
        errors.append(str(exc))
        return

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
    if "generic questions" in description.lower():
        errors.append("SKILL.md description should not frame the skill as generic question generation")
    if len(skill_md.splitlines()) > 500:
        errors.append("SKILL.md should stay under 500 lines")

    for token in REQUIRED_SKILL_TOKENS:
        if token not in skill_md:
            errors.append(f"SKILL.md missing required token: {token}")


def validate_openai_yaml(root: Path, errors: list[str]) -> None:
    openai_path = root / "agents" / "openai.yaml"
    if not openai_path.is_file():
        return
    openai_yaml = read_text(openai_path)
    for token in [
        'display_name: "项目答辩红队审查器"',
        "short_description:",
        "default_prompt:",
        "$defense-beating-simulator",
        "Claim-Evidence Matrix",
    ]:
        if token not in openai_yaml:
            errors.append(f"agents/openai.yaml missing token: {token}")


def validate_agent_compatibility(root: Path, errors: list[str]) -> None:
    checks = {
        "AGENTS.md": ["Universal agent compatibility", "CLAUDE.md", "GEMINI.md", ".agents/skills"],
        "CLAUDE.md": ["AGENTS.md", "SKILL.md", "Claim-Evidence Matrix"],
        "GEMINI.md": ["AGENTS.md", "SKILL.md", "Claim-Evidence Matrix"],
        "install.ps1": ['"codex", "generic", "project"', ".agents\\skills"],
        "install.sh": ["codex|generic|project", ".agents/skills"],
    }
    for rel, tokens in checks.items():
        path = root / rel
        if not path.is_file():
            continue
        text = read_text(path)
        for token in tokens:
            if token not in text:
                errors.append(f"{rel} missing compatibility token: {token}")


def validate_templates(root: Path, errors: list[str]) -> None:
    for rel, tokens in REQUIRED_TEMPLATE_TOKENS.items():
        path = root / rel
        if not path.is_file():
            continue
        text = read_text(path)
        for token in tokens:
            if token not in text:
                errors.append(f"{rel} missing token: {token}")


def validate_evals(root: Path, errors: list[str]) -> None:
    prompts_path = root / "evals" / "prompts.csv"
    if not prompts_path.is_file():
        return
    try:
        with prompts_path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except Exception as exc:  # noqa: BLE001 - surface CSV parse errors
        errors.append(f"evals/prompts.csv is not valid CSV: {exc}")
        return

    if len(rows) < 10:
        errors.append("evals/prompts.csv should contain at least 10 prompts")
    if not any(row.get("should_trigger") == "false" for row in rows):
        errors.append("evals/prompts.csv should include negative prompts")
    if not any("Claim-Evidence Matrix" in row.get("expected_sections", "") for row in rows):
        errors.append("evals/prompts.csv should check Claim-Evidence Matrix output")


def validate_text_files(root: Path, errors: list[str]) -> None:
    unfinished_markers = [r"\bTO" + "DO\b", "place" + "holder", "Replace " + "with"]
    for path in collect_files(root):
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            errors.append(f"File is not valid UTF-8 text: {path.relative_to(root)}")
            continue
        rel = path.relative_to(root).as_posix()
        if "\ufffd" in text:
            errors.append(f"File contains replacement characters: {rel}")
        if any(marker in text for marker in MOJIBAKE_MARKERS):
            errors.append(f"File appears to contain mojibake text: {rel}")
        if re.search("|".join(unfinished_markers), text, re.IGNORECASE):
            errors.append(f"File contains unfinished template-marker text: {rel}")


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    validate_skill_md(root, errors)
    validate_openai_yaml(root, errors)
    validate_agent_compatibility(root, errors)
    validate_templates(root, errors)
    validate_evals(root, errors)
    validate_text_files(root, errors)
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
