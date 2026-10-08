from pydantic import BaseModel


class AppInfo(BaseModel):
    name: str
    version: str
    environment: str
    llm_enabled: bool
