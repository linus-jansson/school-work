def isInDict(key, t):
    # Om nyckeln finns i tabellen returnera True annars false
    if key in t:
        return True
    return False

# Skriver ut värdet ifall den finns i tabellen
def printValue(key, t):
    if isInDict(key, t):
        print(t[key])
    else:
        print("Den här personen finns inte i listan")

# Skriver ut varje key och value i en lista med formatering
def printTable(tabell):
    print("{0:<10}{1:>10}".format("Namn", "Nummer"))
    for key, val in tabell.items():
        print("{0:<10}{1:>10}".format(key, val))

# Definerar en tabell med nummer och namn
telefonbok = {
    "arne": "070456345",
    "bengt": "070234234",
    "stina": "070123234",
    "lisa": "070678678"
}

# 1) 
printValue("stina", telefonbok)

# 2)
printTable(telefonbok)


