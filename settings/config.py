
from pathlib import Path
from array import array

import decouple
from decouple import Config
from pydantic.v1 import BaseSettings


BASE_DIR: Path = Path(__file__).parent.parent.parent.parent.parent.resolve()
dconfig = decouple.Config('.env')

class Settings(BaseSettings):
    # Telegram Bot settings
    class Common:
        TITLE: str = "ArGanSoft Telegram Bot"
        VERSION: str = "0.1.0"
        TIMEZONE: str = "UTC"
        DESCRIPTION: str | None = None
        ENVIRONMENT: str = dconfig("ENVIRONMENT", cast=str, default="DEV")
        DEBUG: bool = dconfig("DEBUG", cast=bool, default=False)
        BASE_DIR: Path = Path(__file__).parent.parent.parent.parent.parent.resolve()
        BACKEND_SERVER_HOST: str = dconfig("BACKEND_SERVER_HOST", cast=str, default="localhost")
        BACKEND_SERVER_PORT: int = dconfig("BACKEND_SERVER_PORT", cast=int, default=8000)
        BACKEND_SERVER_WORKERS: int = dconfig("BACKEND_SERVER_WORKERS", cast=int, default=4)


    class TGBot:
        TGBOT_TOKEN: str = dconfig("TGBOT_TOKEN", cast=str, default="")
        ADMINS: list = dconfig("ADMINS", cast=list, default=[])
        WEBHOOK_POST: str = dconfig("WEBHOOK_POST", cast=str, default="")
        WEBHOOK_PATH: str = BASE_DIR / "webhooks"
        USE_REDIS: bool = dconfig("USE_REDIS", cast=bool, default=True)

    class Redis:
        SCHEME: str = dconfig("REDIS_SCHEME", cast=str, default="redis")
        HOST: str = dconfig("REDIS_HOST", cast=str, default="0.0.0.0")
        PORT: int = dconfig("REDIS_PORT", cast=int, default=6379)
        PATH: str = dconfig("REDIS_PATH", cast=str, default="0")
        DSN: str = f"{SCHEME}://{HOST}:{PORT}/{PATH}"



