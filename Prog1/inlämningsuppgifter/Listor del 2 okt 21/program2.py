###############################################
# Författare: Linus Jansson 2F
# Uppgift 2
# Programet gör listor med hjälp av list comprehension
###############################################

lista1 = [i for i in range(6, 23, 4)] # Går från 6-22 med 4 hopp mellan varje
lista2 = [i for i in range(9, -7, -5)] # Från 9 till (-6) med -5 varje hopp
lista3 = [-(i / 10) for i in range(15, 26, 2)] # Går från 15 - 26 med 2 steg i varje och sen delar nummret på 10 och ggr med -1

# Skriver ut de listorna
print(lista1)
print(lista2)
print(lista3)
