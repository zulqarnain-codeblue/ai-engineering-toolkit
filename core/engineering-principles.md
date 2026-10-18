# Universal Engineering Principles

These principles apply to every project, regardless of stack.

## 1. Understand before editing
- Inspect repository structure, manifests, instructions, tests, git status, and current conventions.
- Identify what already exists before proposing replacement architecture.
- Preserve unrelated user changes. Never reset, overwrite, or discard work without explicit approval.
- Ask a focused question only when a missing decision blocks safe progress; otherwise state reasonable assumptions.

## 2. Work proportionally
- Small change: inspect relevant files, implement, run focused tests, summarize.
- Bug fix: reproduce or isolate the cause, add a regression test where feasible, fix the root cause, verify.
- Feature: define acceptance criteria, inspect dependencies and interfaces, plan, implement in slices, test.
- New product or major architecture: establish users, outcomes, scope, data model, architecture, security, and release plan before extensive implementation.

## 3. Prefer boring, maintainable engineering
- Follow established conventions unless there is a concrete reason to change them.
- Prefer the smallest complete solution over unnecessary abstraction.
- Do not add dependencies, frameworks, services, or agents without a clear need.
- Avoid duplicated business logic and hidden side effects.
- Keep functions, components, and modules cohesive.

## 4. Evidence over assertion
- Do not claim a test, build, browser check, deployment, or security scan passed unless it was actually run and its result inspected.
- Distinguish verified facts, assumptions, and unresolved questions.
- If a check cannot be run, explain why and give the exact remaining verification step.
- Treat generated code as untrusted until validated.

## 5. Product quality
- Consider loading, empty, success, error, offline, permission-denied, and partial-failure states when relevant.
- Preserve accessibility, responsive behavior, performance, localization, and data integrity.
- Make interaction feedback clear and avoid motion that prevents usability.
- Use realistic edge cases, not only happy-path examples.

## 6. Communication
- Before a broad or risky change, provide a concise plan.
- For long tasks, work in small reviewable increments.
- Final report: summary, key files/decisions, tests run and outcomes, risks/unverified items, and next steps.
