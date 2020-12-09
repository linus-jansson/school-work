###############################################
# Författare: Linus Jansson 2F
# Selektion Uppgift 1 och 2
# Programet frågar efter ett heltal och kollar ifall det är 10 eller större eller mindre
###############################################

# Definerar num efter det användaren skriver in
num = int(input("Skriv ett tal > "))

# Kollar ifall det inmatna talet är större, mindre eller lika med 10
if num > 10:
    print(str(num) + " är större än 10")
elif num == 10:
    print(str(num) + " är lika med 10")
else:
    print(str(num) + " är mindre än 10")

# Kollar vilket intervall det inmattade talet ligger mellan
if num < 0:
    print(str(num) + " är mindre än 0 och ligger inte i mellan intervallet 0 - 30")
elif num > 30:
    print(str(num) + " är större än 30 så det ligger inte mellan intervallet 0 - 30")
else:
    for n in range (3): # Mellan 0 till 2 Men egentligen 1-3 som sen blir 10-30
        if num <= ( n + 1 ) * 10: # Kollar ifall nummret är större eller lika med itterationen + 1 * 10 alltså tex 20 eller 30
            print(str(num) + " finns ligger mellan " + str( (((n + 1) * 10) - 10) ) + " - " + str( ((n + 1) * 10) ) ) # Skriver ut intervallet tex 10-20 om man skriver 25
            break; # Breakar ut ur loopen 