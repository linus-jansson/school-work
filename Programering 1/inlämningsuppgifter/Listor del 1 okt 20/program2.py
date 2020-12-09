###############################################
# Författare: Linus Jansson 2F
# Uppgift 2
# Tar fram det största och det minsta nummret i en lista
###############################################

lista = [1, 2, -8, 0]
storst = lista[0] # Det första talet i listan är alltid störst innan den vet nästa

# Avgör vilken som är störst mellan elementet i listan och det största och minsta variabeln
for n in lista:
    if n > storst:
        storst = n

# Skriver ut det största och det minsta
print(f"Största talet i listan är {storst}")