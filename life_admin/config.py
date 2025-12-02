from dataclasses import dataclass
from google.adk.models.google_llm import Gemini
from google.genai import types

APP_NAME = "life_admin"  # IMPORTANT: lowercase

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=2,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

@dataclass
class AppConfig:
    worker_model: str = "gemini-2.5-flash"

config = AppConfig()

def make_gemini(model_name: str | None = None) -> Gemini:
    if model_name is None:
        model_name = config.worker_model
    return Gemini(model=model_name, retry_options=retry_config)
