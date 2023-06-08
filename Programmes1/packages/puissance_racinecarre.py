import math


def puissance():
    nbr = input("Entrez un nombre: ")
    puis = input("Entrez la puissance à laquelle vous voulez l'élever: ")
    resul = math.pow(int(nbr) , int(puis))
    print(f"{nbr} élevé à la puissance {puis} est égale à {resul}.")


def racine_carree():
    nbr = input("Entrez un nombre: ")
    resul = math.sqrt(int(nbr))
    print(f"La racine carrée de {nbr} est {resul}.")
