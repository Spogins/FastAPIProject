from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response, status, Request
from src.blog.containers import Container
from src.blog.repository import NotFoundError
from src.blog.schemas import BlogModel
from src.blog.services.blog import BlogService

app = APIRouter()


@app.get("/blogs", status_code=status.HTTP_200_OK)
@inject
async def get_all(blog_service: BlogService = Depends(Provide[Container.blog_service])):
    return await blog_service.get_blogs()


@app.get("/blog/{blog_id}", status_code=status.HTTP_200_OK)
@inject
async def get_by_id(
        blog_id: int,
        blog_service: BlogService = Depends(Provide[Container.blog_service])):
    try:
        return await blog_service.get_blog_by_id(blog_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@app.delete("/blog/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_by_id(
        blog_id: int,
        blog_service: BlogService = Depends(Provide[Container.blog_service])):
    try:
        await blog_service.delete_blog_by_id(blog_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)