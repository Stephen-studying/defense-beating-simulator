from __future__ import annotations

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

    def test_skill_entrypoint_mentions_material_focus(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("答辩材料审查者", skill)
        self.assertIn("README, report, PPT, code structure, data notes, figures", skill)
        self.assertNotIn("非专业观众", skill)

    def test_question_patterns_deprioritize_public_science(self) -> None:
        patterns = (ROOT / "references" / "question-patterns.md").read_text(encoding="utf-8")
        self.assertIn("should not turn into public-science communication coaching", patterns)
        self.assertIn("Prioritize questions grounded in the user's README", patterns)

    def test_templates_exist(self) -> None:
        for name in [
            "project-summary.template.md",
            "question-bank.template.md",
            "weakness-report.template.md",
            "defense-cheatsheet.template.md",
        ]:
            self.assertTrue((ROOT / "assets" / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
