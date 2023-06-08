import math
from packages.fonction import *
import random

rep = 1
while rep == 1:
    random_number = random.randint(0, 49)
    print("\nTABLE:\n\n|0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |\n"
          "|10|11|12|13|14|15|16|17|18|19|\n"
          "|20|21|22|23|24|25|26|27|28|29|\n"
          "|30|31|32|33|34|35|36|37|38|39|\n"
          "|40|41|42|43|44|45|46|47|48|49|\n")
    print("\nLes nombres pairs sont liés à la couleur noir et les impairs à la couleur rouge.")
    nbr_mise = input("Entrez le nombre sur lequel vous voulez miser: ")
    nbr_mise = int(nbr_mise)
    mt_mise = input("Entrez le montant de la mise: ")
    mt_mise = int(mt_mise)
    valeur_nbr = pair_impair(random_number)
    valeur_nbr_mise = pair_impair(nbr_mise)
    print(f"Votre nombre correspond à la couleur {valeur_nbr_mise}")
    print("..............\nLe nombre généré est:", random_number, " et il correspond à la couleur", valeur_nbr)

    gain = 0

    if nbr_mise == random_number:
        gain = mt_mise*3
    else:
        if valeur_nbr == 'noir' and valeur_nbr_mise == 'noir':
            gain = gain + (mt_mise / 2)
        elif valeur_nbr == 'rouge' and valeur_nbr_mise == 'rouge':
            gain = gain + (mt_mise / 2)

    gain = math.ceil(gain)
    print("Votre gain est de", gain, "\n")
    print("Voulez-vous rejouer ?\n1- Oui\n2- Non\n")
    rep = input("Rejouer: ")
    rep = int(rep)
    if rep == 2:
        print("À bientot !!!")
    while rep < 1 or rep > 2:
        print("Aucune correspondance, réessayez !")
        print("Voulez-vous rejouer ?\n1- Oui\n2- Non\n")
        rep = input("Rejouer: ")
        rep = int(rep)
