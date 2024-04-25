from pydantic_settings import BaseSettings



class AppSettings(BaseSettings):
    API_TITLE :str = "3DSHOP API"
    API_DESCRIPTION :str = "API for an imaginary 3D shop"
    API_PREFIX :str = "/api/v1"
    DATABASE_URL :str = ""
    KAFKA_BOOTSTRAP_SERVERS :str
    KAFKA_TOPIC :str
    KEYCLOAK_URL :str = "http://192.168.126.98:8080/"
    KEYCLOAK_REALM :str
    KEYCLOAK_CLIENT_ID :str
    KEYCLOAK_CLIENT_SECRET :str
    KEYCLOAK_ADMIN_USER :str
    KEYCLOAK_ADMIN_PASSWORD :str
    PUBLIC_KEY :str
    AUDIENCE :str
    ALGORITHM :str
    
    class Config:
        env_file = ".env"
        