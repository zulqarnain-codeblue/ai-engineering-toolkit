# Architecture Decision Standard

For significant architecture decisions, document:
- Context and constraints
- Options considered
- Decision and rationale
- Consequences and trade-offs
- Migration/rollback approach if applicable

Do not force a specific architecture onto every project. Start from the current needs and expected change. Prefer clear module boundaries, explicit data ownership, stable contracts, observability, and straightforward local development.

For new projects, consider:
- user journeys and domain boundaries
- data model and ownership
- authentication and authorization
- integration boundaries and failure modes
- deployment and environments
- observability and incident recovery
- accessibility, performance, and cost constraints
