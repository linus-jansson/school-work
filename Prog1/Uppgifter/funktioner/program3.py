###############################################
# Författare: Linus Jansson 2F
# Funktioner; Uppgift 3
# Datum = 16/02/2021
# Programmet tar in ett heltal från användaren och avgör ifall det är mindre eller större än 0
###############################################

def checkVal(n):
    if n < 0: # Kollar ifall värdet på talet är mindre än 0
        return False
    return True

heltal = int(input("Skriv in ett heltal (>= 0) "))
val = checkVal(heltal)

# En oändlig loop så länge inte värdet av talet är större eller lika med 0
while True:
    if val:
        print(f"Talet du skrev in var {heltal}")
        break
    else:
        heltal = int(input("Skriv in ett heltal (>= 0) "))
        val = checkVal(heltal)

