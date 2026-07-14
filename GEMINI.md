# 针对性答辩模拟器

Use this file as a thin Gemini project-context entrypoint.

When the user asks for project-defense review, graduate-interview questioning, evidence-gap analysis, answer scoring, or material repair:

1. Read `SKILL.md` as the canonical workflow.
2. Load only the relevant files from `references/`.
3. Return the mandatory evidence-first structure directly in chat.
4. Use `assets/` only when the user explicitly requests exported files.

For Gemini CLI discovery, install this directory under `~/.gemini/skills/defense-beating-simulator`, `~/.agents/skills/defense-beating-simulator`, or the matching project-level directory.

Never invent data, results, code capabilities, deployment status, or personal contribution.
