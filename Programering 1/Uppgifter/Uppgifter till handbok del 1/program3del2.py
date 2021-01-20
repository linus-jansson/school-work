###############################################
# Författare: Linus Jansson 2F
# Uppgift ett ränteproblem del 2; 
# Datum = 01/13/2021
###############################################
tal = int(input("Skriv in ett tal "))
startTal = tal
evo = 0

while tal > 1:
    tal *= 0.5 # Halvera talet
    evo += 1

print(f"Det tar {evo} halveringar för att talet {startTal} ska bli mindre än 1")
