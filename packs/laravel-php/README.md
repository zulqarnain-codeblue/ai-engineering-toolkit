# Pack: Laravel / PHP

Use only when the repository uses Laravel/PHP.

## Before coding
- Detect Laravel/PHP versions, database, queue driver, cache, auth approach, deployment environment, and test tooling.
- Inspect migrations, models, policies, requests, services/actions, jobs, events, routes, and existing tests relevant to the change.
- Do not assume the local environment matches production.

## Implementation standards
- Enforce authorization server-side; hiding UI is not access control.
- Validate untrusted input and use explicit response contracts.
- Use transactions for multi-step data changes that must remain consistent.
- Design jobs for retries, idempotency, timeouts, and observable failure.
- Avoid N+1 queries and unbounded result sets.
- Protect secrets and sensitive payloads in logs.
- Make migrations safe for the deployment strategy and existing data volume.
- Keep business logic testable and avoid unnecessary service layers.

## Suggested tools
- Pest: https://github.com/pestphp/pest
- Larastan: https://github.com/larastan/larastan
- Laravel Pint: https://github.com/laravel/pint
- Context7: https://github.com/upstash/context7
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/

## Verification
Run relevant Pest/PHPUnit tests, Pint check, static analysis if configured, migrations against a safe test database, and API/authorization tests. Never run destructive commands against production as a verification shortcut.
