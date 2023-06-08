import fonction

print("PASSWORD GENERATOR\n")

result = fonction.all()
chaine = ''.join(result)
print(f"Password genereted : {chaine}")
fichier = open("passwd.txt", "r")
lines = fichier.readline()
fichier.close()


if chaine in lines:
    fonction.rand()
else:
    fichier = open("passwd.txt", "a")
    fichier.write(f"{chaine}\n")
    fichier.close()
