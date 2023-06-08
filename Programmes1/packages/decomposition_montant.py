def decomposition():
    montant = input("Entrez un montant: ")
    montant = int(montant)
    nbr = 0
    n = 0
    nbr = int(montant / 10000)
    nbr10000 = nbr
    nbr = montant % 10000
    n = nbr
    nbr = int(n / 5000)
    nbr5000 = nbr
    nbr = n % 5000
    n = nbr
    nbr = int(n / 2000)
    nbr2000 = nbr
    nbr = n % 2000
    n = nbr
    nbr = int(n / 1000)
    nbr1000 = nbr
    nbr = n % 1000
    n = nbr
    nbr = int(n / 500)
    nbr500 = nbr
    nbr = n % 500
    n = nbr
    nbr = int(n / 200)
    nbr200 = nbr
    nbr = n % 200
    n = nbr
    nbr = int(n / 100)
    nbr100 = nbr
    nbr = n % 100
    n = nbr
    nbr = int(n / 50)
    nbr50 = nbr
    nbr = n % 50
    n = nbr
    nbr = int(n / 25)
    nbr25 = nbr
    nbr = n % 25
    n = nbr
    nbr = int(n / 10)
    nbr10 = nbr
    nbr = n % 10
    n = nbr
    nbr = int(n / 5)
    nbr5 = nbr
    nbr = n % 5
    n = nbr
    nbr = int(n / 1)
    nbr1 = nbr
    print(f"Votre montant est constitué de:\nBillets de 10000: {nbr10000},\n"
          f"Billets de 5000: {nbr5000},\n"
          f"Billets de 2000: {nbr2000},\n"
          f"Billets de 1000: {nbr1000},\n"
          f"Billets de 500: {nbr500},\n"
          f"Pièces de 200: {nbr200},\n"
          f"Pièces de 100: {nbr100},\n"
          f"Pièces de 50: {nbr50},\n"
          f"Pièces de 25: {nbr25},\n"
          f"Pièces de 10: {nbr10},\n"
          f"Pièces de 5: {nbr5},\n"
          f"Pièces de 1: {nbr1}.")
