import os
import yaml
from dotenv import load_dotenv
from pydantic import ValidationError

from .models import AppSettings
from .enums import EnvironmentVariables

def get_required_env_var(env_var_name: str) -> str:
    env_var = os.getenv(env_var_name)
    if env_var is None:
        raise ValueError(f"Environment variable {env_var_name} is required.")
    return env_var

def load_settings(config_path: str) -> AppSettings:
    load_dotenv()
    with open(config_path, 'r') as file:
        config_data = yaml.safe_load(file)
    try:
        config_data['ENV_VARS'] = {k.name.upper(): get_required_env_var(k.name) for k in EnvironmentVariables}
        config = AppSettings(**config_data)
        return config
    except ValidationError as e:
        print(f"Configuration validation error: {e}")
        raise e