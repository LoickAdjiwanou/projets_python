n1 = 0
n2 = 1
prochain = n1 + n2
termes = int(input("Entrez le nombre de termes de la série: "))
print(f"Série de Fibonacci à {termes} termes: ")
i = 3
print(n1)
print(n2)
while i <= termes:
    print(prochain)
    n1 = n2
    n2 = prochain
    prochain = n1 + n2
    i += 1
    