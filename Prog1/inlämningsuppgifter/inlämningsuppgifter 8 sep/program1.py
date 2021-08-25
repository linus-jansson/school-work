###############################################
# Författare: Linus Jansson 2F
# Uppgift 1 matte med heltal
# Det här programet räknar ut summan, produkten och kvoten av de två tal som använderen matar in
###############################################

# Frågar användaren efter heltal
heltalA = int(input("Mata in ett heltal > "))
heltalB = int(input("Mata in ett till heltal >"))

# Definerar summan produkten och produkten
summan = heltalA + heltalB
produkten = heltalA * heltalB
kvotA = heltalA / heltalB
kvotB = heltalB / heltalA

# Skriver ut de olika lösningarna
print("\nSumman på ditt heltal är: " + str(summan))
print("Produkten på ditt heltal är " + str(produkten))
print("Kvoterna på talen är : " + str(kvotA) + " och " + str(round(kvotB, 3))) # Har två möjliga kvoter A/B och B/A