from domain.cafea import Cafea
from repository.cafeaRepository import Repository


class fileRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def addEntity(self, cafea):
        super().addEntity(cafea)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                cafeaId = line.split()[0]
                cafeaName = line.split()[1]
                cafeaOriginCountry = line.split()[2]
                cafeaPrice = line.split()[3]
                cafea = Cafea(cafeaId, cafeaName, cafeaOriginCountry, cafeaPrice)
                self._entities[cafeaId] = cafea

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for cafea in self.getAllEntities():
                f.write(f'{cafea.getEntityId()} {cafea.getCafeaName()} {cafea.getCafeaOriginCountry()} {cafea.getCafeaPrice()}\n')