# Production Safety Policy

- Never print or expose production secrets.
- Never run destructive production commands without explicit authorization.
- Do not use production data as a casual test fixture.
- Assess migration compatibility, locks, data volume, queue behavior, and rollback.
- Prefer staged rollouts, backups, health checks, and observable deployment steps.
- Confirm the target environment before executing operations.
- If the environment is ambiguous, stop and ask.
