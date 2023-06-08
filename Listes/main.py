liste = [9, 12, 23, -34, -2, 41, 6, -76, 12, 100, -5, -2, 777, 6, -41, 12]
print("-----------")
#Éléments d'une liste
print("Affichage des éléments de la liste: ")
for elt in liste:
    print(elt)
print("-----------")
#Éléments d'une liste inférieurs à 0
print("Affichage des éléments négatifs de la liste: ")
for elt in liste:
    if elt < 0:
        print(elt)
print("-----------")
#Somme des éléments de la liste
for elt in liste:
    somme = 0
    somme = int(somme + elt)
print(f"La somme des éléments de la liste est {somme}.")
print("-----------")
#Maximum et Minimum de la liste
maxi = max(liste)
mini = min(liste)
print(f"Le plus petit élément de la liste est {mini} et le plus grand est {maxi}.")
print("-----------")
#Second plus grand élément de la liste
liste2 = liste
maxi2 = max(liste2)
liste2.remove(maxi2)
maxi2 = max(liste2)
print(f"Le second plus grand élément de la liste est {maxi2}.")
print("-----------")
#Nombre d'éléments pairs et impairs
pairs = 0
impairs = 0
for elt in liste:
    if elt % 2 == 0:
        pairs += 1
    else:
        impairs += 1
print(f"Le nombre d'éléments pairs est {pairs} et impairs est {impairs}.")
print("-----------")
#Insérer un élément dans une liste
liste.append(754)
print("On ajoute un élément à la fin de la liste: ")
for elt in liste:
    print(elt)
print("-----------")
#Supprimer un élément à un endroit spécifié dans la liste
print(f"On supprime l'élément à la 3ème place ({liste[2]}): ")
del liste[2]
for elt in liste:
    print(elt)
print("-----------")
#Fréquence d'un nombre dans la liste
freq, i = 0, 0
while i < len(liste):
    nombre = liste[i]
    for elt in liste:
        if nombre == elt:
            freq += 1
    print(f"Le nombre {nombre} de trouve {freq} fois dans la liste.")
    freq = 0
    i += 1
print("-----------")
#Affichage des éléments qui ne se trouvent qu'une seule fois dans la liste
frequ, j = 0, 0
liste3 = []
while j < len(liste):
    nbr = liste[j]
    for el in liste:
        if nbr == el:
            frequ += 1
    if frequ == 1:
        liste3.append(nbr)
    frequ = 0
    j += 1
print("Les nombres ne se trouvant qu'une seule fois dans la liste sont: ")
for n in liste3:
    print(n)
print("-----------")
#Nombre total d'éléments dupliqués dans la liste
freq, i = 0, 0
liste4 = []
while i < len(liste):
    nombre = liste[i]
    for elt in liste:
        if nombre == elt:
            freq += 1
    if freq == 2:
        liste4.append(nombre)
    freq = 0
    i += 1
nombre_duplique = len(liste4) // 2
print(f"Le nombre d'éléments dupliqué dans la liste sont: {nombre_duplique}.")
print("-----------")
#Supprimer tous les éléments dupliqués de la liste
freq, i = 0, 0
liste4 = []
while i < len(liste):
    nombre = liste[i]
    for elt in liste:
        if nombre == elt:
            freq += 1
    if freq == 2:
        liste.remove(nombre)
        liste.remove(nombre)
    freq = 0
    i += 1
print(f"Éléments de la liste après suppression des éléments dupliqués: {liste}")
print("-----------")
#Fusionner deux listes dans une troisième
liste5 = [123, 5, 567, 67, 758, 8, 5, 78, 463,9, 3, 79, 45]
liste.extend(liste5)
liste_fusion = liste
print(liste_fusion)
print("-----------")
#Renverser la liste
print(f"La liste au départ: {liste}: ")
liste.reverse()
print(f"La liste après le retournement: {liste}")
print("-----------")
#Mettre les nombre pairs et impairs d'une liste dans deux autres différentes listes
pairs = []
impairs = []
for elt in liste:
    if elt % 2 == 0:
        pairs.append(elt)
    else:
        impairs.append(elt)
print(f"La liste au départ: {liste}.")
print(f"La liste des nombres pairs: {pairs}.")
print(f"La liste des nombres impairs: {impairs}.")
print("-----------")
#Recherche d'un élément dans la liste
rec = int(input("Entrez l'élément que vous recherchez: "))
trouve = 0
for elt in liste:
    if rec == elt:
        trouve += 1
if trouve != 0:
    print(f"Le nombre {rec} se trouve dans la liste. Le nombre d'occurences de ce nombre est: {trouve}.")
else:
    print(f"Le nombre {rec} ne se trouve pas dans la liste.")
print("-----------")
#Classer les éléments de la liste dand l'ordre croissant et décroissant
print(f"La liste au départ: {liste}.")
liste.sort()
print(f"La liste en ordre croissant: {liste}.")
liste.reverse()
print(f"La liste en ordre décroissant: {liste}")
print("-----------")
#Classer les éléments de la liste dand l'ordre croissant et décroissant dans deux
#autres selon qu'ils soient pairs ou impairs
print(f"La liste au départ: {liste}.")
pairs.sort()
print(f"La liste des nombres pairs en ordre croissant: {pairs}.")
pairs.reverse()
print(f"La liste des nombres pairs en ordre décroissant: {pairs}.")
impairs.sort()
print(f"La liste des nombres impairs en ordre croissant: {impairs}.")
impairs.reverse()
print(f"La liste des nombres impairs en ordre décroissant: {impairs}.")
print("-----------")
#Rotation de la liste à gauche
long = len(liste)//2
print(f"La liste au départ: {liste}.")
liste = liste[long:] + liste[:long]
print(f"La liste après une rotation à gauche: {liste}.")
liste = liste[-long:] + liste[:-long]
print(f"La liste après une rotation à droite: {liste}.")
print("-----------")
