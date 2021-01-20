###############################################
# Författare: Linus Jansson 2F
# Uppgift vänskapliga rektanglar; 
# Datum = 01/13/2021
###############################################

#I for looparna så börjar man från ett eftersom att det inte är någon vits att räkna geometri med längden 0

maxLen = int(input("Hur många vänskapliga rektanglar vill du leta efter? "))

print(f"Vänskapliga rektanglar upp till sidlängd = {maxLen}")
print("Rekt 1", "Rekt 2", sep = "\t\t")
print("bredd_1", "höjd_1", "bredd_2", "höjd_2", sep = "\t")

antal = 0

for bredd_1 in range(1, maxLen):
    for höjd_1 in range(bredd_1 + 1, maxLen):
        for bredd_2 in range(1, maxLen):
            for höjd_2 in range(bredd_2 + 1, maxLen):
                omkr_1 = 2*(bredd_1 + höjd_1)
                area_1 = bredd_1 * höjd_1

                omkr_2 = 2*(bredd_2 + höjd_2)
                area_2 = bredd_2 * höjd_2

                if area_1 == omkr_2 and area_2 == omkr_1:
                    print(bredd_1, höjd_1, bredd_2, höjd_2, sep = '\t')
                    antal += 1

print(f"Antal hittade lösningar: {antal}")