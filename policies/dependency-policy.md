# Dependency and Extension Policy

Before adding a package, skill, MCP server, plugin, or agent extension:
1. Identify the concrete capability gap.
2. Check compatibility with the agent, operating system, runtime, and project versions.
3. Review maintenance activity, license, documentation, permissions, install scripts, and transitive dependencies.
4. Prefer official sources and least-privilege configuration.
5. Avoid duplicating an existing capability.
6. Pin versions or use lockfiles where appropriate.
7. Document why it was added and how to remove it.

Never assume a popular repository is automatically safe or supported by every agent.
