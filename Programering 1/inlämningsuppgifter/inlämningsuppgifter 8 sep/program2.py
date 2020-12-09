###############################################
# Författare: Linus Jansson 2F
# Uppgift 1; Udda eller jämt
# Frågar användaren efter ett tal och sen kollar ifall det är udda eller jämt
###############################################

heltal = int(input("Skriv in ett heltal så kan jag avgöra ifall det är jämt eller udda > "))

if (heltal % 2 == 0):
    print(str(heltal) + " Är ett jämnt tal")
else:
    print(str(heltal) + " Är ett udda tal")
