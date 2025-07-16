from typing import Iterator, Callable
from src.card.models import Card
from src.card.repository import CardRepository


class CardService:

    def __init__(self, card_repository: CardRepository) -> None:
        self._repository: CardRepository = card_repository


    async def get_cards(self) -> Iterator[Card]:
        return await self._repository.get_all()

    async def get_card_by_id(self, card_id: int) -> Card:
        return await self._repository.get_by_id(card_id)

    async def delete_card_by_id(self, card_id: int) -> None:
        return await self._repository.delete_by_id(card_id)

    async def create_card(self, card):
        return await self._repository.add(card)

