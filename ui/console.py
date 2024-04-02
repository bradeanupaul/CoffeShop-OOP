from service.cafeaService import CafeaService


class Console:
    def __init__(self, cafeaService: CafeaService):
        self.__cafeaService = cafeaService

    def addCafea(self):
        try:
            cafeaName = input("Scrie numele cafelei: ")
            cafeaOriginCountry = input("Scrie tara de origine a cafelei: ")
            cafeaPrice = input("Scrie pretul cafelei: ")
            self.__cafeaService.addCafea(cafeaName, cafeaOriginCountry, cafeaPrice)
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showCafea(self):
        for entity in self.__cafeaService.getAllCafea():
            print(entity)

    def sortCafea(self):
        for entity in self.__cafeaService.sortCafea():
            print(entity)

    def filterCafea(self):
        try:
            cafeaCountry = input("Scrie tara cafelei: ")
            cafeaPrice = input("Scrie pretul cafelei: ")
            for entity in self.__cafeaService.filterCafea(cafeaCountry, cafeaPrice):
                print(entity)
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)

    def printMenu(self):
        print("1. Adauga o cafea.")
        print("2. Afiseaza cafelele.")
        print("3. Sorteaza cafelele.")
        print("4. Filtreaza cafelele.")
        print("x. Iesire.")

    def menu(self):
        while True:
            self.printMenu()
            option = input("Scrie optiunea: ")
            if option == "1":
                self.addCafea()
            if option == "2":
                self.showCafea()
            if option == "3":
                self.sortCafea()
            if option == "4":
                self.filterCafea()
            elif option == "x":
                break
            else:
                print("Optiune gresita.")