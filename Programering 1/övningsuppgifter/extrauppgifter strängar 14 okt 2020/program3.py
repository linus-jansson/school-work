###############################################
# Författare: Linus Jansson 2F
# Uppgift 5.8
# Kollar hur lång tid det är mellan två klockslag
###############################################
print("Det här programmet kollar hur lång tid det är mellan två tidpunkter i minuter")

tid1 = input("Skriv in en tidpunkt i typen tt:mm > ")
tid2 = input("Skriv ett till tidpunkt i typen tt:mm > ")

# Inmatade tiden timmen i minuter
hr1 = int(tid1[:2]) * 60
hr2 = int(tid2[:2]) * 60

# Inmatade minuter
min1 = int(tid1[3:])
min2 = int(tid2[3:])

# Räknar ut skillnaden i tider
tidDiff = (hr2 - hr1) + (min2 - min1)

# Om tiden är negativ så är tid2 på följande dag
if tidDiff < 0:
    # lägger till 24 timmar på negativt tidDiff för att få resten
    tidDiff += 24*60

print(f"Det är {tidDiff} minuter mellan {tid1} & {tid2}")