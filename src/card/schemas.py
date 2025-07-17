from pydantic import BaseModel


class GetCardModel(BaseModel):
    id: int
    title: str

class PostCardModel(BaseModel):
    title: str
