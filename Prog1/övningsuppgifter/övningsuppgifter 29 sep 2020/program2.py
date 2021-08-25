###############################################
# Författare: Linus Jansson 2F
# Uppgift ; Djurparken
# 
###############################################

print("UPPGIFT 2, 4 & 5")
biljeter = int(input("Hur många biljeter såldes? > "))
total = int(input("Vad var det totala priset som biljeterna såldes för? > "))

for n in range(biljeter + 1):
    barn = biljeter - n
    vuxna = n
    kostnad = 300 * vuxna + 200 * barn

    if kostnad == total:
        print("Om det är " + str(vuxna) + " vuxna och " + str(barn) + " barn; så blir den totala kostnaden " + str(kostnad) + "kr")


print("UPPGIFT 6")
sedlar = int(input("Hur många sedlar var det? > "))
totalSedlar = int(input("Hur många sedlar i värde var det? > "))

for n in range(sedlar + 1):
    hundra = sedlar - n
    femhundra = n
    kostnad = 100 * hundra + 500 * femhundra

    if kostnad == totalSedlar:
        print("Om det är " + str(hundra) + " hundra lappar och " + str(femhundra) + " femhundra lappar; så blir den totala valutan " + str(kostnad) + "kr")
    
