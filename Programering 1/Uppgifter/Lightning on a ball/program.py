###############################################
# Författare: 
# Funktioner; Uppgift 1
# Datum = 17/02/2021
# 
# ’M’ markerar m ̈orker, dvs obelyst punkt d ̈ar b ≤ 0
# ’*’ markerar en ganska m ̈ork punkt 0 < b ≤ 0.3
# ’+’ markerar en n ̊agot ljusare punkt 0.3 < b ≤ 0.5
# ’-’ markerar en ganska ljus punkt 0.5 < b ≤ 0.7
# ’.’ markerar en ljus punkt 0.7 < b ≤ 0.9
# ’ ’ markerar en mycket ljus punkt 0.9 < b ≤ 1
# x0 & y0 : positionen på ljuskällan
###############################################

import math

r = float(input("Bestäm en radie på klotet > "))
xn = float(input("Bestäm x0 > ")) # x0
yn = float(input("Bestäm y0 > ")) # y0

zn = ( r**2 - xn**2 - yn**2 )**(1/2) # z0

print(zn)

pk = 1 # proportionalitetskonstanten

x = 0
y = 0

# if negative:
#     b = 0

z = ( r**2 - x**2 - y**2 )**(1/2)
 

b = (x * xn + yn + z + zn) / (r*r)

def calculate_sphere():
    pass

def draw_sphere():
    pass

def calculate_rays():
    pass