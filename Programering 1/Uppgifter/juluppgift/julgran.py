###############################################
# Författare: Linus Jansson 2F
# Uppgift ; Patiensen Klockan
# Datum = 16/12/2020
# Progremmet skriver ut en julgran :)
###############################################
import random
import colorama 
from colorama import Fore, Style

totalLines = int(input("Hur många rader ska själva trädet vara (helst 7 eller 8)? "))
length = totalLines * 2  - 1
tree = [] 


for x in range(1, length, 2):
    innehall = '*'
    if x == 1:
        innehall = 'o'
        color = Fore.YELLOW
    else:
        innehall = '*'
        color = Fore.GREEN
        
    space = ' ' * ((length - x) // 2)
    out = space + color +(innehall * x) + space
    tree.append(out)

for n in tree:
    print(n)

# Ritar ut stammen
for n in range(2):
    print(Fore.YELLOW +' ' * (((length - 1) // 2) - 2),'*' * 3)

print(Fore.RED + ' ' * (((length - 1) // 2) - 4), "GOD JUL!" + Fore.WHITE)


