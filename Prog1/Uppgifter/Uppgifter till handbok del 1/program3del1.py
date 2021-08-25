###############################################
# Författare: Linus Jansson 2F
# Uppgift ett ränteproblem del 1; 
# Datum = 01/13/2021
###############################################
start = 3000
change = start
changeFactor = 1.02
desiredChange = 5000
year = 0

while change < desiredChange:
    change *= changeFactor
    year += 1

print(f"Efter {year} år så finns det {round(change, 2)} kr på konto")