from typing import Callable
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.blog.models import Blog
from src.blog.schemas import BlogModel


class BlogRepository:

    def __init__(self, session_factory: Callable[..., AsyncSession]) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> list[BlogModel]:
        async with self.session_factory() as session:
            result = await session.execute(select(Blog))
            blogs = result.scalars().all()
            return [BlogModel(id=blog.id, title=blog.title, notice=blog.notice) for blog in blogs]

    async def get_by_id(self, blog_id: int) -> BlogModel:
        async with self.session_factory() as session:
            blog = await session.get(BlogModel, blog_id)
            if not blog:
                raise HTTPException(status_code=401, detail=f"Blog not found, id: {blog_id}")
            return BlogModel(id=blog.id, title=blog.title, notice=blog.notice)

    async def add(self, blog_model: BlogModel) -> BlogModel:
        async with self.session_factory() as session:
            blog = BlogModel(id=blog_model.id, title=blog_model.title, notice=blog_model.notice)
            session.add(blog)
            await session.commit()
            await session.refresh(blog)
            return blog

    async def delete_by_id(self, blog_id: int) -> None:
        async with self.session_factory() as session:
            blog = await session.get(BlogModel, blog_id)
            if not blog:
                raise HTTPException(status_code=401, detail=f"Blog not found, id: {blog_id}")
            await session.delete(blog)
            await session.commit()

class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class BlogNotFoundError(NotFoundError):

    entity_name: str = "Blog"