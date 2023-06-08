def conversion():
    print("Quelle conversion voulez-vous faire ? (1/2)\n"
          "1- Celcius en Fahrenheit\n"
          "2- Fahrenheit en Celcius\n")
    choix = 0
    choix = input("Votre choix: ")
    choix = int(choix)
    while choix < 1 or choix > 2:
        input("Option non disponible, réessayez: ")

    if choix == 1:
        temp = input("Entrez la température en celcius: ")
        temp1 = (int(temp) * 1.8) + 32
        print(f"{temp} celcius correspond à {temp1} en fahrenheit")
    if choix == 2:
        temp = input("Entrez la température en fahrenheit: ")
        temp1 = (int(temp) - 32) / 1.8
        print(f"{temp} fahrenheit correspond à {temp1} en celcius")