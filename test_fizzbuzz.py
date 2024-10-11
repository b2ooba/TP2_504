import unittest
from Test2 import FizzBuzz  # Import de la classe FizzBuzz à tester

class TestFizzBuzz(unittest.TestCase):
    def setUp(self) -> None:
        # Création d'une instance de la classe FizzBuzz avec le nom "MaClasse"
        self.instance = FizzBuzz("MaClasse")

    def test_factorielle_de_5(self):
        # Test si la méthode factorielle retourne bien 120 pour 5
        self.assertEqual(self.instance.factorielle(5), 120)

if __name__ == '__main__':
    unittest.main()
