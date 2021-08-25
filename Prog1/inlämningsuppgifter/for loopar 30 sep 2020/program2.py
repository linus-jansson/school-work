###############################################
# Författare: Linus Jansson 2F
# Uppgift 2 & 3
# Skriver ut lösningarna på en funktionen f(x) = 2x^2 - 5x + 1
###############################################

# En function som retunerar functionen beroende på x
def f(x):
    return 2 * x ** 2 - 5 * x + 1

# En function som returnerar functionen f(x) mellan -10 och 10 i heltal
print("Värdena för functionen f(x) = 2x^2 - 5x + 1 där -10 < x < 10 är: ", end="\n[")
for n in range(-10, 11):
    print(f"{f(n):1}", end=", ")
print("]\n")

# Räknar x från -1.0 till 1.0 med en decimal postion
print("Värdena för functionen f(x) = 2x^2 - 5x + 1 där -10.0 < x < 10.0 är: ", end="\n[")
for n in range(-10, 11):
    print(f"{ round( f( n/10 ), 2 ):1}", end=", ") # Kör functionen f(x) där x är n och delas med 10; sedan rundar den av resultatet med 2 decimaler
print("]")