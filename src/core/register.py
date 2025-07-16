from dependency_injector import containers, providers
from config.settings import WIRING_CONFIG
from src.auth.containers import Container as AuthContainer
from src.core.containers import Container as DatabaseContainer
from src.users.containers import Container as UserContainer
from src.blog.containers import Container as BlogContainer
from src.card.containers import Container as CardContainer


class RegisterContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=WIRING_CONFIG)
    users_container = providers.Container(UserContainer)
    auth_container = providers.Container(AuthContainer)
    db_container = providers.Container(DatabaseContainer)
    blog_container = providers.Container(BlogContainer)
    card_container = providers.Container(CardContainer)
