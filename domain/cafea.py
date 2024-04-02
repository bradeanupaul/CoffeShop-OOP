from domain.entity import Entity

class Cafea(Entity):
    def __init__(self, cafeaId, cafeaName, cafeaOriginCountry, cafeaPrice):
        super().__init__(cafeaId)
        self.__cafeaName = cafeaName
        self.__cafeaOriginCountry = cafeaOriginCountry
        self.__cafeaPrice = cafeaPrice

    def getCafeaName(self):
        return self.__cafeaName

    def getCafeaOriginCountry(self):
        return self.__cafeaOriginCountry

    def getCafeaPrice(self):
        return self.__cafeaPrice

    def setCafeaName(self, name):
        self.__cafeaName = name

    def setCafeaOriginCountry(self, originCountry):
        self.__cafeaOriginCountry = originCountry

    def setCafeaPrice(self, price):
        self.__cafeaPrice = price

    def __str__(self):
        return f"Id-ul cafelei: {self.getEntityId()}, Numele cafelei: {self.__cafeaName}, Tara cafelei: {self.__cafeaOriginCountry}, Pretul cafelei: {self.__cafeaPrice}"