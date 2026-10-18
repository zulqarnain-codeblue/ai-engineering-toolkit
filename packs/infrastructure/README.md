# Pack: Infrastructure, CI/CD, and Production Operations

Use when modifying deployment, hosting, CI/CD, containers, secrets, or production infrastructure.

## Safety gates
- Inspect environment and deployment architecture before changes.
- Never expose secrets or print secret values.
- Do not run destructive production commands or modify live data without explicit authorization and a reviewed plan.
- Require backup/rollback planning for high-risk changes.
- Separate development, staging, and production credentials.
- Use least privilege and short-lived credentials where supported.
- Prefer automated CI checks and immutable/repeatable deployments.
- Add health checks, logs, metrics, and alerting appropriate to the service.

## Suggested tools
- Docker CLI: https://github.com/docker/cli
- Trivy: https://github.com/aquasecurity/trivy
- GitHub Actions: https://github.com/features/actions
- Terraform (if infrastructure as code is used): https://github.com/hashicorp/terraform

## Verification
Validate configuration, run CI checks, scan relevant artifacts, test health checks, and document rollback. Do not claim a deployment succeeded unless its result was observed.
