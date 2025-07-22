# app/main.py
from fastapi import FastAPI, HTTPException
from app.schemas import PredictRequest, PredictResponse
from app.services import PredictionService
from app.views import router as form_router

app = FastAPI(title="ML Prediction API")
app.include_router(form_router)

# Инициализация при запуске
service = PredictionService(model_path="model.pkl")

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    try:
        predictions = service.predict_from_csv(request.path)
        return PredictResponse(predictions=predictions)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

