def maxDeux():
    n1 = input("Entrez le premier nombre:")
    n2 = input("Entrez le second nombre: ")
    if n1 > n2:
        print(f"Le plus grand nombre est {n1}.")
    elif n1 < n2:
        print(f"Le plus grand nombre est {n2}.")
    else:
        print(f"{n1} et {n2} sont égaux.")


def maxTrois():
    n1 = input("Entrez le premier nombre:")
    n2 = input("Entrez le second nombre: ")
    n3 = input("Entrez le troisième nombre: ")
    max = 0
    if n1 > n2:
        max = n1
    else:
        max = n2

    if max < n3:
        print(f"Le plus grand nombre est {n3}.")
    else:
        print(f"Le plus grand nombre est {max}.")
