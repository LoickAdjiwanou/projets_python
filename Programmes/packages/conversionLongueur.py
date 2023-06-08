def convertir():
    n = input("Entrez la longueur en centimètres: ")
    kilo = 0.00001 * int(n)
    metre = 0.01 * int(n)
    print(f"La longueur en mètres est: {metre}")
    print(f"La longueur en kilomètres est: {kilo}")
