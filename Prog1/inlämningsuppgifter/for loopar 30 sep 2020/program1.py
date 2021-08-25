###############################################
# Författare: Linus Jansson 2F
# Uppgift 1
# Beräknar summan av en pattern n^2
###############################################

# Definerar variablerna
num = int(input("Skriv in ett heltal? > "))
k = 0
sum = 0

# For n in range 0 och det användaren matar in
for n in range(0, num + 1):
    sum += k**2
    k += 1

# Printar ut summan
print("Summan blir: " + str(sum))