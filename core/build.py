from fastapi import FastAPI, responses
from fastapi.middleware.cors import CORSMiddleware
from core import setup as db_setup
from api.v1 import auth

from config import setting

settings = setting.AppSettings()


class AppBuilder():
    def __init__(self) -> None:
        self._app = FastAPI(
            title=settings.API_TITLE,
            description=settings.API_DESCRIPTION)
        
    
    def register_routes(self):
        
        self._app.include_router(auth.auth_router, prefix=settings.API_PREFIX)
        
        @self._app.get("/",include_in_schema=False)
        def _index():
            return responses.RedirectResponse(url="/docs")
        
        
    
    def register_exceptions(self):
        pass
    
    
    
    def register_middlewares(self):
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        
    def register_databases(self) -> None:
        db_setup.Base.metadata.create_all(
            bind = db_setup.db.get_engine()
        )
    
    
    def get_app(self):
        self.register_databases()
        self.register_routes()
        self.register_exceptions()
        self.register_middlewares()
        return self._app