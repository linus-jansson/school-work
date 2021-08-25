# Kollar ifall talet som matas in i funktionen är ett primtal. Retunerar True ifall det är det annars false
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print("Välkommen till primtalskontrollatorn")

# Bet användaern om en siffra
inmatat_tal = input("Mata in Talet du vill kontrollera: ")
n = int(inmatat_tal)

# 1)
if isPrime(n):
    print(n, "är ett primtal")
else:
    print(n, "är inte ett primtal")

# 2)
print("Skriver ut alla primtal mellan 2 och 100: ")
for num in range(2, 101):
    if isPrime(num):
        print(num)

