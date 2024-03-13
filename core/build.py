from fastapi import FastAPI,responses
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from core import setup as db_setup
from api.v1.router import auth


setting =settings.AppSettings()


class AppBuilder:
    def __init__(self):
        self.app = FastAPI(
            title=setting.API_TITLE,
            description=setting.API_DESCRIPTION,
        )
    
    def register_routes(self):
        self.app.include_router(
            auth.auth_router,
            prefix=setting.API_PREFIX,
            tags=["auth"])
        
        @self.app.get("/",include_in_schema=False)
        def _index():
            return responses.RedirectResponse("/docs")
    
    
    def register_middlewares(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
        
        
    def register_database(self):
        db_setup.Base.metadata.create_all(bind=db_setup.database.get_engine())
    
    
    def get_app(self):
        self.register_routes()
        self.register_middlewares()
        self.register_database()
        return self.app