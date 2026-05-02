import os
import importlib
import json


def test_send_email_fallback_writes_file(tmp_path, monkeypatch):
    # Ensure SENDGRID_API_KEY is unset and DEV_EMAIL_DIR points to tmp
    monkeypatch.delenv("SENDGRID_API_KEY", raising=False)
    monkeypatch.setenv("DEV_EMAIL_DIR", str(tmp_path))

    # reload module so env vars are picked up
    import app.email as email_module
    importlib.reload(email_module)

    to = "user@example.com"
    subj = "Test"
    body = "Hello"
    ok = email_module.send_email(to, subj, body, None)
    assert ok is True

    # find created file
    files = list(tmp_path.iterdir())
    assert len(files) == 1
    data = json.loads(files[0].read_text(encoding="utf-8"))
    assert data["to"] == to
    assert data["subject"] == subj


def test_send_email_uses_sendgrid(monkeypatch):
    # Set a fake API key
    monkeypatch.setenv("SENDGRID_API_KEY", "fake-key")

    # Mock requests.post
    class DummyResp:
        def raise_for_status(self):
            return None


    called = {}

    def fake_post(url, headers=None, json=None, timeout=None):
        called['url'] = url
        called['headers'] = headers
        called['json'] = json
        return DummyResp()

    monkeypatch.setattr("requests.post", fake_post)

    # reload module to pick up SENDGRID_API_KEY
    import app.email as email_module
    importlib.reload(email_module)

    ok = email_module.send_email("u@e.com", "S", "b", "<p>b</p>")
    assert ok is True
    assert called.get('url') == "https://api.sendgrid.com/v3/mail/send"
    assert 'Authorization' in called['headers']
