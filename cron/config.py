from config import settings

setting = settings.AppSettings()


class Config:
    broker_url = f"redis://{setting.REDIS_HOST}:{setting.REDIS_PORT}/{setting.REDIS_DB}"
    result_backend = f"redis://{setting.REDIS_HOST}:{setting.REDIS_PORT}/{setting.REDIS_DB}"
    timezone = "UTC"
    broker_connection_retry_on_startup = True