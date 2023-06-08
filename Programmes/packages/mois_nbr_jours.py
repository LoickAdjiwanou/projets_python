def nbrjours():
    n = input("Entrez le numéro du mois: ")
    n = int(n)
    if n == 1:
        print("Le mois de Janvier (1) compte 31 jours.")
    elif n == 2:
        print("Le mois de Février (2) compte 28 jours.")
    elif n == 3:
        print("Le mois de Mars (3) compte 31 jours.")
    elif n == 4:
        print("Le mois de Avril (4) compte 30 jours.")
    elif n == 5:
        print("Le mois de Mai (5) compte 31 jours.")
    elif n == 6:
        print("Le mois de Juin (6) compte 30 jours.")
    elif n == 7:
        print("Le mois de Juillet (7) compte 31 jours.")
    elif n == 8:
        print("Le mois de Aout (8) compte 31 jours.")
    elif n == 9:
        print("Le mois de Septembre (9) compte 30 jours.")
    elif n == 10:
        print("Le mois de Octobre (10) compte 31 jours.")
    elif n == 11:
        print("Le mois de Novembre (11) compte 30 jours.")
    elif n == 12:
        print("Le mois de Décembre (12) compte 31 jours.")
    elif n < 1 or n > 12:
        print("Le numéro de ce mois n'existe pas !")
