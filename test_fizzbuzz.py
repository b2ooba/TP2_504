def affiche(n1, n2):
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
    return result  # On retourne la chaîne de caractères
print(affiche(5, 10))