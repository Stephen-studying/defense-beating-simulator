# 项目答辩红队审查器 Agent Instructions

Use this repository as a portable local agent skill for project defense red-team review. It is not Codex-only.

## Entrypoints

- `AGENTS.md` for generic local agents that read project-level instructions.
- `SKILL.md` for Codex/OpenAI Skill-compatible agents or any agent that can load detailed skill instructions.
- `agents/openai.yaml` for Codex UI metadata only.
- `CLAUDE.md` and `GEMINI.md` are thin compatibility entrypoints for agents that prefer product-specific project instruction filenames.

## Universal agent compatibility

This skill is plain Markdown plus optional templates. It does not require a Codex-only runtime.

- If the agent supports a local skill directory, copy this repository into that directory and ask the agent to use `defense-beating-simulator`.
- If the agent supports project-level instruction files, keep this repository in the project and ask the agent to read `AGENTS.md` first.
- If the agent only supports custom prompts, paste or attach `SKILL.md` as the workflow instruction and load relevant files from `references/` only when needed.
- If the agent has no automatic discovery, explicitly say: "Use the rules in `AGENTS.md` and `SKILL.md` from this repository."

## Installation modes

- Codex mode copies the skill to `CODEX_HOME/skills` or `~/.codex/skills`.
- Generic mode copies the skill to `AGENT_SKILLS_HOME` or `~/.agent-skills`.
- Project mode can copy the skill into a project-local `.agents/skills` directory when a tool expects project-scoped skills.
- Agents without skill auto-discovery can still use this repository by reading `AGENTS.md` first and `SKILL.md` for the full workflow.

## Default behavior

- Return structured feedback directly in the conversation.
- Start with a Claim-Evidence Matrix before generating hard questions.
- Do not create Markdown files by default.
- Create files only when the user explicitly asks to export, save, or generate a Markdown package.

## Supporting resources

- `references/question-patterns.md` for role-based questions, high-pressure follow-up chains, and defense-material question patterns.
- `references/project-rubrics.md` for risk ranking, answer scoring, data-source defense, contribution wording, and innovation reframing.
- `references/domain-*.md` for project-type-specific red-team questions.
- `assets/*.template.md` only when the user requests exported Markdown files.

## Operating rules

- Ground all questions and answers in the supplied README, report, PPT text, code structure, data notes, figures, experiment tables, screenshots, or project summary.
- Label important claims as `Material-supported`, `Material-implied`, `Material-missing`, or `Risk-inferred`.
- Mark missing evidence as material not provided instead of inventing details.
- Do not fabricate data sources, experiment results, code features, deployment status, or personal contributions.
- Do not describe a showcase demo as a real deployed system unless the material proves it.
- Do not turn team work into individual work.
- Keep humorous intensity labels such as `严刑拷打` as optional UI wording, but keep the actual questions professional and evidence-based.
- Make the first response useful without file output: project positioning, Claim-Evidence Matrix, high-risk gaps, answer strategy, and concrete material repair actions.
