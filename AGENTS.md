# 针对性答辩模拟器 Agent Instructions

Use this repository as a portable Project Defense Red-Team Skill. It works automatically only in agents that support `SKILL.md` discovery; other agents can still use it by reading the Markdown entrypoints explicitly.

## Canonical entrypoints

- `SKILL.md`: canonical workflow and trigger metadata.
- `AGENTS.md`: cross-agent orientation and repository-level instructions.
- `agents/openai.yaml`: OpenAI/Codex UI metadata only.
- `CLAUDE.md` and `GEMINI.md`: thin project-context entrypoints, not substitutes for installing `SKILL.md` into the agent's supported skill directory.

## Supported discovery paths

| Agent host | User-level skill root | Project-level skill root |
| --- | --- | --- |
| Codex | `~/.codex/skills` | Agent-specific project configuration |
| Shared Agent Skills alias | `~/.agents/skills` | `.agents/skills` |
| Claude Code | `~/.claude/skills` | `.claude/skills` |
| Gemini CLI | `~/.gemini/skills` or `~/.agents/skills` | `.gemini/skills` or `.agents/skills` |
| GitHub Copilot | `~/.copilot/skills` or `~/.agents/skills` | `.github/skills`, `.claude/skills`, or `.agents/skills` |

Do not describe one neutral directory as universally discoverable. When automatic discovery is unavailable, ask the agent to read `SKILL.md` explicitly.

## Installation modes

- `codex`: install under `CODEX_HOME/skills` or `~/.codex/skills`.
- `agents` or legacy alias `generic`: install under `AGENT_SKILLS_HOME` or `~/.agents/skills`.
- `claude`: install under `~/.claude/skills`.
- `gemini`: install under `~/.gemini/skills`.
- `copilot`: install under `~/.copilot/skills`.
- `project`: install into a caller-provided project skill root.

The install scripts copy only runtime files: `SKILL.md`, compatibility entrypoints, `agents/`, `references/`, `assets/`, and `LICENSE`. Development files such as README, examples, evals, tests, CI, and packaging metadata must not be copied into an installed skill.

## Required behavior

- Return structured feedback directly in chat unless the user requests file export.
- For every full review, use the seven-section order defined in `SKILL.md`, including in `严刑拷打` mode.
- Start from a Claim-Evidence Matrix with separate `Evidence status` and `Risk basis` columns.
- Include only claims present in the material or the user's own wording.
- Mark reviewer inferences as `Risk-inferred`.
- Use at most five high-risk gaps; never add filler to reach five.

## Resource routing

- Read one or more `references/domain-*.md` files based on project type.
- Read `references/question-patterns.md` for role-specific follow-up chains.
- Read `references/project-rubrics.md` for scoring, safe wording, contribution, novelty, and risk ranking.
- Use `assets/*.template.md` only when the user explicitly asks for exported Markdown.

## Safety

- Do not fabricate data sources, experiment results, code features, deployment status, or personal contributions.
- Do not describe a showcase as a deployed system or course assumptions as measured data.
- Do not turn team work into individual work or model modification into unsupported originality.
- Use material-aware boundary statements instead of confident but unsupported claims.
