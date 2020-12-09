###############################################
# Författare: Linus Jansson 2F
# Uppgift 8
# Datum = 10/11/2020
# Programet räknar ut hur många gram medicin en patient ska få beroende på patientens vikt
###############################################
weight = int(input("Hur mycket väger du i kg? "))

# Räknar ut hur många mg medicin man ska få beroende på vikt
def medicineCalculator(weight):
    if weight < 20:
        return 0.05 * weight
    elif 20 <= weight <= 40:
        return 0.1 * weight
    else:
        return 0.15 * weight

# returnerar ut svaret
print(f"Du ska ta {medicineCalculator(weight)} mg medicin")
