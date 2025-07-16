
from sqladmin import ModelView
from sqlalchemy import Column, Integer, String


from src.core.db import Base


class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)



class CardAdmin(ModelView, model=Card):
    column_list = [
        Card.id,
        Card.title,

    ]