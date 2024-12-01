from pydantic import BaseModel, Field

class EnvVars(BaseModel):
     HUGGINGFACE_API_TOKEN: str = Field(..., title="HuggingFace API Token", description="The API token for the HuggingFace account.")