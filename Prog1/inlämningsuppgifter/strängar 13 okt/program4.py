###############################################
# Författare: Linus Jansson 2F
# Uppgift 4
# Frågar efter en mening och sen räkarn lägden och kollar efter första och sista meningen
###############################################

# Frågar användaren efter en mening
text = input("Skriv in en mening > ")

length = 0              # håller koll på antal tecken i strängen
c = 0                   # Håller koll på hur många ord som finns i texten

first = text.split()[0] # Gör om text till en array och tar det första ordet
last = text.split()[-1] # Gör om text till en array och tar det sista ordet

for n in text:
    if n == " ":        # Ifall det är ett mellanrum
        c += 1          # adderar 1 till c efter varje ord
        length -= 1     # tar bort ett från längden ifall det är ett mellanslag
    length += 1
    
if c < 1:               # kollar ifall det finns fler än ett ord eller inte
    print(f"\"{text}\" är inte en mening")
else:
    print(f"Din mening består av {length} tecken")        
    print(f"Första ordet i din mening är {first}")
    print(f"Sista ordet i din mening är {last}")

