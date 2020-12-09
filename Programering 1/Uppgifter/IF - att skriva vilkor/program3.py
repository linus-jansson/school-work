###############################################
# Författare: Linus Jansson 2F
# Uppgift 3
# Datum = 10/11/2020
# Hittar vilken kostnad som en person får beroende på åldern
###############################################

age = int(input("Hur gammal är du? > "))

# Kollar ifall åldern är mellan värde
if 0 <= age <= 17:
    print("Din biljet kostar 200kr")
elif 18 <= age <= 64:
    print("Din blijet kostar 350 kr")
elif age >= 65:
    print("Din biljett kostar 250kr")
else:
    print(f"{age} är inte en giltig ålder")