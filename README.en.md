<div align="center">

# Targeted Defense Simulator

**A project-defense red-team skill for evidence review, follow-up questioning, and answer preparation.**

Audit the evidence behind project claims before generating questions, safe answers, and repair actions.

[![License](https://img.shields.io/badge/license-MIT-111827)](LICENSE)
[![Type](https://img.shields.io/badge/type-Agent%20Skill-2563eb)](SKILL.md)
[![Agents](https://img.shields.io/badge/agents-Codex%20%7C%20Claude%20%7C%20Gemini%20%7C%20Copilot-16a34a)](#compatibility)

[What it does](#what-it-does) · [Quick start](#quick-start) · [Install](#install) · [Compatibility](#compatibility) · [中文](README.md)

</div>

---

Package and skill ID: `defense-beating-simulator`

Chinese display name: `针对性答辩模拟器`

This is not a generic defense-question generator. It starts by checking whether README files, slides, reports, code structure, data notes, and result figures can support the project's claims.

```text
Claims → Evidence → Gaps → Risks → Follow-up questions → Safe answers → Material repairs
```

The default output is structured chat feedback. Files are exported only when the user explicitly requests them.

## What It Does

1. Builds a Claim-Evidence Matrix with separate evidence-status and risk-basis labels.
2. Ranks up to five material gaps that are most likely to hurt the defense.
3. Generates two-to-four-level follow-up chains tied to those gaps.
4. Produces boundary-aware answers without inventing data, results, features, or contributions.
5. Gives concrete repair actions for README files, slides, reports, demos, and resumes.
6. Scores the user's draft answer and rewrites unsupported or evasive wording.

Full reviews use this order:

1. One-sentence project positioning
2. Claim-Evidence Matrix
3. Top high-risk gaps
4. Follow-up question chains
5. Safe answer strategies
6. Material repair checklist
7. Defense cheatsheet

Evidence status uses `Material-supported`, `Material-implied`, or `Material-missing`. Risk basis uses `Material-derived` or `Risk-inferred`; inferred risks must never be presented as material facts.

## Quick Start

```text
Use defense-beating-simulator to review my project defense materials.
Start with a Claim-Evidence Matrix, identify the highest-risk gaps,
ask three levels of follow-up questions, then provide safe answers and repair actions.
Do not invent information that is absent from my materials.
```

Questioning intensity can be selected as `先热个身` (warm-up), `开始挑刺` (standard review), or `严刑拷打` (high-pressure review). Intensity changes tone and depth, not the evidence standard.

## Best For

- Course projects, capstones, and undergraduate design work
- Research prototypes, competitions, and machine-learning projects
- Graduate interviews, resume-project interviews, and technical interviews
- GitHub README, reproducibility, and project-boundary reviews

## Not For

- Pure speech polishing or generic interview questions
- Career advice without project materials
- General academic explanations unrelated to project evidence
- Replacing advisor feedback or a real committee decision

## Compatibility

The repository is a portable `SKILL.md` project rather than a Codex-only package. Automatic discovery still depends on each agent and version.

| Agent or convention | Default directory | Installer mode |
| --- | --- | --- |
| Codex | `~/.codex/skills` | `codex` |
| Shared Agent Skills | `~/.agents/skills` | `agents` |
| Claude Code | `~/.claude/skills` | `claude` |
| Gemini CLI | `~/.gemini/skills` | `gemini` |
| GitHub Copilot CLI | `~/.copilot/skills` | `copilot` |
| Project-local | `<project>/.agents/skills` | `project` |

These locations follow the official [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/), and [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) documentation.

If discovery fails, explicitly mention `defense-beating-simulator` or ask the agent to read:

```text
AGENTS.md → SKILL.md → the relevant file under references/
```

The legacy `generic` mode remains an alias for `agents` and uses `~/.agents/skills`.

## Install

```bash
git clone https://github.com/Stephen-studying/defense-beating-simulator.git
cd defense-beating-simulator
```

Windows:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex -Force
# Or use: agents / claude / gemini / copilot
```

macOS or Linux:

```bash
sh install.sh --agent codex --force
# Or use: agents / claude / gemini / copilot
```

Gemini CLI also supports native installation from the repository:

```bash
gemini skills install https://github.com/Stephen-studying/defense-beating-simulator
```

Project-local installation requires an explicit destination outside this source repository:

```bash
sh install.sh --agent project --dest "$HOME/your-project/.agents/skills" --force
```

Installers copy only runtime files: `SKILL.md`, agent entrypoints, `references/`, `assets/`, metadata, and the license.

## Repository Structure

```text
SKILL.md              Canonical behavior contract
AGENTS.md             Cross-agent entrypoint and discovery notes
CLAUDE.md / GEMINI.md Thin platform entrypoints
references/           Shared and domain-specific review knowledge
assets/               Optional export templates
examples/             Grounded example inputs and outputs
evals/                Trigger and output regression cases
scripts/              Package and captured-response validators
tests/                Standard-library tests
```

## Validate

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
python scripts/evaluate_response.py --eval-id explicit_01 --response response.md
```

GitHub Actions validates the package, Python installation, unit tests, and runtime-only installers on Linux and Windows.

## Limitations

- The skill cannot verify facts absent from the supplied materials.
- It must not invent data sources, results, deployment status, code behavior, or personal contributions.
- A showcase demo must not be represented as a deployed system.
- The output is a preparation aid, not a guarantee of defense success.

## License

[MIT License](LICENSE)
