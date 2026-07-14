from __future__ import annotations

import csv
import subprocess
import sys
import unittest
from pathlib import Path

from scripts.evaluate_response import evaluate, find_eval
from scripts.validate_skill import (
    DISPLAY_NAME,
    EVIDENCE_STATUSES,
    FULL_REVIEW_SECTIONS,
    INTENSITY_LABELS,
    MANDATORY_OUTPUT_LABELS,
    MATRIX_HEADERS,
    RISK_BASES,
    parse_simple_yaml_lists,
)


ROOT = Path(__file__).resolve().parents[1]


class SkillPackageTests(unittest.TestCase):
    def test_validation_script_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/validate_skill.py"), str(ROOT)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Validation passed", result.stdout)

    def test_skill_entrypoint_has_complete_contract(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        required = [
            "## When to use",
            "## Do not use",
            "## Mandatory full-review output",
            "## Claim-Evidence Matrix",
            "## Evidence labeling rules",
            "## Answer scoring",
            "## Final self-check",
            "it is not automatically proof that the claim is true",
            "Material-derived + Risk-inferred",
            *MATRIX_HEADERS,
            *EVIDENCE_STATUSES,
            *RISK_BASES,
            *INTENSITY_LABELS,
        ]
        for token in required:
            self.assertIn(token, skill)

        positions = [skill.index(label) for label in MANDATORY_OUTPUT_LABELS]
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn("非专业观众", skill)

    def test_display_name_is_consistent(self) -> None:
        checks = {
            "README.md": f"# {DISPLAY_NAME}",
            "README.zh-CN.md": f"# {DISPLAY_NAME}",
            "SKILL.md": f"# {DISPLAY_NAME}",
            "AGENTS.md": f"# {DISPLAY_NAME}",
            "CLAUDE.md": f"# {DISPLAY_NAME}",
            "GEMINI.md": f"# {DISPLAY_NAME}",
            "agents/openai.yaml": f'display_name: "{DISPLAY_NAME}"',
            "pyproject.toml": f'display_name = "{DISPLAY_NAME}"',
        }
        for rel, token in checks.items():
            self.assertIn(token, (ROOT / rel).read_text(encoding="utf-8"), rel)

    def test_domain_references_exist(self) -> None:
        for name in [
            "domain-ai-projects.md",
            "domain-web-showcase.md",
            "domain-engineering-simulation.md",
            "domain-course-design.md",
            "domain-research-prototype.md",
        ]:
            self.assertTrue((ROOT / "references" / name).is_file(), name)

    def test_templates_include_evidence_and_delivery_structure(self) -> None:
        checks = {
            "project-summary.template.md": ["Claim-Evidence Summary", "Evidence status", "Risk basis"],
            "question-bank.template.md": ["High-risk Question Chains", "Evidence status", "Risk basis"],
            "weakness-report.template.md": ["Safe Answer Bank", "Evidence Status", "Risk Basis"],
            "defense-cheatsheet.template.md": ["Three Things Not to Overclaim", "Final 30-second Summary"],
        }
        for name, tokens in checks.items():
            text = (ROOT / "assets" / name).read_text(encoding="utf-8")
            for token in tokens:
                self.assertIn(token, text, name)

    def test_examples_follow_contract_without_known_fabrications(self) -> None:
        files = [
            ROOT / "examples/campus-energy-system/expected-output-chat.md",
            ROOT / "examples/yolo-pv-defect-detection/expected-output-chat.md",
            ROOT / "examples/github-skill-review/expected-output-chat.md",
        ]
        combined = ""
        for path in files:
            text = path.read_text(encoding="utf-8")
            combined += text
            positions = [text.index(section) for section in FULL_REVIEW_SECTIONS]
            self.assertEqual(positions, sorted(positions), path.name)
            for token in MATRIX_HEADERS:
                self.assertIn(token, text, path.name)
            self.assertTrue(any(token in text for token in EVIDENCE_STATUSES), path.name)
            self.assertTrue(any(token in text for token in RISK_BASES), path.name)
        self.assertNotIn("数据来自真实校园运行", combined)
        self.assertNotIn("用户个人负责全部模型设计", combined)

    def test_evals_cover_full_focused_and_negative_cases(self) -> None:
        with (ROOT / "evals/prompts.csv").open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertGreaterEqual(len(rows), 15)
        self.assertEqual({"full", "focused", "negative"}, {row["review_type"] for row in rows})
        self.assertTrue(any(row["should_trigger"] == "true" for row in rows))
        self.assertTrue(any(row["should_trigger"] == "false" for row in rows))

        checks = parse_simple_yaml_lists((ROOT / "evals/expected_checks.yaml").read_text(encoding="utf-8"))
        self.assertEqual(FULL_REVIEW_SECTIONS, checks["expected_default_order"])
        self.assertEqual(EVIDENCE_STATUSES, checks["evidence_status_values"])
        self.assertEqual(RISK_BASES, checks["risk_basis_values"])

    def test_example_passes_response_evaluator(self) -> None:
        row = find_eval(ROOT, "explicit_01")
        response = (ROOT / "examples/campus-energy-system/expected-output-chat.md").read_text(encoding="utf-8")
        self.assertEqual([], evaluate(ROOT, row, response))

    def test_agent_install_paths_and_runtime_scope(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        for path in ["~/.codex/skills", "~/.agents/skills", "~/.claude/skills", "~/.gemini/skills", "~/.copilot/skills"]:
            self.assertIn(path, agents)

        powershell = (ROOT / "install.ps1").read_text(encoding="utf-8")
        shell = (ROOT / "install.sh").read_text(encoding="utf-8")
        for text in [agents, powershell, shell]:
            self.assertNotIn(".agent-skills", text)
        for runtime_entry in ["SKILL.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "LICENSE", "agents", "references", "assets"]:
            self.assertIn(runtime_entry, powershell)
            self.assertIn(runtime_entry, shell)

    def test_packaging_metadata_has_explicit_package(self) -> None:
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        for token in ["[build-system]", 'packages = ["scripts"]', 'license = "MIT"', "defense-skill-validate"]:
            self.assertIn(token, pyproject)


if __name__ == "__main__":
    unittest.main()
