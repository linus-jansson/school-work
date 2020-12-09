###############################################
# Författare: Linus Jansson 2F
# Uppgift 1
# Programet gör en lista med 100 slumpmässiga tal mellan 1-1000. 
# Sen skriver den ut det minsta och det största talet samt så skriver den ut medelvärdet på talen
###############################################

from random import randint

# Definerar en tom listaa
lista = []

def medelvarde(lista = [0]):
    return sum(lista) / len(lista) # Returnerar medelvärdet på inmatad lista

# Generar listan
for n in range(101):
    lista.append(randint(1, 1000))

# Sätter första och minsta talet till första index på listan
minst = lista[0]
storst = lista[0]

# Hittar storleken på listan
for n in lista:
    if n < minst:
        minst = n
    elif n > storst:
        storst = n

# Skriver ut resultaten
print(f"Medelvärdet är på listan är: {medelvarde(lista)}")
print(f"Minsta talet i listan är {minst}")
print(f"Största talet i listan är {storst}")