from pydantic import BaseModel


class GetBlogModel(BaseModel):
    id: int
    title: str
    notice: str


class PostBlogModel(BaseModel):
    title: str
    notice: str