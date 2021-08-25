###############################################
# Författare: Linus Jansson 2F
# Uppgift 6
# Programet räknar ut medelvärdet på tal som användaren skriver in
###############################################


# Funktionen som räknar ut medelvärdet på en lista
def medelvarde(lista = [0]):
    return float(sum(lista) / len(lista))

# Tar in tal från användaren
tal = input("Skriv in några tal tex \"2.5 5 6.2 -6.4\": ").split(" ")

# Gör om varje tal som användaren matar in till en float lista
lista = [float(i) for i in tal]

# Skriver ut medlvärdet på listan
print(f"Talen du matade in har medelvärdet {medelvarde(lista)}")
