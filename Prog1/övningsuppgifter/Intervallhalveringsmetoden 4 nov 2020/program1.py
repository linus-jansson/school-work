###############################################
# Författare: Linus Jansson 2F
# Uppgift 1
# Programmet använder sig av intervallhalvering för att hitta en rot på en ekvation 
# där intervallet ligger mellan 2 och 3
###############################################

# Definerar f(x) och räknar ut tredje gradsfunktionen
def f(x):
    return x**3 - 7*x**2 + 29

a = 2
b = 3
m = 0

# Letar efter nollstället så länge differensen mellan a och b är större än 0.0001
while b - a > 0.001:
    m = (a + b) / 2

    if f(a) * f(m) < 0:
        b = m
    else:
        a = m

print(f"Ekvationen har ett nollställe x = {round(m, 3)}")
