from app.models.entity import Entity

class EntityController(Entity):
    def request(self) -> str:
        return f"Entity controller"
