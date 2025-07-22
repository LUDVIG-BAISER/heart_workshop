# app/views.py
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
import pandas as pd

from app.model import ModelWrapper

router = APIRouter()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

model = ModelWrapper(model_path=str(Path(__file__).parent.parent / "model.pkl"))

# Все необходимые поля:
FIELDS = [
    'Age', 'BMI', 'CK-MB', 'Cholesterol', 'Diabetes', 'Diastolic blood pressure',
    'Diet', 'Exercise Hours Per Week', 'Heart rate', 'Medication Use', 'Obesity',
    'Physical Activity Days Per Week', 'Previous Heart Problems', 'Sedentary Hours Per Day',
    'Sleep Hours Per Day', 'Stress Level', 'Systolic blood pressure', 'Triglycerides', 'Troponin'
]

@router.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "fields": FIELDS, "prediction": None})

@router.post("/", response_class=HTMLResponse)
async def form_post(request: Request):
    form_data = await request.form()
    try:
        input_data = {field: float(form_data[field]) for field in FIELDS}
        df = pd.DataFrame([input_data])
        prediction = model.predict(df)[0]
    except Exception as e:
        prediction = f"Ошибка: {e}"

    return templates.TemplateResponse("form.html", {"request": request, "fields": FIELDS, "prediction": prediction})

