# FizzBuzz.py
class FizzBuzz:
    def __init__(self, name):
        self.name = name

    def affiche(self, n):
        result = ""
        for i in range(1, n + 1):
            if i % 15 == 0:
                result += "FrisBee"
            elif i % 3 == 0:
                result += "Fizz"
            elif i % 5 == 0:
                result += "Buzz"
            else:
                result += str(i)
        return result  # Retourne le résultat
