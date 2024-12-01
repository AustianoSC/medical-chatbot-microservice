from pydantic import BaseModel

class PredictionResponse(BaseModel):
    generated_text: str