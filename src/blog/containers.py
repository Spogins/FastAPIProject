import passlib.hash
from dependency_injector import containers, providers
from config.settings import WIRING_CONFIG
from src.blog.repository import BlogRepository
from src.blog.services.blog import BlogService
from src.core.containers import Container as db_container



class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=WIRING_CONFIG)
    blog_repository = providers.Factory(BlogRepository, session_factory=db_container.session)
    password_hasher = providers.Callable(passlib.hash.pbkdf2_sha256.hash)
    blog_service = providers.Factory(BlogService, blog_repository=blog_repository)