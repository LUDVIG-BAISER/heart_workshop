# app/schemas.py
from pydantic import BaseModel, FilePath

class PredictRequest(BaseModel):
    path: FilePath

class PredictResponse(BaseModel):
    predictions: list
