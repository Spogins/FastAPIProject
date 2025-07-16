from typing import Callable
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.card.models import Card
from src.card.schemas import PostCardModel, GetCardModel


class CardRepository:

    def __init__(self, session_factory: Callable[..., AsyncSession]) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> list[GetCardModel]:
        async with self.session_factory() as session:
            result = await session.execute(select(Card))
            cards = result.scalars().all()
            return [GetCardModel(id=card.id, title=card.title) for card in cards]

    async def get_by_id(self, card_id: int) -> GetCardModel:
        async with self.session_factory() as session:
            card = await session.get(Card, card_id)
            if not card:
                raise HTTPException(status_code=401, detail=f"Card not found, id: {card_id}")
            return GetCardModel(id=card.id, title=card.title)

    async def add(self, card_model: PostCardModel) -> Card:
        async with self.session_factory() as session:
            card = Card(title=card_model.title)
            session.add(card)
            await session.commit()
            await session.refresh(card)
            return card

    async def delete_by_id(self, card_id: int) -> None:
        async with self.session_factory() as session:
            card = await session.get(Card, card_id)
            if not card:
                raise HTTPException(status_code=401, detail=f"Card not found, id: {card_id}")
            await session.delete(card)
            await session.commit()

class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class CardNotFoundError(NotFoundError):

    entity_name: str = "Card"