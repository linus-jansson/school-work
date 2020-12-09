###############################################
# Författare: Linus Jansson 2F
# Selektion Uppgift 3
# Programmet frågar efter ett heltal och kollar ifall det är delbart med 3 eller 5
###############################################

# definerar num efter det som användaren skriver in
num = int(input("Ange ett heltal > "))

# Kollar resten och kollar ifall den blir noll om man delar med 3 eller 5
if (num % 3 == 0) and (num % 5 == 0):
    print(str(num) + " är delbart med 3 och 5")
elif (num % 3 == 0):
    print(str(num) + " är delbart med 3")
elif (num % 5 == 0):
    print(str(num) + " är delbart med 5")
else:
    print(str(num) + " är varken delbart med 3 eller 5")
