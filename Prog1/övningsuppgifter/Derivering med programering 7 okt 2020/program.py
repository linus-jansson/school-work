###############################################
# Författare: Linus Jansson 2F
# Uppgift 1; Derivering med programering
# uppgift 2: 
#   f'(4) är ungefär 51.20999999999981
#   f'(4) är ungefär 50.12009999999805
#   f'(4) är ungefär 50.01200100001313
#   f'(4) är ungefär 50.00120001000141
#   f'(4) är ungefär 50.000119998117036
#   f'(4) är ungefär 50.0000119956212
# Uppgift 3:
#   f'(3) är ungefär 29.910000000000068
# Uppgift 4:
#   ff'(2) är ungefär 26.49000000000001
# Uppgift 5:
#   g'(1) är ungefär 15.937424601000023
# Uppgift 6:
#   gg'(2) är ungefär 7.496380917422423
###############################################

# Definerar funktionerna
def f1(x):
    return x**3 + 2 * x + 5

def f2(x):
    return x**2 - x**3 + 35 * x - 20

def f3(x):
    return x ** 10

def f4(x):
    return x ** x

# Räknar ut prima a av funktionen 
def prim_x(x, h, num = 1):
    if (num == 1):
        return (f1(x + h) - f1(x)) / h
    elif (num == 2):
        return (f2(x + h) - f2(x)) / h
    elif (num == 3):
        return (f3(x + h) - f3(x)) / h
    elif (num == 4):
        return (f4(x + h) - f4(x)) / h


# Definerar x och h
num = int(input("1. f1(x) = x^3 + 2x + 5\n2. f2(x) = x^2 - x^3 + 35x - 20\n3. f3(x) = x^10\n4. f4(x) = x^x\nVilken av funktionerna ovan vill du hitta lutningen för? > ")) # frågar användaren vilken funktion denne vill anvönda
x = int(input("Till vilket x vill du hitta lutningen? > "))
h = 1.0

# Ittererar genom flera h som är 10 ggr mindre
for n in range(10):
    h /= 10
    print(f"{['f1', 'f2', 'f3', 'f4'][num - 1]}'({x}) \u2248 {prim_x(x, h, num)}")