###############################################
# Författare: Linus Jansson 2F
# Uppgift 3
# Bryter ut filtypen på ett filnamn
###############################################

# Tar in filnamnet och typen och splitar den 
filnamn = input("Skriv in filnamnet för att hitta typen på filen (tex program.py) > ").split(".")

# Skriver ut sista elementet i arrayen
print(f"Typen av filen är en {filnamn[-1]}")