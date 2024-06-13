from fastapi import FastAPI, responses
from fastapi.middleware.cors import CORSMiddleware
from core import setup as db_setup
from api.v1 import auth,product,category
from utils.sql import add_admin_user_to_db

from config import setting

settings = setting.AppSettings()


class AppBuilder():
    def __init__(self) -> None:
        self._app = FastAPI(
            title=settings.API_TITLE,
            description=settings.API_DESCRIPTION)
        
    
    def register_routes(self):
        
        self._app.include_router(auth.auth_router, prefix=settings.API_PREFIX)
        
        self._app.include_router(product.product_router, prefix=settings.API_PREFIX)
        
        self._app.include_router(category.category_router, prefix=settings.API_PREFIX)
        
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
        
    
    def register_admin_user(self):
        add_admin_user_to_db()
        
    
    def get_app(self):
        self.register_databases()
        self.register_routes()
        self.register_exceptions()
        self.register_middlewares()
        self.register_admin_user()
        
        return self._app