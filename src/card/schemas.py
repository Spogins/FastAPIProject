from pydantic import BaseModel

class CardContent(BaseModel):
    title: str

class GetCardModel(BaseModel):
    id: int
    title: str



class PostCardModel(BaseModel):
    title: str
