from pydantic import BaseModel, Field

from .ModelConfig import ModelConfig
from .EnvVars import EnvVars

class AppSettings(BaseModel):
    MODEL_CONFIG: ModelConfig = Field(ModelConfig(), title="Model Configuration", description="The name of the model repo on HuggingFace or path to the model local directory.")
    ENV_VARS: EnvVars = Field(..., title="Environment Variables", description="The environment variables to be set before running the microservice.")