# app/model.py
import pickle
import pandas as pd

class ModelWrapper:
    def __init__(self, model_path: str):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, data: pd.DataFrame) -> str:
        result = self.model.predict_proba(data)[:, 1][0]
        return f"{round(result * 100, 2)}%"

