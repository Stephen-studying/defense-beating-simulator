<div align="center">

# Project Defense Red-Team Skill

**A portable Agent Skill for evidence-gap review and high-pressure project-defense questions.**

Review the evidence behind project claims before generating defense questions, safe answers, and material repair actions.

![license](https://img.shields.io/badge/license-MIT-111827)
![skill](https://img.shields.io/badge/type-Agent%20Skill-2563eb)
![agent](https://img.shields.io/badge/install-Codex%20%7C%20Generic%20%7C%20Project-16a34a)
![language](https://img.shields.io/badge/language-English%20%7C%20%E4%B8%AD%E6%96%87-0f766e)

[Install](#install) ·
[Example](#example) ·
[Workflow](#workflow) ·
[Repository Structure](#repository-structure) ·
[中文](README.md)

</div>

---

- Package name: `defense-beating-simulator`.
- This repository is not a generic defense-question generator.
- It is a portable Agent Skill for reviewing project defense materials through a claim-evidence-risk workflow.
- It works with Codex, project-level instruction agents, generic local agents, and custom-prompt agents that can read Markdown instructions.
- By default, it returns structured feedback in chat. It only exports Markdown files when the user explicitly asks for files.

## Workflow

```text
Claims -> Evidence -> Gaps -> Risks -> Follow-up questions -> Safe answers -> Material repairs
```

The skill does not invent data sources, experimental results, deployment status, code features, or personal contributions. It helps users state project boundaries honestly and defensibly.

## What It Does

| Capability | Purpose |
| --- | --- |
| Claim-Evidence Matrix | Check whether each project claim is supported by README, report, slides, code, data notes, or result figures |
| High-risk Question Chains | Generate follow-up questions around data source, contribution, novelty, project boundary, and reproducibility |
| Safe Answer Strategies | Use boundary-aware answers that avoid overclaiming |
| Material Repair Actions | Suggest concrete fixes for README, slides, reports, demo scripts, and resume wording |
| Defense Cheatsheet | Summarize pitch, contributions, highlights, limitations, and high-frequency questions |

## Universal Agent Entrypoints

| Agent type | Recommended entrypoint |
| --- | --- |
| Codex / OpenAI Skill | `SKILL.md` + `agents/openai.yaml` |
| Generic local agent | `AGENTS.md` -> `SKILL.md` |
| Claude-like agent | `CLAUDE.md` -> `AGENTS.md` -> `SKILL.md` |
| Gemini-like agent | `GEMINI.md` -> `AGENTS.md` -> `SKILL.md` |
| Custom prompt agent | Attach or paste `SKILL.md` |
| Project-local agent | Place this repo under `.agents/skills/defense-beating-simulator` |

## Best For

- Course design, capstone, and undergraduate practice projects
- Research prototypes, competition projects, and algorithm experiments
- Resume projects, graduate interviews, and technical interviews
- GitHub project review, README review, and reproducibility checks

## Not For

- Pure speech polishing
- Generic interview practice without project materials
- Career advice unrelated to project evidence
- Replacing advisor feedback or real committee evaluation

## Example

```text
Use defense-beating-simulator to review my project defense materials.
Focus on project positioning, data source, personal contribution,
novelty risk, and missing evidence in README / slides / report.
```

Red-team mode:

```text
Simulate a strict defense committee. Start with a Claim-Evidence Matrix,
then identify high-risk gaps, ask three levels of follow-up questions for each gap,
and finally provide safe answers and material repair actions.
Do not invent information that is not present in my materials.
```

## Install

### Codex

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex -Force
```

```bash
sh install.sh --agent codex --force
```

### Generic local agents

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent generic -Force
```

```bash
sh install.sh --agent generic --force
```

### Project-local agents

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent project -Destination "D:\YourProject\.agents\skills" -Force
```

```bash
sh install.sh --agent project --dest "$HOME/your-project/.agents/skills" --force
```

Use a target project directory outside this repository. Do not install project mode into a child directory of this source repository.

## Repository Structure

```text
defense-beating-simulator/
├── SKILL.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── agents/openai.yaml
├── references/
├── assets/
├── examples/
├── evals/
├── scripts/
├── tests/
├── install.ps1
└── install.sh
```

## Validate

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```
