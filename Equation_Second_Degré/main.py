#This is a simple python project
import math

print("Entrez les coefficients x, y et z: ")
a = input("Entrez x: ")
a = int(a)
b = input("Entrez y: ")
b = int(b)
c = input("Entrez z: ")
c = int(c)

if a == 0:
    if b == 0:
        print("Aucune solution !")
    else:
        if c == 0:
            print("La solution est x=0.")
        else:
            print("La solution est x=", (-c / b))
else:
    d = (b * b)-(4 * a * c)
    d = float(d)
    if d < 0:
        print("Aucune solution dans R.")
    else:
        if d == 0:
            print("La solution unique est x=", (-b / (2 * a)))
        else:
            x1 = ((-b - math.sqrt(d)) / (2 * a))
            x2 = ((-b + math.sqrt(d)) / (2 * a))
            print("Les solutions de l'équation sont x1=", x1, " et x2=", x2)

