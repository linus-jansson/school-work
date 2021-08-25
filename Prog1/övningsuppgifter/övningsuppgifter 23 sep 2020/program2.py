###############################################
# Författare: Linus Jansson 2F
# Uppgift: Maximal ersättning
# Programmet räknar ut hur mycket mat man borde ta med sig för att få flest protioner
###############################################

Emax = 0 # maximal ersättning i kr
ris = 0 # Antelet ris lådor vid maximal erästtning
majs = 0 # antelet små lådor vid maximal ersättning

# x är ris och y är majs

# Räknar ut totala volymen i liter
def V(x, y):
    return (0.05 * x) + (0.05 * y)

# Räknar ut totala massan i kg
def m(x, y): 
    return (25 * x) + (10 * y)

# Räknar ut totala portionerna
def E(x, y):
    return (800 * x) + (160 * y)

# För varje x och y så kollar den volymen, massan och ersättningen
for x in range(21): # mängden ris som finns
    for y in range(1, 36): # mängden majs som finns
        if ( V(x, y) <= 2.1 and m(x, y) <= 600):
            if ( E(x, y) > Emax):
                ris = x
                majs = y
                Emax = E(x, y)
            # print("Lasta " + str(ris) + " ris och " + str(majs) + " majs för att få  " + str(Emax) + " portioner")

print("Lasta " + str(ris) + " ris och " + str(majs) + " majs för att få  " + str(Emax) + " portioner")