import math


def jours_mois_annee():
    jrs = input("Entrez le nombre de jours: ")
    nbr_semaines = int(jrs) / 7
    nbr_jours_restants1 = nbr_semaines - int(nbr_semaines)
    nbr_jours_restants1 = math.ceil(nbr_jours_restants1 * 7)
    nbr_semaines = int(nbr_semaines)
    print(f"{jrs} jours correspond à {nbr_semaines} semaines et {nbr_jours_restants1} jours.")
    nbr_mois = int(jrs) / 30
    nbr_jours_restants2 = nbr_mois - int(nbr_mois)
    nbr_jours_restants2 = math.ceil(nbr_jours_restants2 * 30)
    nbr_mois = int(nbr_mois)
    print(f"{jrs} jours correspond à {nbr_mois} mois et {nbr_jours_restants2} jours.")
    nbr_annee = int(jrs) / 365
    nbr_jours_restants3 = nbr_annee - int(nbr_annee)
    nbr_jours_restants3 = math.ceil(nbr_jours_restants3 * 365)
    nbr_annee = int(nbr_annee)
    print(f"{jrs} jours correspond à {nbr_annee} années et {nbr_jours_restants3} jours.")
