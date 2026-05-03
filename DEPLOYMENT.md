Deployment Guide
================

Local development
- Use Docker Compose: `make up` to build and start services (Postgres, Redis, backend, worker, frontend).
- Run migrations: `make migrate`.

Production notes
- Use environment variables for secrets (`DATABASE_URL`, `JWT_SECRET`, `SENDGRID_API_KEY`, S3 creds).
- Deploy backend and worker as separate services (Kubernetes or managed containers).
- Use an object store (S3) for production storage and a managed DB (Postgres).

CI/CD
- GitHub Actions is configured to run tests, migrations checks, and upload reports.
- Add deployment steps (CD) to push Docker images and update staging/production clusters.

Monitoring
- Collect worker/queue metrics and set alerts on task failure rates and queue backlog.
