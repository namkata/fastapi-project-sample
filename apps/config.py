import os
from dotenv import load_dotenv, find_dotenv
from apps.constants import FORMAT, DATE_FMT
from pydantic import (
    BaseModel,  # configure model in Settings
    BaseSettings,
    PostgresDsn,
    RedisDsn,
    AmqpDsn,
)
load_dotenv(find_dotenv())
print(os.getenv("PG_DNS"))

class Settings(BaseSettings):
    project_title: str | None = os.getenv('PROJECT_TITLE', 'fast api example')
    project_description: str | None = os.getenv('PROJECT_DESCRIPTION', 'fast api example')
    project_version: str = os.getenv('PROJECT_VERSION', '0.1.0')
    pg_dsn: PostgresDsn | str = os.getenv('PG_DNS')  # 'sqlite:///./sql_app.db'
    redis_dsn: RedisDsn | None = os.getenv('REDIS_DNS')
    cors_origins: list[str] = os.getenv('CORS_ORIGINS', ['*'])
    cors_methods: list[str] = os.getenv('CORS_METHODS', ['*'])
    cors_headers: list[str] = os.getenv('CORS_HEADERS', ['*'])

    class Config:
        # `.env.prod` takes priority over `.env`
        env_file = '.env', '.env.prod'
        env_file_encoding = 'utf-8'


class LogConfig(BaseModel):
    """
    Logging configuration to be set for the sever
    """
    LOGGER_NAME: str = os.getenv('PROJECT_TITLE', 'fast api example')
    LOG_FORMAT: str = FORMAT
    LOG_LEVEL: str = "DEBUG"
    DATE_FORMAT: str = DATE_FMT

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": DATE_FORMAT,
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }


logging_conf = LogConfig()
settings = Settings()
