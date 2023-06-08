def caracalpha():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c = input("Entrez un caractère: ")
    i = 0
    present = 0
    while i < len(alphabet):
        if c == alphabet[i]:
            present += 1
        i += 1

    if present != 0:
        print("Le caractère que vous avez entré fais partie de l'alphabet !")
    else:
        print("Le caractère que vous avez entré ne fais pas partie de l'alphabet !")


def voy_con():
    c = input("Entrez un caractère: ")
    voyelle = "aeiouy"
    consonne = "bcdfghjklmnpqrstvwxz"
    i = 0
    j = 0
    voy = 0
    con = 0
    while i < len(voyelle):
        if c == voyelle[i]:
            voy += 1
        i += 1

    while j < len(consonne):
        if c == consonne[j]:
            con += 1
        j += 1

    if voy != 0:
        print("Le caractère entré est une voyelle.")
    elif con != 0:
        print("Le caractère entré est une consonne.")
