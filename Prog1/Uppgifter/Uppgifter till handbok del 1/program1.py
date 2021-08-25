###############################################
# Författare: Linus Jansson 2F
# Uppgift 1; 
# Datum = 01/13/2021
# 
# Uppgift:
# 1) Det finns ett till samband som liknar detta. Kan du hitta det genom att pröva att multiplicera med andra tal än 4?
#
# 2) Det finns liknande samband för 5-siffriga tal. Kan du hitta dem?
#
###############################################
for n in range(2, 10): # 3) Skriv en ”yttre for-loop” som kör testet flera gånger för olika värden på talet 4:
    # Fyrsiffriga tal
    for tal in range(1000, 10000):

        talReversed = int( str(tal)[::-1] )

        if tal * n == talReversed:
            print(f"{tal} * {n} = {talReversed}")

for n in range(2, 10): # 3) Skriv en ”yttre for-loop” som kör testet flera gånger för olika värden på talet 4:    
    # Femsiffriga tal
    for tal in range(10000, 100000):
        
        talReversed = int(str(tal)[::-1])

        if tal * n == talReversed:
            print(f"{tal} * {n} = {talReversed}")