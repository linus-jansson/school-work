###############################################
# Författare: Linus Jansson 2F
# Uppgift 3 Collatz förmodan
# Tar ner användarens tal till ett med hjälp av Collatz förmodan
###############################################

# Num defineras utifrån vad användaren skriver in
num = int(input("Ange ett heltal > "))


# Så länge talet är mer än 1 så kör den Collatz förmodan
while num > 1:

    if num % 2 == 0:
        num = num / 2
    else:
        num = num * 3 + 1

    print("Ditt tal ligger på: " + str(num))