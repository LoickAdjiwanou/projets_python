import os
from packages.fonction import *

reprise = 1
reprise = int(reprise)
while reprise == 1:
    print("___MENU___\n1- Somme\n2- Soustraction\n3- Produit\n4- Division\n5- Modulo\n\n")
    choix = input("Quelle opération entre deux nombres souhaitez-vous faire (entrez 1 ou 2) : ")
    choix = int(choix)


    if choix == 1:
        print("Vous avez choisi la somme, entrez les deux nombre: \n")
        nbr1 = input("Entrez le premier nombre: ")
        nbr2 = input("Entrez le second nombre: ")
        resultat = somme(nbr1, nbr2)
        print(f"La somme des deux nombres est {resultat}")
    elif choix == 2:
        print("Vous avez choisi la soustraction, entrez les deux nombre: ")
        nbr1 = input("Entrez le premier nombre: ")
        nbr2 = input("Entrez le second nombre: ")
        resultat = soustraction(nbr1, nbr2)
        print(f"La soustraction du premier nombre par le second est {resultat}")
    elif choix == 3:
        print("Vous avez choisi le produit, entrez les deux nombre: \n")
        nbr1 = input("Entrez le premier nombre: ")
        nbr2 = input("Entrez le second nombre: ")
        resultat = produit(nbr1, nbr2)
        print(f"La produit des deux nombres est {resultat}")
    elif choix == 4:
        print("Vous avez choisi la division, entrez les deux nombre: \n")
        nbr1 = input("Entrez le premier nombre: ")
        nbr2 = input("Entrez le second nombre: ")
        resultat = division(nbr1, nbr2)
        print(f"La division du premier nombre par le second est {resultat}")
    elif choix == 5:
        print("Vous avez choisi le modulo, entrez les deux nombre: \n")
        nbr1 = input("Entrez le premier nombre: ")
        nbr2 = input("Entrez le second nombre: ")
        resultat = modulo(nbr1, nbr2)
        print(f"Le modulo du premier nombre par le second est {resultat}")
    elif choix < 1 or choix > 5:
        print("Aucune option !")

    print("Voulez-vous recommencer ?\n1- Oui\n2- Non")
    reprise = input("Entrez 1 ou 2: ")
    reprise = int(reprise)

if reprise != 1:
    print("Au revoir !")


os.system("pause")
