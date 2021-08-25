# Författare: Linus Jansson 2F
guess = int(input("Gissa vilket tal jag tänker på? > "))

if guess > 10:
    print("Du gissade för högt")
elif guess < 10:
    print("Du gissade för lågt")
elif guess == 10:
    print("Rätt!")