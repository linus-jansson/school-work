###############################################
# Författare: Linus Jansson 2F
# Selektion extrauppgifter del 2; Uppgift 1
# Programmet frågar efter ett tal och kollar ifall det är delbart med 8
###############################################

# Definerar efter det användaren matar in
num = int(input("Skriv in ett tal > "))

# Kollar ifall talet är delbart med 7
if num % 7 == 0:
    print(num, "är delbart med 7")
else:
    print(num, "är inte delbart med 7")