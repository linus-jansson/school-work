###############################################
# Författare: Linus Jansson 2F
# Uppgift 7
# Får in tal från användaren och räknar ut medianen på dem talen
###############################################

# Funktionen som räknar ut medelvärdet på en lista
def median(lista = [0]):
    median = 0 # Definerar medianen
    # Sorterar listan
    lista.sort()

    if len(lista) % 2 == 0:
        # Hittar talet i mitten (medelvärdet) mellan två nummer i mitten
        median = ( lista[ (len(lista) // 2) - 1 ] + lista[ (len(lista) // 2) ] ) / 2
    else:
        # Hämtar värdet på elementet i mitten av den sorterade listan. Vilket kommer finnas eftersom att den är udda
        median = lista[len(lista) // 2]

    # Returnerar medianen från funktionen
    return median 

# Tar in decimaltal från användaren
tal = input("Skriv in några tal tex \"2.5 5 6.2 -6.4\": ").split(" ")

# Gör om varje decimaltal till en float lista
lista = [float(i) for i in tal]

# Skriver ut medianen på listan och skriver ut den
print(f"Decimaltalen du matade in har medianen {round(median(lista), 3)}")
