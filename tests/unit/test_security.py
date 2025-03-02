# tests/unit/test_security.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_security_headers():
    response = client.get("/")
    headers = response.headers
    
    assert headers["Content-Security-Policy"] == "default-src 'self'"
    assert headers["X-Frame-Options"] == "DENY"
    assert "max-age=63072000" in headers["Strict-Transport-Security"]