from repositories.entity_repository import EntityRepository
from adapters.entity_adapter import EntityAdapter
from models.entity import Entity

class EntityService:
    def __init__(self):
        self.entity_repository = EntityRepository()
        self.entity_adapter = EntityAdapter()
 
