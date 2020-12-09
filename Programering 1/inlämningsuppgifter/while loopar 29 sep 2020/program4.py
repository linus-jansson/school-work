###############################################
# Författare: Linus Jansson 2F
# Uppgift 4
# Programet frågar om hur långt från marken en boll släpps
###############################################

# Definerar Varibalerna 
Y = int(input("Hur långt upp läpps bollen? > ")) # Y i höjd
marginal = 0.01 # 1 cm marginal 
studs = 0 


# Kollar så att Y är större eller lika med 1cm marginal
while Y >= marginal:
    Y *= 0.7 # Tar bort 30% av höjden varje studs
    studs += 1 # Adderar ett studs

print("Det tog " + str(studs) + " för den att stanna")
