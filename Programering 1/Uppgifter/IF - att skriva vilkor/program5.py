###############################################
# Författare: Linus Jansson 2F
# Uppgift 5
# Datum = 10/11/2020
# Estimerar hur lång en person kommer bli beroende på kön och föräldrars längd
###############################################

# Tar in kön och föräldras längd
sex = int(input("Vilket kön är det? (1 för kille 0 för tjej) > "))
dadLength = int(input("Hur lång är pappan? i cm > "))
momLength = int(input("Hur lång är mamman? i cm > "))

# Funktion som räknar ut ungifärlig längd beroende på kön och föräldras längd
def estimatedLength(sex, PL, ML):
    if sex == 0:
        return (PL + ML - 13) / 2
    else:
        return (PL + ML + 13) / 2

print(f"barnet kommer ungefär bli {estimatedLength(sex, dadLength, momLength)}")