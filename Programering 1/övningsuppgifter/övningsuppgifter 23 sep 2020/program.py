###############################################
# Författare: Linus Jansson 2F
# Uppgift: Maximal ersättning
# Programmet frågar efter en max vikt och en max volym och sen räknar ut vad den maximala ersättningen är
###############################################

# Frågar användaren efter max vikt och max volym på bilen
maxLastVolym = int(input("Vad är max volymen på lastbilen? (Liter) > "))
maxLastVikt = int(input("Vad är max vikten på lastbilen? (kg) > "))

Emax = 0 # maximal ersättning i kr
stora = 0 # Antelet stora lådor vid maximal erästtning
sma = 0 # antelet små lådor vid maximal ersättning

# x är stora lådor och y är små lådor

# Räknar ut totala volymen i liter
def V(x, y):
    return (200 * x) + (50 * y)

# Räknar ut totala massan i kg
def m(x, y): 
    return (5 * x) + (20 * y)

# Räknar ut ersättningen i kr
def E(x, y):
    return (40 * x) + (25 * y)

# För varje x och y så kollar den volymen, massan och ersättningen
for x in range(int(maxLastVolym / 200 ) + 1):
    for y in range(1, int(maxLastVikt / 20) + 1):
        if ( V(x, y) <= maxLastVolym and m(x, y) <= maxLastVikt):
            if ( E(x, y) > Emax):
                stora = x
                sma = y
                Emax = E(x, y)
            # print("Lasta " + str(x) + " stora och " + str(y) + " små lådor för att få den maximal ersättnigen " + str(E(x, y)))
            


print("Tony ska lasta " + str(stora) + " stora och " + str(sma) + " små lådor för att få den maximal ersättnigen " + str(Emax) + "kr")