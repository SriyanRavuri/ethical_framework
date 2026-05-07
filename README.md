# Ethical & Safety Risk Framework for Autonomous Offensive AI

A structured, runnable framework for evaluating when autonomous AI should and
should not be used in offensive security contexts. Includes:

- A six-dimension **risk scoring rubric** (`framework/risk_dimensions.py`)
- A short **decision walk-through** (`framework/decision_framework.md`)
- A **deployment readiness check** (`framework/deployment_criteria.py`)
- A **tool evaluator** that runs the rubric on three real-world tools
  (`tools/tool_evaluator.py`)

## Risk dimensions

| Dimension | Description |
|-----------|-------------|
| Scope creep | Agent acts outside pre-authorised boundaries |
| Unintended damage | Actions cause data loss or service disruption |
| False-positive exploitation | Agent acts on incorrect vulnerability assessment |
| Legal liability | GDPR, EU AI Act, Computer Misuse Act, CFAA |
| Human oversight | When and how humans must remain in the loop |
| Auditability | Whether actions can be traced, explained, reviewed |

The decision flow is documented in `framework/decision_framework.md`.

## Project layout

```
03_ethical_framework/
├── framework/
│   ├── decision_framework.md
│   ├── deployment_criteria.py
│   └── risk_dimensions.py
├── tools/
│   └── tool_evaluator.py
├── results/
├── requirements.txt
└── README.md
```

## Setup

```bash
cd 03_ethical_framework

python -m venv .venv
source .venv/bin/activate              # Linux / macOS
# .venv\Scripts\Activate.ps1            # Windows PowerShell

pip install -r requirements.txt
```

This project has no API or dataset dependencies — it's pure Python.

## Run it

Three things to run:

```bash
# 1. Print the risk-dimensions table for the three pre-assessed tools
python framework/risk_dimensions.py

# 2. Run the deployment readiness check (against the built-in example config)
python framework/deployment_criteria.py

# 3. Run the tool evaluator and write a Markdown report to results/
python tools/tool_evaluator.py
```

You can supply your own tool config to the readiness check:

```bash
python framework/deployment_criteria.py --config my_tool.json
```

A minimal config looks like:

```json
{
  "authorised_targets_only": true,
  "human_confirmation_for_active": true,
  "audit_log": true,
  "scope_enforcement": true,
  "rollback_plan": false,
  "rate_limited": true,
  "read_only_default": true,
  "redteam_review": false
}
```
