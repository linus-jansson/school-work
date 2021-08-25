###############################################
# Författare: Linus Jansson 2F
# Uppgift 2; Jämför tal
# Användaren skriver in två tal och programet avgör ifall dom är lika eller inte
###############################################

heltal1 = float(input("Skriv in ett tal >> "))
heltal2 = float(input("Skriv in ett till tal >> "))

if heltal1 == heltal2:
    print(str(heltal1) + " och " + str(heltal2) + " Är samma tal")
else:
    print(str(heltal1) + " och " + str(heltal2) + " Är INTE samma tal")