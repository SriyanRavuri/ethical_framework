## Autonomous Offensive AI Tool Risk Assessment

| Tool | Scope Creep | Unint. Damage | FP Exploit | Legal Risk | Oversight | Auditability | Net Risk | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PentestGPT | 2 | 2 | 3 | 2 | 4 | 3 | 1.0 | MEDIUM RISK — Suitable for controlled research environments only |
| AutoAttacker (research prototype) | 4 | 3 | 4 | 4 | 2 | 2 | 5.5 | CRITICAL RISK — Not recommended for deployment outside isolated lab environments |
| HackingBuddyGPT | 3 | 2 | 3 | 3 | 3 | 3 | 2.5 | HIGH RISK — Research use with strict human oversight required at every step |

### Individual Recommendations

**PentestGPT**: MEDIUM RISK — Suitable for controlled research environments only
  _Notes: Human-in-the-loop by design; risk mainly from over-confident recommendations_

**AutoAttacker (research prototype)**: CRITICAL RISK — Not recommended for deployment outside isolated lab environments
  _Notes: Highly autonomous; limited scope enforcement; research-only_

**HackingBuddyGPT**: HIGH RISK — Research use with strict human oversight required at every step
  _Notes: Moderate autonomy; designed for CTF/lab use; needs scope hardening for enterprise_
