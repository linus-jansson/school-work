###############################################
# Författare: Linus Jansson 2F
# Uppgift 2
# Programet läser in 10 heltal in i en lista
# Sen så tar den bort alla 0or i arrayen och skriver ut den
################################################


lista = []
nyLista = []

while len(lista) <= 10:
    lista.append(int(input("Skriv in ett heltal > ")))

for n in lista:
    if n != 0:
        nyLista.append(n)

print(lista)
print(nyLista)