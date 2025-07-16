from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.responses import RedirectResponse
from config_fastapi.fastapi_mgr import templates

card_views = APIRouter()

@card_views.get('/card', include_in_schema=False)
@inject
async def card(request: Request):
    return templates.TemplateResponse(name='card.html', context={'request': request})