###############################################
# Författare: Linus Jansson 2F
# Uppgift 1; Udda eller jämt
# Frågar användaren efter ett brutto och en skatte stats och räknar ut nettolönen
###############################################

# Sätter variablerna till det användaren skriver in
brutto = float(input("Vad är bruttoinkomsten? (tex 27,500.32) > "))
skatt = float(input("Vad är skattesatsen? (tex 0.3) > "))

# Räknar ut nettolönen
netto = brutto - (brutto * skatt)

# Skriver ut nettolönen
print("Nettolönen är ca: " + str( round(netto, 3) )) # Rundar av netto