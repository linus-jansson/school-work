###############################################
# Författare: Linus Jansson 2F
# Uppgift 6
# Datum = 10/11/2020
# Räknar ut vad en elev får för betyg beroende på hur många poäng hen får
###############################################

# Tar in namn och poäng
name = input("Vad heter du? ")
points = int(input("Hur många poäng fick du på provet? "))

# Kollar poänget och mellan vilket intervall det ligger mellan
if points >= 50:
    print(f"{name} fick ett A på provet")
elif 42 < points < 50:
    print(f"{name} fick ett B på provet")
elif  34 < points < 42:
    print(f"{name} fick ett C på provet")
elif 26 < points < 34:
    print(f"{name} fick ett D på provet")
elif 19 < points < 26:
    print(f"{name} fick ett E på provet")
else:
    print(f"{name} fick ett F på provet")
    