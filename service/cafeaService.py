import random

from repository.cafeaRepository import Repository
from domain.cafea import Cafea


class CafeaService:
    def __init__(self, cafeaRepository: Repository):
        self.__cafeaRepository = cafeaRepository

    def createRandomId(self):
        ok = 1
        randomId = random.randint(1, 100)
        for entity in self.__cafeaRepository.getAllEntities():
            if entity.getEntityId() == randomId:
                ok = 0
        if ok == 1:
            return randomId
        else:
            self.createRandomId()

    def getAllCafea(self):
        return self.__cafeaRepository.getAllEntities()

    def addCafea(self, cafeaName, cafeaOriginCountry, cafeaPrice):
        cafeaId = self.createRandomId()
        if not float(cafeaPrice):
            raise TypeError("Pretul cafelei trebuie sa fie de tip float.")
        if float(cafeaPrice) <= 0:
            raise TypeError("Pretul cafelei trebuie sa fie mai mare decat 0.")
        cafea = Cafea(cafeaId, cafeaName, cafeaOriginCountry, cafeaPrice)
        self.__cafeaRepository.addEntity(cafea)

    def sortCafea(self):
        cafeaList = self.getAllCafea()
        sortedList = sorted(cafeaList, key=lambda x: (x.getCafeaOriginCountry(), x.getCafeaPrice()))
        return sortedList

    def filterCafea(self, inputCountry, inputPrice):
        cafeaList = self.getAllCafea()
        sortedList = []
        for cafea in cafeaList:
            if cafea.getCafeaOriginCountry() == inputCountry and float(cafea.getCafeaPrice()) <= float(inputPrice):
                sortedList.append(cafea)
        return sortedList

