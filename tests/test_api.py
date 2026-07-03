import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "MSME Financial Health Score API is running."

def test_score_endpoint_low_risk():
    payload = {
        "gst_compliance": 0.9,
        "upi_inflows": 0.8,
        "epfo_contributions": 0.7
    }
    response = client.post("/score", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert data["risk_level"] in ["Low", "Medium", "High"]

def test_score_endpoint_medium_risk():
    payload = {
        "gst_compliance": 0.5,
        "upi_inflows": 0.5,
        "epfo_contributions": 0.4
    }
    response = client.post("/score", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert data["risk_level"] in ["Low", "Medium", "High"]

def test_invalid_payload():
    # Missing required fields should trigger validation error
    payload = {"gst_compliance": 0.9}
    response = client.post("/score", json=payload)
    assert response.status_code == 422  # Unprocessable Entity
