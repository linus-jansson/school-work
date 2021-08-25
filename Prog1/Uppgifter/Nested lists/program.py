###############################################
# Författare: Linus Jansson 2F
# Listor i listor; Uppgift 1-4
# Datum = 03/17/2021
# Hantering av olika element i listor som har inre listor
###############################################
def heltal(x, y): # Lägger till heltal i en lista 
    returnList = []
    
    for n in range(x, y+1):
        returnList.append(n)

    return returnList

def isPrime(n): # kollar ifall ett tal är ett primtal
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        
        return True
        
def primtal(x): # Räknar ut primtal och lägger in det i en lista
    returnList = []

    for n in range(3, x*5):
        if len(returnList) < x:
            if isPrime(n):
                returnList.append(n)

    return returnList

def kvadraten(x): # Kvadrera en lista
    temp = []
    for n in x:
        temp.append(n*n)
    return temp

# Räknar ut multiplicationstabeller 
def multiTabell(x, y):
    tabell = []
    for n in range(x, y + 1): # För varje tabell
        inner = []
        for i in range(1, 11): # Räkna ut varje tal mellan 1-10 i tabellen
            inner.append(i*n)
        tabell.append(inner)
    return tabell

# Frågar användaren vilken uppgift som ska köras
uppgift = input("Vilken uppgift vill du köra? (1, 2, 3, 4) > ")

# Huvud loopen
while True:
    if uppgift == "1":
        resultat = [heltal(1, 5), primtal(5)]
        for lista in resultat:
            print(lista)
        break
    elif uppgift == "2":
        resultat = [kvadraten(heltal(1, 5)), kvadraten(primtal(5))]
        for lista in resultat:
            print(lista)
        break
    elif uppgift == "3":
        tabell = multiTabell(1,10)
        for n in tabell:
            for i in n:
                print(f"{i}\t", end="")
            print("\n")
                
        break
    elif uppgift == "4":
        resultat = [heltal(1, 100), primtal(100)]
        for lista in resultat:
            print(lista)
        break