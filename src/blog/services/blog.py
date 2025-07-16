from typing import Iterator, Callable
from src.blog.models import Blog
from src.blog.repository import BlogRepository


class BlogService:

    def __init__(self, blog_repository: BlogRepository) -> None:
        self._repository: BlogRepository = blog_repository


    async def get_blogs(self) -> Iterator[Blog]:
        return await self._repository.get_all()

    async def get_blog_by_id(self, blog_id: int) -> Blog:
        return await self._repository.get_by_id(blog_id)

    async def delete_blog_by_id(self, blog_id: int) -> None:
        return await self._repository.delete_by_id(blog_id)

    async def create_blog(self, blog):
        return await self._repository.add(blog)

