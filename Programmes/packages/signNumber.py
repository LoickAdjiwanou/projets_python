def signe():
    n = input("Entrez un nombre: ")
    n = int(n)
    if n < 0:
        print(f"{n} est un nombre négatif.")
    elif n > 0:
        print(f"{n} est un nombre positif.")
    else:
        print(f"{n} est un nombre nul.")
