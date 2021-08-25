###############################################
# Författare: Linus Jansson 2F
# Funktioner; Uppgift 1
# Datum = 16/02/2021
# Räknar uhopp summorna av 1 + 2 + 3 + N
###############################################

def factorial(N):
    summa = 0
    for x in range(1, N):
        print(f"{summa} + {x} = {summa + x}")
        summa += x 
    return summa

heltal = int(input("Ange ett heltal som den ska addera ihop > "))

print(factorial(heltal))