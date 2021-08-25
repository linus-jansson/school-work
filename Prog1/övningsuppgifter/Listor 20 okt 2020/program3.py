###############################################
# Författare: Linus Jansson 2F
# Uppgift 3
# Kollar kontantkort är billigast med hjälp av rpartiotion av strängar
################################################

namn = []
pris = []

while True:
    s = input("Namn och pris för ett kort: ")

    if s == "":
        break

    s = s.rpartition(" ")

    namn.append(s[0:1])
    pris.append(float(s[-1]))

m = min(pris)
k = pris.index(m)

print(namn[k][0] + " är billigast")
print(f"Kostnad: {m:1.2f} kr/månad")