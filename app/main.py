from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
from pathlib import Path
import os
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

MODEL_PATH = os.getenv("MODEL_PATH", "app/model/model.joblib")

app = FastAPI(title="ML Inference Service", version="0.1.0")

PREDICTIONS = Counter("predictions_total", "Total number of predictions", ["label"])

class TextIn(BaseModel):
    text: str

@app.on_event("startup")
def _load_model():
    global model
    if not Path(MODEL_PATH).exists():
        raise RuntimeError(f"Model not found at {MODEL_PATH}. Run `python -m app.train` first.")
    model = load(MODEL_PATH)

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/livez")
def live():
    return {"status": "alive"}

@app.post("/predict")
def predict(inp: TextIn):
    pred = model.predict([inp.text])[0]
    label = "positive" if int(pred) == 1 else "negative"
    PREDICTIONS.labels(label=label).inc()
    return {"label": label}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
