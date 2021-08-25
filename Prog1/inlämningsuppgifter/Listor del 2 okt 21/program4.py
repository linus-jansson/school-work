###############################################
# Författare: Linus Jansson 2F
# Uppgift 4
# Programet låter användaren mata in ett personnummer och sen så skriver den ut år, månad, dag och dom 4 sista sifforna
###############################################

# Tar in personnummert och tar bort minus tecknet direkt
personnummer = input("Skriv in ett personnummer av typen ååååmmdd-xxxx > ").replace("-", "")

# Slicar de olika bitarna på personnummret. 
# Kollar också ifall användaren har matat in personnummret i typen "ååååmmdd-xxxx" eller "ååmmdd-xxxx"
if len(personnummer) == 12:
    year = slice(0, 4)
    month = slice(4, 6)
    day = slice(6, 8)
    xxxx = slice(8, 12)
elif len(personnummer) == 10:
    year = slice(0, 2)
    month = slice(2, 4)
    day = slice(4, 6)
    xxxx = slice(6, 10)
else:
    # Säger till ifall användaren inte har matat in ett gilltigt personnummer stänger av programmet
    print("Du verkar inte ha matat in en ett giltigt personnummer")
    quit()

# Skriver ut de olika delarna på personnummet
print(f"År: {personnummer[year]}")
print(f"Månad: {personnummer[month]}")
print(f"Dag: {personnummer[day]}")
print(f"xxxx: {personnummer[xxxx]}")


