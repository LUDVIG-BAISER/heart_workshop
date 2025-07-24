import joblib
import pandas as pd
import os

class ModelWrapper:
    def __init__(self, model_path: str = None):
        if model_path is None:
            base_dir = os.path.dirname(__file__)  # путь к файлу model.py
            model_path = os.path.join(base_dir, 'model_best_recall.pkl')

        self.model = joblib.load(model_path)

    def predict(self, data: pd.DataFrame) -> str:
        result = self.model.predict_proba(data)[:, 1][0]
        return f"{round(result * 100, 2)}%"