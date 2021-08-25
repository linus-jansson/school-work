###############################################
# Författare: Linus Jansson 2F
# Uppgift 5.9
# Kontrollerar kontrollsiffran i ett personnummer
###############################################

# Definerar variablerna
nmr = input("Skriv in ett persnnnumer av typen ååmmdd-xxxx eller ååmmddxxxx > ")
temp = ""
summa = 0
omvaxel = False

# Tar bort minustecknet ifall personnummret har det
for n in nmr:
    if n != "-":
        temp += n

# För varje siffra av de första 9 sifforna så ska den multiplicera varje nummer med omväxlande 2 och 1 och sen räkba ihop summan
for n in temp[:9]:
    if omvaxel:
        summa += int(n) * 1
    else:
        
        if int(n) * 2 >= 10: # kollar ifall n är större eller lika med 10
            for k in str(int(n) * 2): # Adderar varje i "tal" n*2 till summan 
                summa += int(k)
        else: 
            summa += int(n) * 2

    # sätt omvaxel till motsatsa för att sen multiplicera med 2 eller 1
    omvaxel = not omvaxel

# Kollar ifall summan + konntrollsiffran är jämntdelbart med 10
if (summa + int(temp[9])) % 10 == 0:
    print(summa + int(temp[9]));
    print("Kontrollsiffran stämmer")
else:
    print("Kontrollsiffran stämmer inte")