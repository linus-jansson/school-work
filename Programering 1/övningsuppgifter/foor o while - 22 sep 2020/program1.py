###############################################
# Författare: Linus Jansson 2F
# Uppgift 1 Beräkna utryck med while 
# Programet beräknar värdet av uttrycket 3n+17 för alla positiva heltal n mellan 0-10, större men mindre än 10 och så länge värdet av utrycket är mindre än 100
###############################################

# Function för att lösa equationen
def f(x):
    return 3 * x + 17

print("Mellan 0 och 10")

# For 0-10
for n1 in range(11):
    print(f(n1))

print("Större än 20 men mindre än 100")

# For 21 - 99 
for n2 in range (21, 100):
    print(f(n2))


print("Så länge värdet av utrycket är mindre än 100")

# ^^^^^^
n3 = 0
while f(n3) < 100:

    print(f(n3))
    n3 += 1

