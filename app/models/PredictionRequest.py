from pydantic import BaseModel

class PredictionRequest(BaseModel):
    text: str
    max_length: int | None = None
    temperature: float | None = None