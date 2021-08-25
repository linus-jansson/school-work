###############################################
# Författare: Linus Jansson 2F
# Uppgift 3; Medaljer vid en tävling
# Ett program som avgör vilken medalj man får om man är med i en tävling utifrån tid
###############################################

# Fråga användaren efter tiden
userTime = float(input("Ange tiden i minuter som du kom in i mål med > "))

# Avgör vilket diplom den ska få
if (1.0 > userTime < 6.0):
    print("Du får guld!")
elif (6.0 < userTime < 11.0):
    print("Du får silver")
elif (11.0 < userTime < 16.0):
    print("Du får brons")
elif (userTime > 16.0):
    print("Du får ett diplom")