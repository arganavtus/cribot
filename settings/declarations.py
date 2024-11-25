import enum
from functools import lru_cache
from decouple import config as dconfig

from .config import Settings


class Environment(str, enum.Enum):
    PRODUCTION: str = "PROD"
    DEVELOPMENT: str = "DEV"
    STAGING: str = "STAGE"


class DevSettings(Settings):
    DESCRIPTION: str | None = "Development Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT


class StageSettings(Settings):
    DESCRIPTION: str | None = "Test Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.STAGING


class ProdSettings(Settings):
    DESCRIPTION: str | None = "Production Environment."
    DEBUG: bool = False
    ENVIRONMENT: Environment = Environment.PRODUCTION


class SettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> Settings:
        if self.environment == Environment.DEVELOPMENT.value:
            return DevSettings()
        elif self.environment == Environment.STAGING.value:
            return StageSettings()
        return ProdSettings()


@lru_cache()
def get_settings() -> Settings:
    return SettingsFactory(
        environment=dconfig("ENVIRONMENT", default="DEV", cast=str))()  # type: ignore


settings: Settings = get_settings()
