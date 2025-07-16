from pydantic import BaseModel

class BlogContent(BaseModel):
    title: str
    text: str

class GetBlogModel(BaseModel):
    id: int
    title: str
    notice: str
    content: BlogContent


class PostBlogModel(BaseModel):
    title: str
    notice: str
    content: BlogContent