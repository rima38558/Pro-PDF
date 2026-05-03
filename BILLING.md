Billing & Payments (overview)
=============================

Plans and subscriptions
- The backend defines `Plan` and `Subscription` models (see `backend/app/models.py`).
- Users subscribe to plans; `require_active_subscription` dependency guards premium endpoints.

Payment provider
- PayU India is planned for payments. Integration points:
  - Create order endpoint → redirect to PayU checkout
  - Webhook endpoint to verify and activate subscriptions
  - Invoice generation after successful payment

Security and verification
- Verify webhook signatures and use idempotency keys for order processing.

Next steps
- Implement PayU sandbox integration and webhook handler.
- Add tests and docs for billing flow.
