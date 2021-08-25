# Ber användaren om en sträng med ord
ord = input("Skriv in ett antal ord: ")

# Gör om strängen till en lista med ord
listaMedOrd = ord.split()

# Skriver ut till användaren
print(f"Du skrev {len(listaMedOrd)} ord")
print(f"Det första ordet du skrev var: {listaMedOrd[0]}")
print(f"Det sista ordet du skrev var: {listaMedOrd[-1]}")

