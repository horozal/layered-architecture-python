from app.repositories.entity_repository import EntityRepository
from app.adapters.entity_adapter import UserRepository
from app.models.entity import Entity

class EntityService:
    def __init__(self):
        self.entity_repository = UserRepository()
        self.entity_adapter = UserAdapter()  
