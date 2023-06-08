import functions


def maximum():
    n1 = int(input("Entrez le premier nombre: "))
    n2 = int(input("Entrez le second nombre: "))
    n3 = int(input("Entrez le troisieme nombre: "))
    n = int(functions.maximum(n1, n2, n3))
    print(f"Le plus grand nombre est {n}")


def sommeliste():
    print("Entrez les cinqs nombres de la liste: ")
    liste = list()
    type(liste)
    x1 = int(input("=>"))
    liste.append(x1)
    x2 = int(input("=>"))
    liste.append(x2)
    x3 = int(input("=>"))
    liste.append(x3)
    x4 = int(input("=>"))
    liste.append(x4)
    x5 = int(input("=>"))
    liste.append(x5)

    i, somme, multi = 0, 0, 1
    while i < len(liste):
        somme = somme + liste[i]
        multi = multi * liste[i]
        i += 1

    print(f"La somme des elements de votre liste est: {somme} et le produit est : {multi}.")


def retourner():
    chaine = input("Entrez la chaine: ")
    print(f"L'inverse de votre chaine est: {functions.retourner_chaine(chaine)}")


def factorielle():
    nb = -1
    while nb < 0:
        nb = int(input("Entrez le nombre dont vous voulez la factorielle: "))

    print(f"La factorielle de {nb} est {functions.factorielle(nb)}.")


def unique():
    taille = int(input("Entrez le nombre d'éléments de votre liste: "))
    i = 1
    liste = list()
    type(liste)
    unique_liste = list()
    type(unique_liste)
    while i <= taille:
        x = int(input(f"{i}=> "))
        liste.append(x)
        i += 1

    j, k, trouve, element, occ = 0, 0, 0, 0, 0
    long = len(liste)
    while j < long:
        element = liste[j]
        occ = liste.count(element)
        if occ == 1:
            unique_liste.append(element)
        j += 1

    print(f"Les nombres uniques de votre liste sont: {unique_liste}")


def upp_low():
    phr = input("Entrez votre phrase: ")
    grs, pts = functions.upper_lower(phr)
    print(f"Votre phrase comporte {grs} lettres en grand(s) caractère(s)"
          f" et {pts} lettres en petits caractères.")


def even_liste():
    tail = int(input("Entrez le nombre d'éléments de votre liste: "))
    i, j = 1, 0
    nombres = list()
    type(nombres)
    while i <= tail:
        x = int(input(f"{i}=> "))
        nombres.append(x)
        i += 1
    print(f"Votre liste est: {nombres}")
    evens = list()
    type(evens)
    while j < len(nombres):
        res = float(nombres[j] % 2)
        if res != 0:
            nombres.remove(nombres[j])
        j += 1
    print(f"Les éléments pairs de votre liste sont: {nombres}")


def parfait():
    par = int(input("Entrez un nombre entier: "))
    functions.parfait(par)


def pangram():
    phr = input("Entrez votre phrase:")
    res = functions.pangram(phr)
    if res == 26:
        print("Votre phrase est un pangram.")
    else:
        print("Votre phrase n'est pas un pangram.")


def ordre_alphabetique():
    lts = input("Entrez les mots: ")
    print(f"En ordre alphabetique: {functions.ordre_alphabetique(lts)}")


def ordre_alphabetique():
    i, liste_mots, mt = 0, list(), ""
    type(liste_mots)
    n = int(input("Entrez le nombre de mots de votre liste: "))
    while i < n:
        mt = input(f"Mot n¯{i+1}: ")
        liste_mots.append(mt)
        i += 1

    print(f"Les mots en ordre alphabetique: {sorted(liste_mots)}")

def produit(n):
    m = input("Entrez un nombre: ")
    m = m*2
    return produit(m)

