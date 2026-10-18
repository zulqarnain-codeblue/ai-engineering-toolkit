# Profile: Existing Codebase

Use when adding to or maintaining an established repository.

- Read instructions, README, manifests, architecture, tests, and git status first.
- Identify the current patterns and extend them unless they are demonstrably unsafe or unsuitable.
- Do not rewrite or scaffold over an existing system without explicit authorization.
- Trace the affected path end-to-end, including callers, data, tests, and deployment implications.
- Make changes small and reviewable.
- Preserve uncommitted changes and unrelated behavior.
- Update docs when setup, API, schema, or user-visible behavior changes.
