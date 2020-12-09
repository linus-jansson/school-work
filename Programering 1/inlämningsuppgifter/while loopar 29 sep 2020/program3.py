###############################################
# Författare: Linus Jansson 2F
# Uppgift 3
# Programet frågar efter ett heltal och sen beräknar den harmoniska serien
###############################################

# Definerar variabler
num = int(input("Skriv in ett heltal > "))
sum = 0
k = 1 

# Så länge k är mindre än num
while k <= num: 
    sum += 1/k # Addera 1 / k på summan (1 / 1) + (1 / 2) + (1 / 3) + (1 / 4)
    k += 1 

print("Summan är:", sum )