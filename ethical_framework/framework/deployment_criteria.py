"""
deployment_criteria.py — checklist-based readiness check for autonomous
offensive AI tools. Reads a JSON config describing a tool's controls and
prints / returns whether the tool meets the deployment baseline.
"""

import argparse
import json
import sys
from pathlib import Path


# Each criterion = (key, human-readable name, weight). Weight 2 = mandatory.
CRITERIA = [
    ("authorised_targets_only", "Hard allow-list of authorised targets", 2),
    ("human_confirmation_for_active", "Human confirmation gate before active actions", 2),
    ("audit_log",                 "Tamper-evident audit log of all actions", 2),
    ("scope_enforcement",         "Runtime scope enforcement (refuses out-of-scope)", 2),
    ("rollback_plan",             "Rollback / containment plan for unintended actions", 1),
    ("rate_limited",              "Rate limits on outbound network actions", 1),
    ("read_only_default",         "Read-only by default; write requires uplift", 1),
    ("redteam_review",            "Independent red-team review of the agent", 1),
]


def evaluate(config: dict) -> dict:
    score = 0
    max_score = 0
    failures = []

    for key, name, weight in CRITERIA:
        max_score += weight
        if config.get(key) is True:
            score += weight
        else:
            failures.append((name, weight))

    pct = round(100 * score / max_score, 1) if max_score else 0
    mandatory_pass = all(config.get(k) for k, _, w in CRITERIA if w == 2)

    if mandatory_pass and pct >= 80:
        verdict = "READY — supervised production deployment acceptable"
    elif mandatory_pass:
        verdict = "PARTIAL — mandatory controls present; tighten optional controls"
    else:
        verdict = "NOT READY — one or more mandatory controls missing"

    return {
        "score": score,
        "max_score": max_score,
        "percent": pct,
        "mandatory_pass": mandatory_pass,
        "verdict": verdict,
        "failures": failures,
    }


def print_report(result: dict) -> None:
    print(f"Score: {result['score']}/{result['max_score']} ({result['percent']}%)")
    print(f"Mandatory controls: {'PASS' if result['mandatory_pass'] else 'FAIL'}")
    print(f"Verdict: {result['verdict']}")
    if result["failures"]:
        print("\nMissing / failing criteria:")
        for name, weight in result["failures"]:
            tag = "MANDATORY" if weight == 2 else "optional"
            print(f"  [{tag}] {name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=Path,
        help="Path to a JSON config describing the tool's controls. "
             "If omitted, runs against a built-in example config.",
    )
    args = parser.parse_args()

    if args.config and args.config.exists():
        cfg = json.loads(args.config.read_text())
    else:
        # Built-in example: a fairly mature tool, missing red-team review.
        cfg = {
            "authorised_targets_only": True,
            "human_confirmation_for_active": True,
            "audit_log": True,
            "scope_enforcement": True,
            "rollback_plan": True,
            "rate_limited": True,
            "read_only_default": True,
            "redteam_review": False,
        }
        print("(no --config supplied — using built-in example)\n")

    print_report(evaluate(cfg))


if __name__ == "__main__":
    main()
