def divi511():
    n = input("Entrez un nombre: ")
    n = int(n)
    if n % 5 == 0:
        if n % 11 == 0:
            print(f"{n} est divisible à la fois par 5 et par 11.")
    else:
        print(f"{n} n'est pas divisible par 5 et par 11.")
