 # FastAPI entrypoint (API endpoints only)
from fastapi import FastAPI, Request
from pydantic import BaseModel

# Define request schema
class MSMEData(BaseModel):
    gst_compliance: float
    upi_inflows: float
    epfo_contributions: float = 0.0
    other_features: dict = {}

# Initialize FastAPI app
app = FastAPI(title="MSME Financial Health Score API")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "MSME Financial Health Score API is running."}

# Score endpoint stub
@app.post("/score")
def score(msme: MSMEData):
    """
    Stub implementation: returns a synthetic score here.
    Replace with LightGBM/XGBoost model inference later.
    """
    # Simple weighted average for demo purposes
    synthetic_score = (
        (msme.gst_compliance * 0.4) +
        (msme.upi_inflows * 0.4) +
        (msme.epfo_contributions * 0.2)
    ) * 100

    return {
        "msme_id": "demo-msme-001",
        "score": round(synthetic_score, 2),
        "risk_level": "Low" if synthetic_score > 70 else "Medium",
        "recommendation": "Eligible for credit expansion" if synthetic_score > 70 else "Needs compliance improvement"
    }
