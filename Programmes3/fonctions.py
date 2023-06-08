import random


def fonc_divisibles():
    liste5 = list()
    type(liste5)
    liste7 = list()
    type(liste7)
    x, y = 0, 0
    for x in range(1500, 2700):
        if x % 5 == 0:
            liste5.append(x)

    for y in range(1500, 2700):
        if y % 7 == 0:
            liste7.append(x)

    print(f"Les nombres entre 1500 et 2700 divisibles par 5 sont: {liste5}"
          f"\nEt ceux divisibles par 7 sont: {liste7}.")


def devinette():
    print("Essayez de deviner le nombre entre 1 et 9: ")
    x = random.randint(1, 9)
    nb = int(input("Entrez le nombre deviné par l'ordinateur: "))
    while nb != x:
        nb = int(input("Entrez le nombre deviné par l'ordinateur: "))

    if nb == x:
        print("Bravo !!!")

