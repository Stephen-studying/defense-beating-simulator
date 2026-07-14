from __future__ import annotations

import argparse
import csv
from pathlib import Path

try:
    from scripts.validate_skill import parse_simple_yaml_lists
except ModuleNotFoundError:  # Allow `python scripts/evaluate_response.py`.
    from validate_skill import parse_simple_yaml_lists


NEGATION_MARKERS = ("不", "未", "没有", "不能", "不要", "尚未", "避免", "并非", "不得")


def split_expected(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def find_eval(root: Path, eval_id: str) -> dict[str, str]:
    with (root / "evals/prompts.csv").open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("id") == eval_id:
                return row
    raise ValueError(f"Unknown eval id: {eval_id}")


def check_order(text: str, tokens: list[str]) -> list[str]:
    positions = [text.find(token) for token in tokens]
    if any(position < 0 for position in positions):
        return []
    if positions != sorted(positions):
        return ["Required sections are not in the expected order"]
    return []


def find_unqualified_overclaims(text: str, phrases: list[str]) -> list[str]:
    errors: list[str] = []
    for phrase in phrases:
        start = 0
        while True:
            index = text.find(phrase, start)
            if index < 0:
                break
            prefix = text[max(0, index - 12) : index]
            if not any(marker in prefix for marker in NEGATION_MARKERS):
                errors.append(f"Potential unsupported assertion: {phrase}")
                break
            start = index + len(phrase)
    return errors


def evaluate(root: Path, row: dict[str, str], response: str) -> list[str]:
    checks = parse_simple_yaml_lists((root / "evals/expected_checks.yaml").read_text(encoding="utf-8"))
    errors: list[str] = []
    review_type = row.get("review_type", "")

    for token in split_expected(row.get("expected_sections", "")):
        if token not in response:
            errors.append(f"Missing eval-specific content: {token}")

    if review_type == "full":
        for token in checks["must_include_for_full_review"]:
            if token not in response:
                errors.append(f"Missing full-review section: {token}")
        errors.extend(check_order(response, checks["expected_default_order"]))
        for header in checks["required_matrix_headers"]:
            if header not in response:
                errors.append(f"Missing matrix header: {header}")
        if not any(label in response for label in checks["evidence_status_values"]):
            errors.append("No evidence-status label found")
        if not any(label in response for label in checks["risk_basis_values"]):
            errors.append("No risk-basis label found")
        errors.extend(find_unqualified_overclaims(response, checks["must_not_assert_without_evidence"]))
    elif review_type == "negative":
        for token in checks["negative_prompts_should_not_focus_on"]:
            if token in response:
                errors.append(f"Negative prompt incorrectly focused on: {token}")
    elif review_type != "focused":
        errors.append(f"Unknown review_type: {review_type}")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate one captured Agent response against a skill eval row.")
    parser.add_argument("--eval-id", required=True, help="ID from evals/prompts.csv")
    parser.add_argument("--response", required=True, help="UTF-8 text or Markdown response file")
    parser.add_argument("--root", help="Repository root; defaults to the current working directory")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    row = find_eval(root, args.eval_id)
    response = Path(args.response).read_text(encoding="utf-8")
    errors = evaluate(root, row, response)
    if errors:
        print(f"Evaluation failed for {args.eval_id}:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Evaluation passed for {args.eval_id}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
