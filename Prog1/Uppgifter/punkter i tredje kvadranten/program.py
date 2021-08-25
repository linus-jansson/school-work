###############################################
# Författare: Linus Jansson 2F
# Uppgift ; tredje kvadranten
# Datum = 11/11/2020
# Programet tar reda på hur många punkter det är i den tredje kvadranten
###############################################

import random
import matplotlib.pyplot as plt

antal_punkter = 80

X = [] #Lista med x-koordinater
Y = [] #Lista med y-koordinater

count = 0

for i in range(antal_punkter):
    X.append(random.randint(-20, 20)) #Slumpad x-koordinat
    Y.append(random.randint(-20, 20)) #Slumpad y-koordinat

# för antalet punkter
for i in range(antal_punkter):
    # Så ska den kolla x[i], y[i] och kolla ifall båda är negativa.
    # Är dom det så ligger den i den 3 kvadranten
    if X[i] < 0 and Y[i] < 0: 
        count += 1

print(f"Antalet punkter i 3 kvadranten: {count}")