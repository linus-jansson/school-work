###############################################
# Författare: Linus Jansson 2F
# Selektion extrauppgifter del 2; Uppgift 5
# Programmet frågar efter ett årtal och kollar ifall det är ett skottår eller inte
###############################################

# Bestämmer året utifrån det användaren skriver in
year = int(input("Vilket år vill du kolla ifall det är ett skottår? > "))

# Kollar ifall det är ett skottår eller inte
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print("Året " + str(year) + " är ett skottår")
else:
    print(year, "är inte ett skottår")