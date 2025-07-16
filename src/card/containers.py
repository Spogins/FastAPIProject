import passlib.hash
from dependency_injector import containers, providers
from config.settings import WIRING_CONFIG
from src.card.repository import CardRepository
from src.card.services.card import CardService
from src.core.containers import Container as db_container



class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=WIRING_CONFIG)
    card_repository = providers.Factory(CardRepository, session_factory=db_container.session)
    password_hasher = providers.Callable(passlib.hash.pbkdf2_sha256.hash)
    card_service = providers.Factory(CardService, card_repository=card_repository)