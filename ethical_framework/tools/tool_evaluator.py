"""
tool_evaluator.py — evaluate autonomous offensive AI tools against the
risk dimensions framework. Prints a Markdown comparison table and per-tool
deployment recommendation, and writes the same content to a file.
"""

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from framework.risk_dimensions import (  # noqa: E402
    ASSESSED_TOOLS, generate_comparison_table
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "results" / "tool_risk_assessments.md",
    )
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)

    body = ["## Autonomous Offensive AI Tool Risk Assessment\n"]
    body.append(generate_comparison_table(ASSESSED_TOOLS))
    body.append("\n### Individual Recommendations\n")
    for tool in ASSESSED_TOOLS:
        body.append(f"**{tool.tool_name}**: {tool.deployment_recommendation()}")
        if tool.notes:
            body.append(f"  _Notes: {tool.notes}_\n")

    text = "\n".join(body)
    args.output.write_text(text)
    print(text)
    print(f"\nReport written to: {args.output}")


if __name__ == "__main__":
    main()
