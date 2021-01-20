###############################################
# Författare: Linus Jansson 2F
# Uppgift ett Pytagoreiska tal-tripler; 
# Datum = 01/13/2021
###############################################
maxL = int(input("Hur många tal vill du testa? "))
antal = 0

for a in range(3, maxL):
    for b in range(a + 1, maxL):
        for c in range(b + 1, 2*maxL):
            if a*a + b*b == c*c:
                print(a,b,c)
                antal += 1

print(f"{antal} lösningar")