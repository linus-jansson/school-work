###############################################
# Författare: Linus Jansson 2F
# Uppgift 1
# Summerar alla nummer i en lista
###############################################

lista = [1, 2, 3, 4, 5, 6, 7, 9, 2, 2]
summa = 0

# För varje index på listan så ska den addera värdet till summan
for n in lista:
    summa += n

print(f"summan på listan är {summa}")