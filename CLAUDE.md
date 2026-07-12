# 项目答辩红队审查器

This repository is a portable Agent Skill for project defense red-team review.

Use this file as a thin compatibility entrypoint. The canonical instructions are:

1. Read `AGENTS.md` first for cross-agent operating rules.
2. Read `SKILL.md` for the complete defense-review workflow.
3. Load files from `references/` only when the project type requires them.
4. Use `assets/` templates only when the user explicitly asks to export Markdown files.

Default behavior: return structured feedback directly in chat, starting with a Claim-Evidence Matrix. Do not invent data sources, experiment results, deployment status, code features, or personal contributions.
