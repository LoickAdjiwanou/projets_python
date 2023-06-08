def nature():
    print("Entrez la longeur des cotés du triangle: ")
    cot1 = input("Entrez la longueur du premier coté: ")
    cot2 = input("Entrez la longueur de second coté: ")
    cot3 = input("Entrez la longueur du troisième coté: ")
    isocele = 0
    equilateral = 0
    commun = 0
    if cot1 == cot2:
        isocele = 1
        if cot1 == cot3:
            equilateral = 1
    elif cot1 == cot3:
        isocele = 1
    elif cot2 == cot3:
        isocele = 1

    if cot1 != cot2 and cot2 != cot3 and cot1 != cot3:
        commun = 1

    if equilateral == 1:
        print("Le triangle est équilatéral !.")
    elif isocele == 1:
        print("Le triangle est isocèle !.")
    elif commun == 1:
        print("Le triangle est commun, les trois cotés ont des longueurs différentes !.")
