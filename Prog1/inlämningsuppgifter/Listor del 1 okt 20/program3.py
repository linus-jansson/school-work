###############################################
# Författare: Linus Jansson 2F
# Uppgift 3
# Programet tar bort dubbleter i en lista
###############################################

lista = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40] # Lista med alla numemr
nyLista = [] # en ny lista för att lägga nummrerna i minus dubbleter

for n in lista:
    # Kollar ifall n finns i den nya listan eller inte för att avgöra ifall det är en dubblet
    if n not in nyLista:
        nyLista.append(n) # lägg till n i nya listan

print("Listan med dubbletter:", end=" ")
print(lista)

print("Listan utan dubbletter:", end=" ")
print(nyLista)