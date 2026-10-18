# Pack: AI Applications and Agentic Systems

Use when an application calls LLMs, exposes AI features, or orchestrates agents.

## Standards
- Define input/output schemas and validate model output.
- Treat model output, retrieved documents, tool results, and user-supplied content as untrusted.
- Defend against prompt injection and unauthorized tool use.
- Keep authorization and business rules outside model judgment.
- Set timeouts, bounded retries, cancellation, rate limits, and cost budgets.
- Track latency, token/cost estimates, failure rates, and evaluation outcomes without logging secrets or unnecessary personal data.
- Provide fallback/error states and human review for consequential actions.
- Version prompts and maintain representative evaluation cases.
- Do not add multi-agent orchestration unless the workflow benefits from it.

## Suggested tools
- promptfoo: https://github.com/promptfoo/promptfoo
- LangGraph: https://github.com/langchain-ai/langgraph (when stateful orchestration is needed)
- Context7: https://github.com/upstash/context7
- Trail of Bits skills: https://github.com/trailofbits/skills

## Verification
Test normal, malformed, adversarial, refusal, tool-failure, timeout, and high-cost scenarios. Evaluate quality on a fixed dataset before changing prompts or models.
