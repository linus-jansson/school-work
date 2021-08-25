###############################################
# Författare: Linus Jansson 2F
# Selektion extrauppgifter del 2; Uppgift 3
# Programmet frågar vilka knappar som ska vara på eller av Sen så bestämmer programemt vilka lampr som ska vara på
###############################################

# Frågar efter på eller av från användaren och sätter det i variabler
knappEtt = int(input("Ska knapp ett vara på? (0 eller 1) > "))
knappTva = int(input("Ska knapp två vara på? (0 eller 1) > "))
knappTre = int(input("Ska knapp tre vara på? (0 eller 1) > "))

# Kollar vilka lampor som ska var på
if knappEtt == 1 and knappTva == 1 and knappTre == 0:
    print("Lampa ett är tänd")
elif knappEtt == 0 and knappTva == 1 and knappTre == 1:
    print("Lampa två är tänd")
elif knappTre == 1 and knappTva == 1 and knappTre == 1:
    print("Alla lampor är tända")
else:
    print("Inga lampor är tända")