###############################################
# Författare: Linus Jansson 2F
# Uppgift 5
# Delar upp olika saker som användaren matar in 
###############################################

# A)
# Tar in namnen och gör det till en lista
namn = input("Skriv in några namn tex \"nils kurt\" > ").split(" ")

# Skriver ut listan
print(namn)



# B)
# Tar in heltal från användaren och gör det till en lista
heltal = input("Skriv in några heltal tex \" 5 76 1 -21 -31\" > ").split(" ")

# Skriver ut listan med heltal
print(heltal)

# Sorterar listan med heltal 
heltal.sort()

# Skriver ut den sorterade listan med heltal
print(heltal)