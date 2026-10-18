# AI Engineering Toolkit

A reusable, agent-compatible engineering operating system for projects built with Claude Code, Google Antigravity, and other coding agents.

The toolkit uses a **universal core + project profiles + optional domain/stack packs** model. It is intentionally tool-agnostic: repository instructions explain the process, while skills and external tools are enabled only when relevant.

## Goals

- Understand an existing codebase before changing it.
- Turn ambiguous requests into proportional plans and verifiable acceptance criteria.
- Research reference products with REA when needed.
- Use current, version-specific documentation rather than guessing.
- Implement maintainable code that fits the existing architecture.
- Verify behavior with automated tests and real user-flow checks where appropriate.
- Protect credentials, production data, and destructive operations.
- Report what changed and what was actually verified.

## Quick start

1. Copy `core/`, `profiles/`, `packs/`, `skills/`, and `policies/` into your central toolkit repository or keep this repository as the source of truth.
2. For a project, copy `templates/AGENTS.md` to the project root as `AGENTS.md`.
3. If using Claude Code, copy `templates/CLAUDE.md` to the project root as `CLAUDE.md`, or keep it concise and point to `AGENTS.md`.
4. Read `core/project-discovery.md` and choose one profile from `profiles/`.
5. Enable only relevant packs from `packs/`.
6. Run the detector: `python scripts/detect_project.py /path/to/project`.
7. Review its output; detection is advisory, not a license to modify files automatically.
8. Follow the selected workflow and report verification honestly.

## Recommended first setup

For a new product or a substantial feature:
- Use **Spec Kit OR Superpowers as the primary workflow** for that task. They may coexist in your toolkit, but avoid running two overlapping planning systems simultaneously.
- Use REA only when reverse-engineering or investigating an existing reference product is useful.
- Use Context7 or official documentation for version-sensitive framework/library questions.
- Use Playwright when browser interaction or end-to-end UI verification is relevant.
- Use security tooling proportionally to the project's risk.

## Repository map

```text
core/       universal engineering standards and workflows
profiles/   task modes: new product, existing codebase, bug fix, feature
packs/      stack/domain-specific guidance
skills/     reusable task recipes
templates/  project instruction and planning templates
policies/   safety, permissions, dependency and production rules
scripts/    read-only project detection utilities
```

## Compatibility notes

- `AGENTS.md` is a broadly usable convention supported by multiple coding-agent tools, but support and precedence vary. Check the specific agent's current documentation.
- Claude Code can use `CLAUDE.md`; keep it short and reference shared instructions rather than duplicating everything.
- Antigravity may use workspace rules, skills, or agent-specific configuration depending on the current product version. Treat the templates here as source material and adapt them to the supported mechanism in your installed version.
- This repository does not install MCP servers, plugins, packages, or skills automatically. Review and configure those explicitly.
- The project detector only reads common manifest/config filenames and does not inspect source code deeply.

## Tool references

- REA: https://github.com/morluto/rea
- Superpowers: https://github.com/obra/superpowers
- Spec Kit: https://github.com/github/spec-kit
- Anthropic Skills: https://github.com/anthropics/skills
- Vercel Agent Skills: https://github.com/vercel-labs/agent-skills
- Context7: https://github.com/upstash/context7
- Playwright MCP: https://github.com/microsoft/playwright-mcp
- Trail of Bits Skills: https://github.com/trailofbits/skills
- shadcn/ui: https://github.com/shadcn-ui/ui
- Storybook: https://github.com/storybookjs/storybook
- axe-core: https://github.com/dequelabs/axe-core
- Pest: https://github.com/pestphp/pest
- Larastan: https://github.com/larastan/larastan
- Laravel Pint: https://github.com/laravel/pint
- Shopify CLI: https://github.com/Shopify/cli
- Theme Check: https://github.com/Shopify/theme-check
- promptfoo: https://github.com/promptfoo/promptfoo
- LangGraph: https://github.com/langchain-ai/langgraph
- Expo: https://github.com/expo/expo
- Maestro: https://github.com/mobile-dev-inc/maestro
- dbt Core: https://github.com/dbt-labs/dbt-core
- Trivy: https://github.com/aquasecurity/trivy

## License

This scaffold is provided as a starting point. Review the licenses of any third-party tools or skills you adopt separately.
