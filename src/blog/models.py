from sqladmin import ModelView
from sqlalchemy import Column, Integer, String
from src.core.db import Base


class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    notice = Column(String, index=True)


class BlogAdmin(ModelView, model=Blog):
    column_list = [
        Blog.id,
        Blog.title,
        Blog.notice,
    ]