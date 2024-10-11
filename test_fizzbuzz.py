import unittest
from fizzbuzz import affiche  # On supposera que la méthode existe dans fizzbuzz.py (elle n'existe pas)

class TestFizzBuzz(unittest.TestCase):
    def test_affiche(self):
        # Vérification de l'existence de la méthode et du bon affichage
        expected_output = (
            "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617Fizz1819BuzzFizz"
        )
        self.assertEqual(affiche(), expected_output)

if __name__ == '__main__':
    unittest.main()
