# Skill Evals

This directory contains lightweight evaluation prompts for checking whether the skill is triggered in the right situations and whether the output contains the expected defense-review structure.

The evals are not automated model benchmarks. They are regression prompts for maintainers to manually or semi-automatically check behavior after changing `SKILL.md`, references, or templates.

## Files

- `prompts.csv`: trigger and non-trigger prompts across Chinese, English, README review, PPT review, resume project review, course design, AI projects, web demos, engineering simulation, and research prototypes.
- `expected_checks.yaml`: strings and behaviors that maintainers should check in triggered and non-triggered outputs.

## Review rule

A triggered output should start from evidence review, not from a generic list of questions.
