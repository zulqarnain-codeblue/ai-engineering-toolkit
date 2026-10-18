# Code Review Checklist

Review the diff, not just the intended design.

## Correctness
- Does it meet acceptance criteria?
- Are edge cases, errors, retries, and partial failures handled?
- Are assumptions and invariants explicit?

## Architecture
- Does the change fit existing boundaries?
- Is logic duplicated?
- Are new dependencies justified?
- Are contracts and backwards compatibility considered?

## Data and security
- Is authorization enforced server-side?
- Is input validated at trust boundaries?
- Are secrets and personal data protected?
- Are transactions, idempotency, and concurrency handled where needed?
- Are logs free of credentials and sensitive payloads?

## User experience
- Are loading, empty, error, and success states clear?
- Does keyboard navigation work?
- Is the UI responsive and usable at expected sizes?
- Is motion respectful of reduced-motion preferences?

## Delivery
- Are migrations reversible or safely forward-compatible where possible?
- Are tests and documentation updated?
- Are new environment variables documented without values?
- Are deployment risks and rollback steps understood?
