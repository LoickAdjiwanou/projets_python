print("-----Nombres en toutes lettres-----")
nombre = int(input("Entrez un nombre entre 0 et 100 (inclus): "))
TabUnites = ['un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf']
TabDizaines = ['dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf']
TabCentaines = ['dix', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante', 'soixante-dix', 'quatre-vingt', 'quatre-vingt-dix']
if nombre == 0:
    print(f"{nombre} en toutes lettres donne: zéro")
if nombre > 0 and nombre < 10:
    print(f"{nombre} en toutes lettres donne: {TabUnites[nombre-1]}")
if nombre > 9 and nombre < 100:
    unite = int(nombre / 10)
    dizaine = int(nombre % 10)
    if nombre > 9 and nombre < 17:
        print(f"{nombre} en toutes lettres donne: {TabDizaines[dizaine]}")
    elif nombre > 16 and nombre < 20:
        print(f"{nombre} en toutes lettres donne: {TabDizaines[0]}-{TabUnites[dizaine-1]}")
    if nombre > 19 and nombre < 100:
        if dizaine == 0:
            print(f"{nombre} en toutes lettres donne: {TabCentaines[unite-1]}")
        else:
            print(f"{nombre} en toutes lettres donne: {TabCentaines[unite-1]}-{TabUnites[dizaine-1]}")
if nombre > 99 and nombre < 1000:
    unite = int(nombre / 100)
    reste = int(nombre % 100)
    dizaine = int(reste / 10)
    centaine = int(reste % 10)
    if dizaine == 0 and centaine == 0:
        if unite == 1:
            print(f"{nombre} en toutes lettres donne: cent")
        else:
            print(f"{nombre} en toutes lettres donne: {TabUnites[unite-1]}-cent")
    elif dizaine != 0:
        if dizaine == 1:
            if unite == 1:
                print(f"{nombre} en toutes lettres donne: cent-{TabDizaines[centaine]}")
            else:
                print(f"{nombre} en toutes lettres donne: {TabUnites[unite-1]}-cent-{TabDizaines[centaine]}")
        else:
            if unite == 1:
                print(f"{nombre} en toutes lettres donne: cent-{TabCentaines[dizaine-1]}-{TabUnites[unite-1]}")
            else:
                print(f"{nombre} en toutes lettres donne: {TabUnites[unite-1]}-cent-{TabCentaines[dizaine-1]}-{TabUnites[centaine-1]}")
if nombre == 1000:
    print(f"{nombre} en toutes lettres donne: mille")
    