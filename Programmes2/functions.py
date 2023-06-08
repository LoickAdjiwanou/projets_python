def maximum(a, b, c):
    return max(a, b, c);


def retourner_chaine(chaine):
    inverse = "".join(reversed(chaine))
    return inverse


def factorielle(nombre):
    i, facto = 1, 1
    while i <= nombre:
        facto = facto * i
        i += 1
    return facto


def upper_lower(phrase):
    grands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    petits = "abcdefghijklmnopqrstuvwxyz"
    i, gr, pt = 0, 0, 0
    while i < len(phrase):
        if phrase[i] in grands:
            gr += 1
        elif phrase[i] in petits:
            pt += 1
        i += 1
    return gr, pt


def parfait(n):
    i, res, lis, som = 1, 0.0, list(), 0
    type(lis)
    while i <= n:
        lis.append(i)
        res = float(n % i)
        if res != 0:
            lis.remove(i)
        i += 1

    j = 0
    while j < len(lis):
        som = som + lis[j]
        j += 1

    if n == som/2:
        print(f"{n} est un nombre parfait.")
    else:
        print(f"{n} n'est pas un nombre parfait.")


def pangram(phrase):
    alphabet1 = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = alphabet1.upper()
    i, alpha, j = 0, 0, 0
    while i < len(phrase):
        while j < 26:
            if alphabet1[j] in phrase or alphabet2[j] in phrase:
                alpha += 1
            j += 1
        i += 1
    return alpha


















