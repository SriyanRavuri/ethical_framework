"""
risk_dimensions.py — quantitative scoring of risk dimensions for autonomous offensive AI tools.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class RiskAssessment:
    tool_name: str
    scope_creep_risk: int          # 1 (low) to 5 (critical)
    unintended_damage_risk: int
    false_positive_exploitation: int
    legal_liability_risk: int
    human_oversight_adequacy: int  # 1 (poor) to 5 (excellent) — higher is better
    auditability: int              # 1 (poor) to 5 (excellent) — higher is better
    notes: Optional[str] = None

    def overall_risk_score(self) -> float:
        """
        Compute overall risk score.
        Risk dimensions are summed; safeguard dimensions (oversight, auditability) subtract.
        Higher score = higher net risk.
        """
        risk = (
            self.scope_creep_risk +
            self.unintended_damage_risk +
            self.false_positive_exploitation +
            self.legal_liability_risk
        )
        safeguards = self.human_oversight_adequacy + self.auditability
        return round((risk - safeguards) / 2, 2)

    def deployment_recommendation(self) -> str:
        score = self.overall_risk_score()
        if score <= 0:
            return "LOW RISK — Suitable for supervised enterprise deployment with standard controls"
        elif score <= 2:
            return "MEDIUM RISK — Suitable for controlled research environments only"
        elif score <= 4:
            return "HIGH RISK — Research use with strict human oversight required at every step"
        else:
            return "CRITICAL RISK — Not recommended for deployment outside isolated lab environments"

    def to_markdown_row(self) -> str:
        return (
            f"| {self.tool_name} "
            f"| {self.scope_creep_risk} "
            f"| {self.unintended_damage_risk} "
            f"| {self.false_positive_exploitation} "
            f"| {self.legal_liability_risk} "
            f"| {self.human_oversight_adequacy} "
            f"| {self.auditability} "
            f"| {self.overall_risk_score()} "
            f"| {self.deployment_recommendation()} |"
        )


# Pre-assessed tools based on published documentation and research
ASSESSED_TOOLS = [
    RiskAssessment(
        tool_name="PentestGPT",
        scope_creep_risk=2,
        unintended_damage_risk=2,
        false_positive_exploitation=3,
        legal_liability_risk=2,
        human_oversight_adequacy=4,
        auditability=3,
        notes="Human-in-the-loop by design; risk mainly from over-confident recommendations"
    ),
    RiskAssessment(
        tool_name="AutoAttacker (research prototype)",
        scope_creep_risk=4,
        unintended_damage_risk=3,
        false_positive_exploitation=4,
        legal_liability_risk=4,
        human_oversight_adequacy=2,
        auditability=2,
        notes="Highly autonomous; limited scope enforcement; research-only"
    ),
    RiskAssessment(
        tool_name="HackingBuddyGPT",
        scope_creep_risk=3,
        unintended_damage_risk=2,
        false_positive_exploitation=3,
        legal_liability_risk=3,
        human_oversight_adequacy=3,
        auditability=3,
        notes="Moderate autonomy; designed for CTF/lab use; needs scope hardening for enterprise"
    ),
]


def generate_comparison_table(assessments: list) -> str:
    headers = [
        "Tool", "Scope Creep", "Unint. Damage", "FP Exploit",
        "Legal Risk", "Oversight", "Auditability", "Net Risk", "Recommendation"
    ]
    header_row = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    rows = [a.to_markdown_row() for a in assessments]
    return "\n".join([header_row, separator] + rows)


if __name__ == "__main__":
    print("## Autonomous Offensive AI Tool Risk Assessment\n")
    print(generate_comparison_table(ASSESSED_TOOLS))
    print("\n### Individual Recommendations\n")
    for tool in ASSESSED_TOOLS:
        print(f"**{tool.tool_name}**: {tool.deployment_recommendation()}")
        if tool.notes:
            print(f"  Notes: {tool.notes}\n")
