###############################################
# Författare: Linus Jansson 2F
# Uppgift 1 
# 
# A: Om man ger andra startvärlden till variablen k
#    - "listans" värde blir annourlunda. tex [ 2 4 ] istället för [   0   2   4 ] om jag börjar på 2 istället för 0
# B: Om man drar in den sista raden så att den hamnar på samma rad ovan
#    -  Den skriver ett "]"" i slutet på varje rad och gör en ny rad istället för att allt hamnar på samma rad
# C: Vad händer om du istället drar ut näst sista raden så att den hamnar under ordet while
#    - Den skriver ut k oändligt många gånger
###############################################

print("[", end="")
k = 2

while k < 6:
    print(f"{k:2}", end="")
    k += 2

print(" ]")