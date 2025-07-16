from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.responses import RedirectResponse
from config_fastapi.fastapi_mgr import templates

blog_views = APIRouter()

@blog_views.get('/blog', include_in_schema=False)
@inject
async def blog(request: Request):
    return templates.TemplateResponse(name='blog.html', context={'request': request})