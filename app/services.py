# app/services.py
import pandas as pd
from app.model import ModelWrapper
from app.utils import prepare_df

class PredictionService:
    def __init__(self, model_path: str):
        self.model = ModelWrapper(model_path)

    def predict_from_csv(self, file_path: str) -> list:
        df = pd.read_csv(file_path)
        df = prepare_df(df)  # 👈 подготовка перед predict
        return self.model.predict(df)
