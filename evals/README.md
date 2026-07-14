# Skill Evals

This directory contains regression prompts for trigger coverage and output-contract checks.

## What is automated

- `scripts/validate_skill.py` parses `prompts.csv` and `expected_checks.yaml` with the Python standard library.
- Unit tests verify positive, focused, and negative prompts; matrix headers; evidence/risk labels; output order; examples; and installation metadata.
- `scripts/evaluate_response.py` can check a captured Agent response against one eval row.

Example:

```bash
python scripts/evaluate_response.py --eval-id explicit_01 --response response.md
```

## What still requires a live Agent

These checks do not call a model in CI. Before a release, run at least one campus-energy prompt and one AI-project prompt in fresh Agent sessions, save the responses, and evaluate them with the script. A full review must contain all seven sections in order; a focused review may return only the relevant evidence row and requested coaching.

Do not treat a green structural CI run as proof that every Agent host will trigger or follow the skill identically.
