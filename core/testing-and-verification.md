# Testing and Verification Standard

Select checks based on the changed behavior and project stack.

## Test layers
- Unit: pure functions and isolated business rules.
- Integration: database, API, queues, external adapters, and module boundaries.
- End-to-end: complete user-visible journeys.
- Visual/accessibility: layout, responsive behavior, keyboard interactions, semantics.
- Security: authorization boundaries, validation, abuse cases, secret handling.
- Data quality: schema, uniqueness, completeness, reconciliation, and transformation rules.
- Operations: startup, migrations, health checks, rollback, and observability.

## Agent requirements
- Add regression coverage for bug fixes where feasible.
- Test both allowed and denied access for authorization changes.
- Include boundary and failure cases for important logic.
- Avoid brittle tests tied to implementation details when behavior assertions are possible.
- Never modify production data just to test.
- Do not weaken or delete tests merely to make the suite pass without explaining the reason and obtaining approval when the change is material.
- Record exact commands and meaningful outcomes.
