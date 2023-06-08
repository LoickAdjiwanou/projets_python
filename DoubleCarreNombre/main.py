def carre_double(nbr):
    car = (int)(nbr)*(int)(nbr)
    db = (int)(nbr) * 2
    return car, db


print("Entrez un nombre: ")
nombre = input()
(carr, doub) = carre_double(nombre)
print(f"Le double de nombre est {doub} et son carré est {carr}")
