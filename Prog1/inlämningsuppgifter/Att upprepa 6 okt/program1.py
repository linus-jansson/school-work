###############################################
# Författare: Linus Jansson 2F
# Uppgift 1
# Programet frågar om hur långt från marken en boll släpps. Användaren kan skriva in det flera gånger.
###############################################

# En oändlig loop så att användaren kan skriva in flera gånger
while True:

    # Definerar Varibalerna 
    Y = int(input("Hur långt upp läpps bollen? ( >= 0 för att avbryta programet) > ")) # Y är höjd i meter
    marginal = 0.01 # 1 cm marginal 
    studs = 0 

    if Y <= 0: # Kollar ifall det användaren skrivit in är mindre än eller lika med noll        
        break

    # Kollar så att Y är större eller lika med 1cm marginal
    while Y >= marginal:
        Y *= 0.7 # Tar bort 30% av höjden varje studs
        studs += 1 # Adderar ett studs

    print("Det tog " + str(studs) + " för den att stanna")