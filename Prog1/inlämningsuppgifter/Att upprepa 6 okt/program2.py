###############################################
# Författare: Linus Jansson 2F
# Uppgift 2
# Programet frågar efter posetiva heltal och skriver ut det största när användaren skriver ett negativt tal
###############################################

nMin = int(input("Skriv ett posetivt heltal (Negativt för att avbryta programet) > "))
nMax = 0

# Oändlig loop så länge det tal som användaren skriver in är större än 0.
while True and (nMin > -1):
    num = int(input("Skriv ett posetivt heltal (Negativt för att avbryta programet) > "))

    # Kollar ifall användaren skriver in ett tal som är mindre än 0 o
    # Sedan kollar den ifal num är större än nMin och sen om den är större än nMax
    if num < 0:
        break
    if num < nMin:
        nMin = num
    elif num > nMax:
        nMax = num


if nMin > -1:   # vi vill inte att den ska skriva ut ifall användaren skriver -1 
    print("Det största talet är {} och det minsta talet är {}".format(nMax, nMin))