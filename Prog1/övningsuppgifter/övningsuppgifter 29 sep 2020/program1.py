###############################################
# Författare: Linus Jansson 2F
# Uppgift ; Djurparken
# 
###############################################

barn = int(input("Hur många barn biljeter ska du köpa? > "))
vuxna = int(input("Hur många vuzen bljet ska du köpa? > "))

barnPris =  200 * barn
vuxenPris = 300 * vuxna

print("För barnet kostade det " + str(barnPris) + " och för de vuxna kostade det " + str(vuxenPris) + " Med en total på " + str(barnPris + vuxenPris) )
