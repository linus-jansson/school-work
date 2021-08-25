###############################################
# Författare: Linus Jansson 2F
# Uppgift 1
# Programet kollar först ifall ett namn finns i en lista och om det finns det så tar den bort namnet från listan
# Sen så frågar den om ett namn som man vill lägga till i listan och sen visar den listan och hur många namn som finns i listan
###############################################

# Definerar en lista med namn
lista = ["linus", "erik", "vilhem", "albin", "david", "hugo", "eli", "edvin", "linus"]

# A & B

inputNamn = input("Skriv in ett namn > ")

# Kollar ifall namnet finns i listan
if inputNamn.lower() in lista:

    # För varje element i listan så kollar den ifall inputNamn är lika med elementet och tar bort den 
    for n in lista:
        if n == inputNamn:
            lista.remove(n)
    
    print(f"{inputNamn} finns i listan, tar bort den.")
    print(lista)
else:
    print(f"{inputNamn} finns inte i listan, inget tas bort.")


# C)

# Frågar användaren efter ett namn
inputNamn = input("Skriv in ett namn som du vill lägga till i listan> ")

# Lägger till namnet i listan
lista.append(inputNamn)

# Skriver ut att en ändring har hänt och hur många namn som finns i listan
print(f"{inputNamn} las till i listan. Nu finns det {len(lista)} namn i listan")
print(lista)