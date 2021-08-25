###############################################
# Författare: Linus Jansson 2F
# Uppgift 4
# Datum = 10/11/2020
# Kollar vilken typ av vinkel något har som anvöndaren skriver in
###############################################

angle = int(input("Skriv in en vinkel > "))

# Räknar ut vilken typ av vinkel det är beroende på vinkel
if angle == 0:
    print("0 Vinkel")

elif 0 < angle < 90:
    print("vinkeln är spetsig")
elif angle == 90:
    print("Vinkeln är spetsig")
elif 90 < angle < 180:
    print("vinkeln är trubbig")
elif angle == 180:
    print("vinkeln är en rak linje")
elif 180 < angle < 360:
    print("Vinkeln är en reflexvinkel")
elif angle == 360:
    print("Vinkeln är en full vinkel")
else: 
    print("Vinkeln du har skrivit in är inte mellan 0-360")