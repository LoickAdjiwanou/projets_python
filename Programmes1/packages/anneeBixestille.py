def bixestille():
    annee = input("Entrez une année: ")
    annee = int(annee)
    if annee % 4 != 0:
        print("Cette annee n'est pas bissextille.")
    else:
        if annee % 100 == 0:
            if annee % 400 == 0:
                print("Cette annee est bissextille.")
            else:
                print("Cette annee n'est pas bissextille.")
        else:
            print("Cette annee est bissextille.")
