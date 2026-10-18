# Project Discovery and Capability Selection

## Step 1 — Read the environment
Inspect, when present:
- `AGENTS.md`, `CLAUDE.md`, README and project docs
- Git status and current branch
- package manifests and lockfiles
- language/framework manifests
- test, lint, formatting, CI and deployment configuration
- existing design system and architectural conventions
- environment variable names (never print secret values)

Do not dump secrets, `.env` contents, tokens, private keys, or customer data into chat or logs.

## Step 2 — Classify the work
Choose one primary profile:
- `new-product`
- `existing-codebase`
- `bug-fix`
- `feature-development`

Then identify applicable dimensions:
- stack: React/Next.js, Laravel/PHP, Shopify, mobile, data, infrastructure, other
- domain: SaaS, ecommerce, AI application, internal tool, data pipeline, content site, other
- risk: low, medium, high (auth, payments, personal data, production infrastructure, regulated context)
- verification: unit, integration, browser, device, data-quality, security, deployment

## Step 3 — Select only relevant capabilities
- REA: reference product investigation or behavior discovery.
- Spec Kit: substantial specification-driven work where its commands and agent support fit.
- Superpowers: disciplined implementation workflow where supported.
- Context7 / official docs: APIs or libraries where version correctness matters.
- Playwright: web UI behavior and end-to-end verification.
- Stack pack: only if the stack is detected or explicitly selected.
- Domain pack: only if the domain's requirements materially affect the work.
- Security pack: always apply baseline security; expand for high-risk changes.

## Step 4 — Resolve conflicts
1. Explicit user requirements and safety constraints.
2. Existing project conventions and architecture.
3. This toolkit's universal principles.
4. Optional pack guidance.
5. Personal preference.

If two workflows overlap, choose one primary workflow and use other tools only for non-overlapping tasks.

## Step 5 — Report selection
For substantial work, briefly report:
- detected stack and evidence
- chosen profile and packs
- relevant assumptions
- checks planned
- anything that could not be detected reliably
