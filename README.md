<div align="center">

# 答辩挨打模拟器

**Defense Beating Simulator**

A Codex Skill for turning project materials into defense questions, weak-point reports, and safe answers.

![Skill](https://img.shields.io/badge/Codex-Skill-111827)
![Python](https://img.shields.io/badge/Python-3.9%2B-2563EB)
![License](https://img.shields.io/badge/License-MIT-16A34A)

</div>

## Focus

This is not a public-speaking coach. It stress-tests the material that will actually be judged:

- README and project positioning
- report, PPT, figures, and result claims
- code structure and implementation evidence
- data source, assumptions, metrics, and limitations
- personal contribution, project boundary, and risky wording

## Output

- `project-summary.md`: what the project says and what the material supports
- `question-bank.md`: role-based questions with risk labels
- `weakness-report.md`: high-risk gaps and repair actions
- `defense-cheatsheet.md`: one-page final prep card

## Intensity

```text
先热个身 / 开始挑刺 / 严刑拷打
```

| Mode | Use for |
| --- | --- |
| 先热个身 | basic understanding and low-pressure rehearsal |
| 开始挑刺 | normal defense questioning across data, method, result, and contribution |
| 严刑拷打 | high-pressure red-team review of the easiest places to lose points |

## Install

PowerShell:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex -Force
```

POSIX shell:

```bash
sh install.sh --agent codex --force
```

Then restart Codex and invoke:

```text
Use $defense-beating-simulator to analyze my project README in graduate-interview mode, intensity "严刑拷打".
```

## Validate

No third-party dependency is required.

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```

## Structure

```text
SKILL.md                 Skill entrypoint
AGENTS.md                Generic-agent entrypoint
references/              Question patterns and scoring rubrics
assets/                  Output templates
scripts/validate_skill.py Dependency-free package validator
tests/                   Smoke tests
```
