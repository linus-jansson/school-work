###############################################
# Författare: Linus Jansson 2F
# Uppgift 4
# Programet räknar ut ens lön om man får 1 öre per dag fast efter varje dag man jobbar så fördubblas lönen
###############################################

# Definera variablerna
lon = 0.01
dag = 1

# Så länge lönen är mindre eller lika med 10 miljoner
while lon <= 10000000:
    lon *= 2 # Fördubbla lönen
    dag += 1 # Addera arbetsdagen med ett


# Skriv ut svaret
print("Det tar " + str(dag) + " innan han får " + str(lon) + " eller 10 miljoner")