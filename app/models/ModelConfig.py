from pydantic import BaseModel, Field

class ModelConfig(BaseModel):
    MODEL_NAME: str = Field("llama-3-8b-chat-doctor", title="Model Name", description="The name of the model repo on HuggingFace or path to the model local directory.")
    MAX_LENGTH: int = Field(512, title="Max Length", description="The maximum length of the generated text.")
    TEMPERATURE: float = Field(0.7, title="Temperature", description="The temperature value for text generation.")