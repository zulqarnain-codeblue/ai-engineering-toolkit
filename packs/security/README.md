# Pack: Security and Privacy

Apply the baseline to every project; expand this pack for authentication, authorization, payments, personal data, file uploads, external integrations, or production infrastructure.

## Minimum controls
- Threat-model trust boundaries and sensitive assets.
- Validate input server-side; encode output for its context.
- Enforce authorization at the resource/action boundary.
- Use secure session/token handling and least privilege.
- Protect secrets; rotate exposed credentials rather than merely deleting them from the latest diff.
- Rate-limit abuse-prone endpoints and expensive operations.
- Review file upload, SSRF, injection, CSRF, XSS, access-control, and dependency risks as relevant.
- Minimize sensitive data collection and retention.
- Avoid logging tokens, passwords, payment data, or unnecessary personal information.

## Suggested references/tools
- Trail of Bits skills: https://github.com/trailofbits/skills
- Trivy: https://github.com/aquasecurity/trivy
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/

Security tooling is supplementary. It does not replace human review or threat-specific testing.
