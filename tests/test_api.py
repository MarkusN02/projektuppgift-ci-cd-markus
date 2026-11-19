from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app, raise_server_exceptions=False)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add_endpoint():
    response = client.get("/add", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_divide_endpoint():
    response = client.get("/divide", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 2.5}


def test_divide_by_zero_endpoint():
    response = client.get("/divide", params={"a": 1, "b": 0})
    assert response.status_code == 400
    assert "noll" in response.json()["detail"]


def test_add_invalid_input():
    response = client.get("/add", params={"a": "x", "b": 3})
    assert response.status_code == 422

def test_version_default(monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "dev"}


def test_version_from_environment(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.2.3")
    response = client.get("/version")
    assert response.json() == {"version": "1.2.3"}