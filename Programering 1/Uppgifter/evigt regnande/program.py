###############################################
# Författare: Linus Jansson 2F
# Uppgift ; Evigt Regnande
# Datum = 24/11/2020
# Programet hittar sannolikheten att det skulle bli regn förevigt om sannolikheten för regn är 60 från början
#   Den tar en start sannolikhet och slumpar fram en procent 
#   Ifall procenten är mindre än eller lika med sannolikheten så regnar det och lägger till 1 på antal regn
#   Sen kör detta många gånger för att få ett bättre resultat
###############################################
from random import randint

antal_regn = 0 # Håller på på hur många gånger det har regnat
antal_sol = 0 # Håller koll på hur många gånger det är sol / inte regn [BEHÖVS INTE] 
antal_korningar = 100001 # Hur många gånger den ska köra programmet 

for korning in range(antal_korningar):
    # Sannolikheten att det regnar imorgon
    sannolikhet = 60 
    
    # Så länge sannolikhten är större än 0 och mindre än 100
    while sannolikhet > 0 and sannolikhet < 100:
        
        # denna slumpar fram en chans att det blir regn
        chans = randint(1, 100)

        # Om chansen är mindre eller lika med sannolikheten så regnar det
        if (chans <= sannolikhet):
            sannolikhet += 10
        # Annars så regnar det inte
        else:
            sannolikhet -= 10
            # antal_regn += 1

        # Om sannolikheten för regn är 100% så lägger den på regn med 1
        if sannolikhet == 100:
            antal_regn += 1
        # Om sannolikheten är 0% så regnar det inte
        elif sannolikhet == 0:
            antal_sol += 1

# Räknar ut sannolikheten 60% regn
P60 = (antal_regn / antal_korningar)

print(f"Det är {round(P60 * 100, 3)}% att det kommer bli procent för evigt ")
