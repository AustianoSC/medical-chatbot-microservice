from fastapi import FastAPI, HTTPException
from loguru import logger
from .models import PredictionRequest, PredictionResponse
from .llm_service import LLMService

llm_app = FastAPI(title="LLM Microservice")
llm_service = LLMService()

@llm_app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        generated_text = await llm_service.generate(
            request.text,
            max_length=request.max_length,
            temperature=request.temperature
        )
        return PredictionResponse(generated_text=generated_text)
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@llm_app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(llm_app, host="0.0.0.0", port=8000)