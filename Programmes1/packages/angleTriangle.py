def angle():
    angle1 = input("Entrez la valeur du premier angle: ")
    angle2 = input("Entrez la valeur du second angle: ")
    angle3 = 180 - (int(angle1) + int(angle2))
    print(f"La valeur du troisième angle est {angle3}.")
