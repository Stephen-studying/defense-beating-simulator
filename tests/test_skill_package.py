from __future__ import annotations

import csv
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillPackageTests(unittest.TestCase):
    def test_validation_script_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skill.py"), str(ROOT)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Validation passed", result.stdout)

    def test_skill_entrypoint_has_red_team_contract(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for token in [
            "## When to use",
            "## Do not use",
            "## Claim-Evidence Matrix",
            "## Evidence labeling rules",
            "Material-supported",
            "Material-implied",
            "Material-missing",
            "Risk-inferred",
            "项目一句话定位",
            "高风险缺口 Top 5",
        ]:
            self.assertIn(token, skill)
        self.assertNotIn("非专业观众", skill)

    def test_domain_references_exist(self) -> None:
        for name in [
            "domain-ai-projects.md",
            "domain-web-showcase.md",
            "domain-engineering-simulation.md",
            "domain-course-design.md",
            "domain-research-prototype.md",
        ]:
            self.assertTrue((ROOT / "references" / name).is_file(), name)

    def test_templates_include_delivery_structure(self) -> None:
        checks = {
            "project-summary.template.md": "Claim-Evidence Summary",
            "question-bank.template.md": "High-risk Question Chains",
            "weakness-report.template.md": "Safe Answer Bank",
            "defense-cheatsheet.template.md": "Three Things Not to Overclaim",
        }
        for name, token in checks.items():
            text = (ROOT / "assets" / name).read_text(encoding="utf-8")
            self.assertIn(token, text, name)

    def test_examples_and_evals_exist(self) -> None:
        required = [
            "CLAUDE.md",
            "GEMINI.md",
            "README.en.md",
            "examples/campus-energy-system/input-project-summary.md",
            "examples/campus-energy-system/expected-output-chat.md",
            "examples/yolo-pv-defect-detection/input-project-summary.md",
            "examples/yolo-pv-defect-detection/expected-output-chat.md",
            "evals/prompts.csv",
            "evals/expected_checks.yaml",
            "evals/README.md",
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_universal_agent_entrypoints_are_documented(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Universal agent compatibility", agents)
        self.assertIn("CLAUDE.md", agents)
        self.assertIn("GEMINI.md", agents)
        self.assertIn(".agents/skills", agents)

        for rel in ["CLAUDE.md", "GEMINI.md"]:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn("AGENTS.md", text)
            self.assertIn("SKILL.md", text)
            self.assertIn("Claim-Evidence Matrix", text)

        openai_yaml = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "项目答辩红队审查器"', openai_yaml)

    def test_evals_include_positive_and_negative_prompts(self) -> None:
        with (ROOT / "evals" / "prompts.csv").open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertGreaterEqual(len(rows), 10)
        self.assertTrue(any(row["should_trigger"] == "true" for row in rows))
        self.assertTrue(any(row["should_trigger"] == "false" for row in rows))
        self.assertTrue(any("Claim-Evidence Matrix" in row["expected_sections"] for row in rows))


if __name__ == "__main__":
    unittest.main()
