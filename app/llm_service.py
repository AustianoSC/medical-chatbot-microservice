import huggingface_hub as hf_hub

from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from .config import load_settings

class LLMService:
    def __init__(self):
        settings = load_settings("configs/config.yaml")
        hf_hub.login(settings.ENV_VARS.HUGGINGFACE_API_TOKEN)
        tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_CONFIG.MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(settings.MODEL_CONFIG.MODEL_NAME)
        
        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_length=settings.MODEL_CONFIG.MAX_LENGTH,
            temperature=settings.MODEL_CONFIG.TEMPERATURE
        )
        
        self.llm = HuggingFacePipeline(pipeline=pipe)
    
    async def generate(self, text: str, max_length: int | None = None, temperature: float | None = None) -> str:
        return self.llm(text)