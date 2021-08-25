###############################################
# Författare: Linus Jansson 2F
# Uppgift 3
# Talet skriver ut en tabel 1-12 och skriver ut kvadraten och kubik på talet
###############################################

# För varje tal mellan 1-12
for n in range(1, 13):
    # Höj upp med 2 och 3 och skriv ut det formaterat
    print(f"{n:2}. {n**2:2}. {n**3}.")
    