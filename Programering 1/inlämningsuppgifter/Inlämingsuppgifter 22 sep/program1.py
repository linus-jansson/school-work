###############################################
# Författare: Linus Jansson 2F
# Uppgift 1 gissa tal
# Programet frågar efter ett tal och kollar ifall användaren gissat rätt
###############################################

# Definerar Num
num = int(input("Gissa på ett tal"))

# If-satserna
if num > 10:
    print("Du gissade på ett för stort tal")
elif num < 10:
    print("Du gissade på ett för litet tal")
else:
    print("Du gissade rättt")