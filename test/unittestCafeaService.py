import unittest

from repository.cafeaRepository import Repository
from service.cafeaService import CafeaService

class TestCafeaService(unittest.TestCase):
    def setUp(self):
        self.cafeaRepository = Repository()
        self.CafeaService = CafeaService(self.cafeaRepository)
        self.CafeaService.addCafea("Lavatzza", "Italia", "10")

    def testAddCafea(self):
        self.CafeaService.addCafea("Lattee", "Italia", "15")
        cafele = self.CafeaService.getAllCafea()
        self.assertTrue(len(cafele) == 2, "Trebuie sa fie 2 cafele.")
        self.assertTrue(cafele[1].getCafeaName() == "Lattee", "A doua cafea este numita Lattee.")

if __name__ == '__main__':
    unittest.main()


