# Pack: React / Next.js

Use only when the repository uses React or Next.js.

## Before coding
- Detect framework and versions from manifests and lockfiles.
- Identify routing model, rendering strategy, data-fetching conventions, styling system, component library, and test stack.
- Read official docs for version-sensitive behavior.

## Implementation standards
- Follow existing component and route conventions.
- Keep server/client boundaries explicit where applicable.
- Handle loading, empty, error, and permission states.
- Avoid unnecessary client-side JavaScript and effects.
- Validate forms at the appropriate trust boundary; server-side validation remains authoritative.
- Respect semantics, keyboard use, focus, responsive layouts, and reduced motion.
- Measure before adding complex performance optimizations.

## Suggested tools
- Vercel Agent Skills: https://github.com/vercel-labs/agent-skills
- Context7: https://github.com/upstash/context7
- Vitest: https://github.com/vitest-dev/vitest
- Playwright: https://github.com/microsoft/playwright
- Storybook: https://github.com/storybookjs/storybook
- axe-core: https://github.com/dequelabs/axe-core
- shadcn/ui: https://github.com/shadcn-ui/ui (optional, not mandatory)

## Verification
Run available lint, typecheck, unit/component tests, production build, and relevant browser journeys. State which commands were unavailable.
