from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict():
    r = client.post("/predict", json={"text":"I love this"})
    assert r.status_code == 200
    assert r.json()["label"] in {"positive","negative"}
