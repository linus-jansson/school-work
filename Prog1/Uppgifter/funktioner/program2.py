###############################################
# Författare: Linus Jansson 2F
# Funktioner; Uppgift 2
# Datum = 16/02/2021
# Programmet gör om celcius till farhenheit
###############################################

def to_farenheit(c):
    return (c*9/5) + 32 # Formeln för att göra om celcius to farhenheit

heltal = int(input("Ange en temperatur som du vill omvandla till celcius > "))

print(to_farenheit(heltal))