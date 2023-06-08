def caracteres():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chiffres = "0123456789"
    symboles = ",'.;:{(})_-+=*&?%$/!|±@£¢¤¬¦²³¼½¾[]~¯µ"
    c = input("Entrez n'importe quel caractère du clavier: ")
    i = 0
    j = 0
    k = 0
    alpha = 0
    chifr = 0
    symb = 0
    while i < len(alphabet):
        if c == alphabet[i]:
            alpha += 1
        i += 1

    while j < len(chiffres):
        if c == chiffres[j]:
            chifr += 1
        j += 1

    while k < len(symboles):
        if c == symboles[k]:
            symb += 1
        k += 1

    if alpha != 0:
        print("Le caractère est une lettre de l'alphabet.")
    elif chifr != 0:
        print("Le caractère est un chiffre.")
    elif symb != 0:
        print("Le caractère est un symbole.")
