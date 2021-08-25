###############################################
# Författare: Linus Jansson 2F
# Uppgift 2
# Programmet frågar efter ett heltal och beräknar summan 1 + 4 + 9 + 16 + num^2
###############################################

# Bestämmer variblerna
num = int(input("Skriv in ett heltal > "))
sum = 0
k = 1 

while k <= num: 
    sum += k ** 2 # adderar summan med k^2
    k += 1 # Adderar 1 til "iteratorn"

print("Summan är:", sum )