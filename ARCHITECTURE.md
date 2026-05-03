Pro PDF — Architecture Overview
================================

Components
- Backend (FastAPI): `backend/app` — REST API, auth, billing, PDF task enqueueing.
- Worker (Celery): background PDF processing & email delivery, uses Redis broker.
- Database (Postgres): persistent storage via SQLAlchemy and Alembic migrations.
- Storage: local filesystem by default, S3/MinIO optional (`USE_S3` env).
- Frontend (React + Vite): `frontend/` — user UI for uploads, tools, and billing.

Data flow
1. User uploads file via frontend → backend stores file (S3 or local).
2. Backend enqueues a Celery task (merge/split/rotate/watermark/highlighter).
3. Worker processes PDF and writes output back to storage; notifies user via email or webhook.

Design notes
- Keep heavy PDF work in Celery to avoid web request timeouts.
- Use abstracted storage functions in `backend/app/storage.py` to switch S3/local easily.
- Use feature flags and subscription checks to gate premium tools.
