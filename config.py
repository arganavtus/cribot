from dataclasses import dataclass
from pathlib import Path
from decouple import config as dconfig

BASE_DIR: Path = Path(__file__).parent.parent.parent.parent.parent.resolve()

@dataclass()
class Settings:
    # Common settings
    class Common:
        TITLE: str = "ArGanSoft CriBot"
        VERSION: str = "0.1.0"
        TIMEZONE: str = "UTC"
        DESCRIPTION: str | None = None
        DEBUG: bool = dconfig("DEBUG", cast=bool, default=False)
        BASE_DIR: Path = Path(__file__).parent.parent.parent.parent.parent.resolve()

    class TGBot:
        TOKEN: str = dconfig("TGBOT_TOKEN", cast=str)
        ADMINS: int = dconfig("TGBOT_ADMINS", cast=int)
        USE_REDIS: bool = dconfig("TGBOT_USE_REDIS", cast=bool, default=False)

    class Redis:
        SCHEME: str = dconfig("REDIS_SCHEME", cast=str, default="redis")
        HOST: str = dconfig("REDIS_HOST", cast=str, default="0.0.0.0")
        PORT: int = dconfig("REDIS_PORT", cast=int, default=6379)
        PATH: str = dconfig("REDIS_PATH", cast=str, default="0")
        URL: str = f"{SCHEME}://{HOST}:{PORT}/{PATH}"

    class Config:
        case_sensitive: bool = True
        env_file: str = f"{str(BASE_DIR)}/.env"


