# Decision Framework — Autonomous Offensive AI

A short walk-through for deciding whether and how to deploy autonomous AI in
an offensive security context.

## Step 1 — Authorisation

> Is the target pre-authorised in writing?

If **no** → STOP. Do not proceed regardless of technical capability.

## Step 2 — Human availability

> Is a human available to confirm intrusive / irreversible actions?

If **no** → restrict the agent to passive recon only (no probes that touch
the target beyond TCP connect).

## Step 3 — Reversibility

> Is the proposed action reversible (no data write, no service disruption)?

If **no** → require explicit human confirmation per action.

## Step 4 — Scope

> Does the action stay within the authorised services / hosts?

If **no** → STOP. Log a scope violation. Investigate.

## Step 5 — Auditability

> Is every action being logged in a tamper-evident way?

If **no** → STOP. Auditability is non-negotiable.

If all five gates pass, proceed.

## Notes on the legal layer

This framework does not replace legal review. The Computer Misuse Act (UK),
CFAA (US), GDPR, and EU AI Act all impose obligations that are not captured by
operational gates alone.
