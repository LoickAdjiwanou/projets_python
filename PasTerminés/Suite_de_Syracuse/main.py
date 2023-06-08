n = int(input("Entrez le nombre n à partir duquel la suite sera initiée: "))
liste = list()
liste.append(14)
while n != 0:
    if n != 0:
        if n % 2 == 0:
            n = n/2
            liste.append(n)
        elif n % 2 != 0:
            n = (3*n)/2
            liste.append(n)


i = len(liste)
while i != 0:
    print(liste[i])
i -= 1

