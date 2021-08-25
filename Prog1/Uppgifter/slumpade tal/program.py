###############################################
# Författare: Linus Jansson 2F
# Uppgift ; slumpmässiga tal
# Datum = 10/11/2020
# Genererar 20 tal mellan 1-50 och kollar ifall det är udda jämnt och ett primtal
###############################################

from random import randint

def isPrimeNumber(n):
    # Ifall talet är 1 så är det ett primtal
    if n > 1:
        # Hittar faktorer i talet
        for i in range(2, n):
            # Är n jämnt delbart med i så är det inte ett primtal
            if (n % i == 0):
                return False
        else:
            return True
    else:
        return False

def isEven(n):
    # Returnerar True ifall n är jämt delbart med 2
    if n % 2 == 0:
        return True
    return False

addons = ""

for k in range(21):

    n = randint(1, 50)

    if ( isEven(n) ):
        addons += "Jämnt "
    else:
        addons += "Udda "
    
    if( isPrimeNumber(n) ):
        addons += "Primtal"
        
    print(str(n) + " <-- " + addons)
    
    addons = ""