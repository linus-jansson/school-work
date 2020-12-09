###############################################
# Författare: Linus Jansson 2F
# Uppgift 1; största talet
# Användaren skriver in två tal och programet skriver ut det största talet
###############################################

heltal1 = float(input("Skriv in ett tal >> "))
heltal2 = float(input("Skriv in ett till tal >> "))

# Avgör vilket heltal som är störst
if (heltal1 > heltal2):
    print(str(heltal1) + " är större än " + str(heltal2))
else: 
    print(str(heltal2) + " är större än " + str(heltal1))