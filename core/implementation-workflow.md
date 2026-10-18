# Implementation Workflow

1. **Restate outcome**: identify the user problem and observable result.
2. **Inspect**: read relevant code, tests, interfaces, and current git changes.
3. **Specify**: define acceptance criteria proportional to change size.
4. **Plan**: list small, ordered steps and likely risks.
5. **Implement**: make focused changes; preserve compatibility unless a breaking change is intended.
6. **Test**: run the smallest relevant checks first, then broader checks.
7. **Review**: inspect diff for regressions, accidental files, secrets, incomplete states, and maintainability.
8. **Document**: update docs/contracts when behavior or setup changes.
9. **Report**: state what changed, tests run, outcomes, and remaining risks.

## Completion checklist
- [ ] Acceptance criteria addressed
- [ ] Existing conventions followed
- [ ] Relevant tests added/updated
- [ ] Relevant tests actually run
- [ ] Lint/type/build checks run when available
- [ ] Security and data-integrity implications considered
- [ ] UI states and accessibility considered when applicable
- [ ] Diff reviewed; unrelated changes preserved
- [ ] Docs/config updated when necessary
- [ ] Final report distinguishes verified and unverified behavior
