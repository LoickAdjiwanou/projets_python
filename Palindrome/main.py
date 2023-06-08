mot = input("Entrez un mot: ")
mot_renverse = "".join(reversed(mot))
i = 0
palindrome = 0
while i < len(mot):
    lettre1 = mot[i]
    lettre2 = mot_renverse[i]
    if lettre1 == lettre2:
        palindrome += 1
    i += 1

if palindrome == len(mot):
    print(f"Le mot {mot} est un palindrome !")
else:
    print(f"Le mot {mot} n'est pas un palindrome !")
    