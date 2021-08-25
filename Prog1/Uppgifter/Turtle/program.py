###############################################
# Författare: Linus Jansson 2F
# Nivå 2; uppgift 11
# Datum = 03/16/2021
# Genererar en cool figur med turtle
###############################################

import turtle as t

def skum_rektangel(x): 
    if x <= 360:
        t.left(x) # Programet bestämmer hur mycket den första rotationen ska rotera
        t.forward(150)
        t.left(-85)
        t.forward(90)
        t.left(-110)
        t.forward(110)
        t.left(-55)
        t.goto(0,0)
        t.setheading(0)

t.speed("fastest")

grupper = 0
medlemmar = 0
v = 45
while grupper < 3: # 3 grupper
    while medlemmar < 4: # 4 figurer per grupp
        skum_rektangel(v) # Ritar ut en figur
        v += 10 # Ökar rotationsvinkeln
        medlemmar += 1
    v += 70 # klar med en grupp ökar roations vinkeln mer
    medlemmar = 0
    grupper += 1

t.done() # klar