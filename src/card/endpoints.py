from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response, status, Request
from src.card.containers import Container
from src.card.repository import NotFoundError
from src.card.schemas import PostCardModel, GetCardModel
from src.card.services.card import CardService

app = APIRouter()


@app.get("/cards", status_code=status.HTTP_200_OK)
@inject
async def get_all(card_service: CardService = Depends(Provide[Container.card_service])):
    return await card_service.get_cards()


@app.get("/card/{card_id}", status_code=status.HTTP_200_OK)
@inject
async def get_by_id(
        card_id: int,
        card_service: CardService = Depends(Provide[Container.card_service])):
    try:
        return await card_service.get_card_by_id(card_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@app.delete("/card/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_by_id(
        card_id: int,
        card_service: CardService = Depends(Provide[Container.card_service])):
    try:
        await card_service.delete_card_by_id(card_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/create_card", status_code=status.HTTP_201_CREATED)
@inject
async def create_card(card: PostCardModel, card_service: CardService = Depends(Provide[Container.card_service])):
    return await card_service.create_card(card)


@app.post("/create_cards", status_code=status.HTTP_201_CREATED)
@inject
async def create_cards(amount: int, card_service: CardService = Depends(Provide[Container.card_service])):
    return await card_service.create_cards(amount)


@app.delete("/delete_cards", status_code=status.HTTP_201_CREATED)
@inject
async def delete_cards(card_service: CardService = Depends(Provide[Container.card_service])):
    return await card_service.delete_cards()

