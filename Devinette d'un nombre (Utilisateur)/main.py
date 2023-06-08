import  random

def ordi_devine(x):
    petit = 1
    grand = x
    retour = ''
    devine = 0
    while retour != 'c':
        if petit != grand:
            devine = random.randint(petit, grand)
        else:
            devine = petit   #ou grand car petit == grand
        retour = input(f"{devine} est-il trop grand(G), trop petit(P), ou correct(C) ?? ")
        if retour == 'g':
            grand = devine - 1
        elif retour == 'p':
            petit = devine + 1

    print(f"L'ordinateur a deviné votre nombre: {devine}.")

ordi_devine(10)