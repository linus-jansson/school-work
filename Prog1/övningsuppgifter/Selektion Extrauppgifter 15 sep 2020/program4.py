###############################################
# Författare: Linus Jansson 2F
# Selektion extrauppgifter del 2; Uppgift 4
# Programmet frågar efter en ålder och pris och sen så avgör den ifall användaren får rabatt eller inte
###############################################

# Bestämmer variablerna ålder, pris och rabatt
age = int(input("Skriv in din ålder i heltal > "))
price = int(input("Hur mycket kostar varan eller varorna du köper? > "))
discount = 0.8

# Kollar ifall användaren får rabatt eller itne
if age >= 65 or age <= 12:
    print("Du får rabatt! " + str( price * discount ) + " kr kostar det istället för " + str( price ) + "kr")
else: 
    print("Du får ingen rabatt. Din total blir: " + str(price) + "kr")