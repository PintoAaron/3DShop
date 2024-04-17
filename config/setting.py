from typing import Union

from pydantic_settings import BaseSettings



class AppSettings(BaseSettings):
    API_TITLE :str = "3DSHOP API"
    API_DESCRIPTION :str = "API for an imaginary 3D shop"
    API_PREFIX :str = "/api/v1"
    DATABASE_URL :str = ""
    KAFKA_BOOTSTRAP_SERVER :str = "localhost:9092"
    
    
    class Config:
        env_file = ".env"