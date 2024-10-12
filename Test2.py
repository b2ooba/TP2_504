class FizzBuzz:
    def __init__(self, name):
        self.name = name

    def affiche():
        result = ""
        for i in range(1, 101):
            if i % 15 == 0:
                result += "FrisBee"  
            elif i % 3 == 0:
                result += "Fizz"
            elif i % 5 == 0:
                result += "Buzz"
            else:
                result += str(i)
        print(result)
    affiche()
    def factorielle(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorielle(n - 1) 
    print("\n")
    def affiche_n(n1, n2):
        result = ""
        for i in range(n1, n2 + 1):
            if i % 15 == 0:
                result += "FrisBee"
            elif i % 3 == 0:
                result += "Fizz"
            elif i % 5 == 0:
                result += "Buzz"
            else:
                result += str(i)
        return result 
    print("La reponse pour n1 et n2 est :") 
    print(affiche_n(5, 10))
    def factorielle(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorielle(n - 1)
