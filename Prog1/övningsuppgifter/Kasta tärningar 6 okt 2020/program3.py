###############################################
# Författare: Linus Jansson 2F
# Uppgift: Maximal ersättning
# Räknar ut den relativa frekvensen för att 5 tärningars summa ska bli 25
###############################################

from random import randint #  Importerar slumpfunktion

while True:
    antal = 0 # Antal kast med summan 25

    n = int(input("Hur många tärningskast vill du göra? (>= 0 för att avbryta) > "))

    if n < 0:
        break 
    
    for i in range(n):
        t1 = randint(1, 6) # slumpar heltal från 1 till 6
        t2 = randint(1, 6)
        t3 = randint(1, 6)
        t4 = randint(1, 6)
        t5 = randint(1, 6)

        sum = t1 + t2 + t3 + t4 + t5

        if sum == 25:
            antal += 1 # Ökar antalet emed 1

    andel = round( ((antal / n) * 100), 1) # Relativ frekvens med en decimal
    
    print("Andel kast med poängsumma 25 (%):", andel)