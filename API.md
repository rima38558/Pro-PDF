API Reference (high level)
==========================

The backend is a FastAPI application exposing REST endpoints. OpenAPI docs are available when the server runs at `/docs`.

Key endpoints
- `POST /api/auth/register` — register a new user (queues verification email)
- `POST /api/auth/token` — obtain JWT token
- `POST /api/tasks/enqueue/{tool}` — enqueue PDF tasks (merge, split, rotate, watermark, highlighter)
- `GET /api/plans` — list billing plans
- `POST /api/subscriptions` — create a subscription (billing flow scaffold)

Notes
- Protected endpoints require `Authorization: Bearer <token>` and some require `require_active_subscription`.
- Use `multipart/form-data` for file uploads.
