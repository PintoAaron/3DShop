from pydantic_settings import BaseSettings



class AppSettings(BaseSettings):
    API_PREFIX:str = "/api/v1"
    API_TITLE:str = "3D SHOP API"
    API_DESCRIPTION:str = "Api endpoints for an imaginary online shop"
    DATABASE_URL:str
    REDIS_HOST:str
    REDIS_PORT:int
    REDIS_DB:int
    KEYCLOAK_URL:str
    KEYCLOAK_REALM:str
    KEYCLOAK_ADMIN:str
    KEYCLOAK_CLIENT:str
    KEYCLOAK_CLIENT_SECRET:str
    KEYCLOAK_ADMIN_PASSWORD:str
    PUBLIC_KEY:str
    AUDIENCE:str
    ALGORITHM:str
    
    
    class Config:
        env_file = ".env"
    
    
    
    