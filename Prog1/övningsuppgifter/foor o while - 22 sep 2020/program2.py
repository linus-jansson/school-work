###############################################
# Författare: Linus Jansson 2F
# Uppgift 2 Beräkna utryck med while 
# Löser ekvationen  (5x + 6) / 3 = 102
###############################################

#En function för att snygga till matten lite
def f(x):
    return (5 * x + 6 ) / 3

# Kollar För varje f(x) om den är lika med 102 eller inte
x = 0
while f(x) != 102:
    x += 1
print ("lösningen har lösningen x=", x)