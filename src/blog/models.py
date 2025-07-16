
from sqladmin import ModelView
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.dialects.postgresql import JSONB

from src.core.db import Base


class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    notice = Column(String, index=True)
    content = Column(JSONB)


class BlogAdmin(ModelView, model=Blog):
    column_list = [
        Blog.id,
        Blog.title,
        Blog.notice,
        Blog.content,
    ]