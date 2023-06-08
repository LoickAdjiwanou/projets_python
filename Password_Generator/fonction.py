import random

def all():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chiffres = "0123456789"
    caracteres = "#!\/$%?&*()_+`:.'><'}~{[¯]}¼³²¦¬¤¢£@±"

    def rand():
        alpha = random.randint(0, 25)
        chifr = random.randint(0, 9)
        carac = random.randint(0, 36)
        return alpha, chifr, carac

    alpha, chifr, carac = rand()

    passwd = list()
    type(passwd)
    i = 0
    while i < 3:
        passwd.append(alphabet[alpha])
        passwd.append(chiffres[chifr])
        passwd.append(caracteres[carac])
        rand()
        alpha, chifr, carac = rand()
        i += 1
    return passwd