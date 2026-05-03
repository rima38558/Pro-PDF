Security
========

Secrets
- Never commit secrets or API keys. Use environment variables and GitHub Secrets for CI.

Dependencies
- Keep `backend/requirements.txt` up to date and run dependency scans periodically.

Data protection
- Store minimal PII and secure user passwords using strong hashing (bcrypt).
- Use TLS in production for all endpoints and S3 connections.

Access controls
- Admin endpoints should be protected and audited. Use role checks for privileged operations.

Vulnerabilities
- Run automated security scans (Snyk/Dependabot) and respond to alerts.
