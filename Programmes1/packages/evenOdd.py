def pair_impair():
    n = input("Entrez un nombre: ")
    n = int(n)
    if n % 2 == 0:
        print(f"{n} est un nombre pair.")
    else:
        print(f"{n} est un nombre impair.")
