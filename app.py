from google.adk.apps.app import App
from life_admin.agent import root_agent
from life_admin.config import APP_NAME

app = App(
    name=APP_NAME,
    root_agent=root_agent,
)
