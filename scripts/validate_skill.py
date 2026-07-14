from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


SKILL_NAME = "defense-beating-simulator"
DISPLAY_NAME = "针对性答辩模拟器"
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
    "scripts/evaluate_response.py",
    "install.ps1",
    "install.sh",
    "pyproject.toml",
]

FULL_REVIEW_SECTIONS = [
    "项目一句话定位",
    "Claim-Evidence Matrix",
    "高风险缺口",
    "连续追问链",
    "防守型回答策略",
    "材料修复清单",
    "答辩速查卡",
]

MANDATORY_OUTPUT_LABELS = [
    "**项目一句话定位**",
    "**Claim-Evidence Matrix**",
    "**高风险缺口（最多 5 项）**",
    "**连续追问链**",
    "**防守型回答策略**",
    "**材料修复清单**",
    "**答辩速查卡**",
]

MATRIX_HEADERS = [
    "Claim / 项目说法",
    "Evidence / 材料依据",
    "Evidence status / 证据状态",
    "Gap / 缺口",
    "Risk basis / 风险依据",
    "Risk",
]

EVIDENCE_STATUSES = ["Material-supported", "Material-implied", "Material-missing"]
RISK_BASES = ["Material-derived", "Risk-inferred"]
INTENSITY_LABELS = ["先热个身", "开始挑刺", "严刑拷打"]

REQUIRED_TEMPLATE_TOKENS = {
    "assets/project-summary.template.md": ["Claim-Evidence Summary", "Evidence status", "Risk basis"],
    "assets/question-bank.template.md": [
        "High-risk Question Chains",
        "Evidence status",
        "Risk basis",
        "Required material repair",
    ],
    "assets/weakness-report.template.md": [
        "Overall Risk Level",
        "Evidence Status",
        "Risk Basis",
        "Safe Answer Bank",
    ],
    "assets/defense-cheatsheet.template.md": [
        "Three Things Not to Overclaim",
        "Evidence Status",
        "Risk Basis",
        "Final 30-second Summary",
    ],
}

TEXT_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".csv", ".toml", ".ps1", ".sh", ".txt"}
IGNORED_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache", "build", "dist"}
MOJIBAKE_MARKERS = [
    "\u951f\u65a4\u62f7",
    "\u9239\u6e3e",
    "\u7edb\u65f1\u4eac",
    "\u6924\u572d\u6d30",
    "\u95c2\u6e48\u7c3f",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(skill_md: str) -> dict[str, str]:
    normalized = skill_md.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        frontmatter, _body = normalized[4:].split("\n---\n", 1)
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


def parse_simple_yaml_lists(text: str) -> dict[str, list[str]]:
    """Parse the small top-level list subset used by the eval rules."""
    result: dict[str, list[str]] = {}
    current: str | None = None
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" ") and line.endswith(":"):
            current = line[:-1].strip()
            if not current:
                raise ValueError(f"Empty YAML key on line {line_number}")
            result[current] = []
            continue
        if line.startswith("  - ") and current:
            value = line[4:].strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
                value = value[1:-1]
            result[current].append(value)
            continue
        raise ValueError(f"Unsupported eval YAML syntax on line {line_number}: {raw_line}")
    return result


def find_repo_root(path: Path | None) -> Path:
    if path is not None:
        return path.resolve()
    cwd = Path.cwd().resolve()
    if (cwd / "SKILL.md").is_file():
        return cwd
    return Path(__file__).resolve().parents[1]


def collect_text_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in IGNORED_DIRS or part.endswith(".egg-info") for part in path.parts):
            continue
        if path.is_file() and (path.suffix.lower() in TEXT_SUFFIXES or path.name == ".gitignore"):
            files.append(path)
    return files


def require_tokens(text: str, tokens: list[str], rel: str, errors: list[str]) -> None:
    for token in tokens:
        if token not in text:
            errors.append(f"{rel} missing required token: {token}")


def assert_order(text: str, tokens: list[str], rel: str, errors: list[str]) -> None:
    positions = [text.find(token) for token in tokens]
    if any(position < 0 for position in positions):
        return
    if positions != sorted(positions):
        errors.append(f"{rel} does not keep the required section order")


def validate_skill_md(root: Path, errors: list[str]) -> None:
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return
    try:
        skill_md = read_text(skill_path)
        frontmatter = parse_frontmatter(skill_md)
    except Exception as exc:  # noqa: BLE001
        errors.append(str(exc))
        return

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if name != SKILL_NAME:
        errors.append(f"SKILL.md name must be {SKILL_NAME!r}, got {name!r}")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append("SKILL.md name must be lowercase hyphen-case and under 64 chars")
    if not description or len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append("SKILL.md description must be present and under 700 characters")
    if "<" in description or ">" in description:
        errors.append("SKILL.md description must not contain angle brackets")

    required = [
        f"# {DISPLAY_NAME}",
        "## When to use",
        "## Do not use",
        "## Mandatory full-review output",
        "## Claim-Evidence Matrix",
        "## Evidence labeling rules",
        "## Answer scoring",
        "## Final self-check",
        "高风险缺口（最多 5 项）",
        "it is not automatically proof that the claim is true",
        "Material-derived + Risk-inferred",
        *MATRIX_HEADERS,
        *EVIDENCE_STATUSES,
        *RISK_BASES,
        *INTENSITY_LABELS,
    ]
    require_tokens(skill_md, required, "SKILL.md", errors)
    assert_order(skill_md, MANDATORY_OUTPUT_LABELS, "SKILL.md", errors)
    if len(skill_md.splitlines()) > 500:
        errors.append("SKILL.md should stay under 500 lines")


def validate_branding(root: Path, errors: list[str]) -> None:
    checks = {
        "README.md": [f"# {DISPLAY_NAME}", "README.en.md"],
        "README.zh-CN.md": [f"# {DISPLAY_NAME}"],
        "AGENTS.md": [f"# {DISPLAY_NAME}"],
        "CLAUDE.md": [f"# {DISPLAY_NAME}"],
        "GEMINI.md": [f"# {DISPLAY_NAME}"],
        "agents/openai.yaml": [f'display_name: "{DISPLAY_NAME}"', "$defense-beating-simulator"],
        "pyproject.toml": [f'display_name = "{DISPLAY_NAME}"'],
    }
    for rel, tokens in checks.items():
        path = root / rel
        if path.is_file():
            require_tokens(read_text(path), tokens, rel, errors)


def validate_agent_compatibility(root: Path, errors: list[str]) -> None:
    checks = {
        "AGENTS.md": [
            "~/.codex/skills",
            "~/.agents/skills",
            "~/.claude/skills",
            "~/.gemini/skills",
            "~/.copilot/skills",
        ],
        "install.ps1": ["codex", "agents", "generic", "claude", "gemini", "copilot", "project", ".agents\\skills"],
        "install.sh": ["codex|agents|generic|claude|gemini|copilot|project", ".agents/skills"],
    }
    for rel, tokens in checks.items():
        path = root / rel
        if path.is_file():
            text = read_text(path)
            require_tokens(text, tokens, rel, errors)
            if ".agent-skills" in text:
                errors.append(f"{rel} uses obsolete .agent-skills path")


def validate_templates(root: Path, errors: list[str]) -> None:
    for rel, tokens in REQUIRED_TEMPLATE_TOKENS.items():
        path = root / rel
        if path.is_file():
            require_tokens(read_text(path), tokens, rel, errors)


def validate_evals(root: Path, errors: list[str]) -> None:
    prompts_path = root / "evals/prompts.csv"
    checks_path = root / "evals/expected_checks.yaml"
    if prompts_path.is_file():
        try:
            with prompts_path.open("r", encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"evals/prompts.csv is not valid CSV: {exc}")
            rows = []
        if len(rows) < 15:
            errors.append("evals/prompts.csv should contain at least 15 prompts")
        types = {row.get("review_type", "") for row in rows}
        for review_type in {"full", "focused", "negative"}:
            if review_type not in types:
                errors.append(f"evals/prompts.csv missing review_type: {review_type}")
        if not any(row.get("should_trigger") == "true" for row in rows):
            errors.append("evals/prompts.csv should include positive prompts")
        if not any(row.get("should_trigger") == "false" for row in rows):
            errors.append("evals/prompts.csv should include negative prompts")

    if checks_path.is_file():
        try:
            checks = parse_simple_yaml_lists(read_text(checks_path))
        except ValueError as exc:
            errors.append(f"evals/expected_checks.yaml is invalid: {exc}")
            return
        required_keys = {
            "must_include_for_full_review",
            "required_matrix_headers",
            "evidence_status_values",
            "risk_basis_values",
            "intensity_labels",
            "must_not_assert_without_evidence",
            "negative_prompts_should_not_focus_on",
            "expected_default_order",
        }
        missing = sorted(required_keys - checks.keys())
        if missing:
            errors.append(f"evals/expected_checks.yaml missing keys: {', '.join(missing)}")
        for token in FULL_REVIEW_SECTIONS:
            if token not in checks.get("expected_default_order", []):
                errors.append(f"evals/expected_checks.yaml missing output-order token: {token}")


def validate_examples(root: Path, errors: list[str]) -> None:
    examples = [
        "examples/campus-energy-system/expected-output-chat.md",
        "examples/yolo-pv-defect-detection/expected-output-chat.md",
        "examples/github-skill-review/expected-output-chat.md",
    ]
    for rel in examples:
        path = root / rel
        if not path.is_file():
            continue
        text = read_text(path)
        require_tokens(text, [*FULL_REVIEW_SECTIONS, *MATRIX_HEADERS], rel, errors)
        if not any(label in text for label in EVIDENCE_STATUSES):
            errors.append(f"{rel} does not contain an evidence-status value")
        if not any(label in text for label in RISK_BASES):
            errors.append(f"{rel} does not contain a risk-basis value")
        assert_order(text, FULL_REVIEW_SECTIONS, rel, errors)

    combined = "\n".join(read_text(root / rel) for rel in examples if (root / rel).is_file())
    for fabricated in ["数据来自真实校园运行", "用户个人负责全部模型设计"]:
        if fabricated in combined:
            errors.append(f"Examples contain a known fabricated claim: {fabricated}")


def validate_packaging(root: Path, errors: list[str]) -> None:
    path = root / "pyproject.toml"
    if path.is_file():
        require_tokens(
            read_text(path),
            ["[build-system]", 'packages = ["scripts"]', 'license = "MIT"', "defense-skill-validate"],
            "pyproject.toml",
            errors,
        )


def validate_text_files(root: Path, errors: list[str]) -> None:
    unfinished_parts = [r"\bTO" + r"DO\b", r"\bplace" + r"holder\b", "Replace " + "with"]
    unfinished = re.compile("|".join(unfinished_parts), re.IGNORECASE)
    for path in collect_text_files(root):
        rel = path.relative_to(root).as_posix()
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            errors.append(f"File is not valid UTF-8 text: {rel}")
            continue
        if "\ufffd" in text:
            errors.append(f"File contains replacement characters: {rel}")
        if any(marker in text for marker in MOJIBAKE_MARKERS):
            errors.append(f"File appears to contain mojibake text: {rel}")
        if unfinished.search(text):
            errors.append(f"File contains unfinished template-marker text: {rel}")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"Missing required file: {rel}")
    validate_skill_md(root, errors)
    validate_branding(root, errors)
    validate_agent_compatibility(root, errors)
    validate_templates(root, errors)
    validate_evals(root, errors)
    validate_examples(root, errors)
    validate_packaging(root, errors)
    validate_text_files(root, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the defense-beating-simulator skill package.")
    parser.add_argument("path", nargs="?", help="Repository or skill root. Defaults to the current repository.")
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
