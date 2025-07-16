from pydantic import BaseModel


class BlogModel(BaseModel):
    id: int
    title: str
    notice: str
