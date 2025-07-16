from fastapi import APIRouter
from src.blog.endpoints import app as blog_app
from src.blog.views import blog_views
from src.users.endpoints import app as user_app
from src.users.views import user_views
from src.auth.endpoints import app as auth_app
from src.auth.views import auth_views

router_app = APIRouter()
API_PREFIX = "/api/v1"

# ENDPOINTS
router_app.include_router(auth_app, prefix=API_PREFIX, tags=["Auth"])
router_app.include_router(user_app, prefix=API_PREFIX, tags=["Users"])
router_app.include_router(blog_app, prefix=API_PREFIX, tags=["Blog"])

# VIEWS
router_app.include_router(auth_views)
router_app.include_router(user_views)
router_app.include_router(blog_views)
