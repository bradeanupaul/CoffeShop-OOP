class Repository:
    def __init__(self):
        self._entities = {}

    def getAllEntities(self):
        return list(self._entities.values())

    def getEntityById(self, entityId):
        if entityId in self._entities:
            return self._entities[entityId]
        return None

    def addEntity(self, entity):
        self._entities[entity.getEntityId()] = entity


