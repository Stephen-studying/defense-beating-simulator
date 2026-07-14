# 针对性答辩模拟器

Use this file as a thin Claude project-context entrypoint.

When the user asks for project-defense review, graduate-interview questioning, evidence-gap analysis, answer scoring, or material repair:

1. Read `SKILL.md` as the canonical workflow.
2. Load only the relevant files from `references/`.
3. Return the mandatory evidence-first structure directly in chat.
4. Use `assets/` only when the user explicitly requests exported files.

For automatic Claude Code skill discovery, install this directory under `~/.claude/skills/defense-beating-simulator` or `.claude/skills/defense-beating-simulator`. Merely keeping this file inside another skill directory does not guarantee discovery.

Never invent data, results, code capabilities, deployment status, or personal contribution.
