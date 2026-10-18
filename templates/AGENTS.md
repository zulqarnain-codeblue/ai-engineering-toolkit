# Agent Instructions

Read `README.md` and the relevant files under the AI Engineering Toolkit before substantial work.

## Always
- Inspect the codebase, project instructions, git status, manifests, and tests before editing.
- Preserve existing user changes and established architecture.
- Choose a proportional workflow; do not over-plan tiny fixes.
- Use current official documentation for version-sensitive behavior.
- Add or update tests for meaningful behavior changes.
- Run relevant checks and report exact outcomes honestly.
- Consider security, accessibility, performance, error states, and data integrity where relevant.
- Keep changes focused and review the final diff.

## Never
- Expose secrets or sensitive data.
- Run destructive production operations without explicit authorization and a reviewed plan.
- Claim checks passed when they were not run.
- install dependencies or agent extensions without evaluating relevance, compatibility, permissions, and licensing.
- Replace existing architecture or design systems without a reason.

## Before work
1. Classify the task as bug fix, feature, existing-codebase work, or new product.
2. Detect stack/domain and load only relevant packs.
3. State assumptions if they materially affect the solution.
4. Define acceptance criteria appropriate to the scope.

## Before completion
Provide:
- Summary of changes
- Important decisions/files
- Tests and checks actually run, with results
- Risks, limitations, and unverified behavior
- Deployment notes if relevant
