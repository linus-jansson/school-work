# Linus Jansson 2F
# Det här porgramet löser en cirkelns radie, omkrets och area med tre decimaler
import math # Importera math från python för att få ett mer acurate pi

diameter = int(input("Mata in en diameter i din UNIT > ")) # Frågar efter en diameter som den ska utgå ifrån

pi = math.pi # definerar pi så att man slipper skriva math.pi överallt

radie = diameter / 2 # Räkna ut radien 
omkrets = pi * radie**2 # Räknar ut omkretsen
area = 2 * pi * radie # Räknar ut arean

# Skriver ut resultaten
print("Radien är: ", round(radie, 3))
print("Omkretsen är: ", round(omkrets,3))
print("Arean är: ", round(area,3))