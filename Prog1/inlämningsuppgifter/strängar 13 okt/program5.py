###############################################
# Författare: Linus Jansson 2F
# Uppgift 5
# Kollar ifall användaren har födelsedag efter vad hen skriver in för personnummer
###############################################
from datetime import date

nmr = input("Skriv in ditt personnummer yymmddxxxx > ") # Frågar efter personens personnummer
datum = date.today().strftime("%m%d")                   # hämtar dagens datum och sätter formatet på den

if datum == nmr[2:6]:                                   # kollar ifall personen har födelsedag och grattar ifall den har det
    print("Grattis på din födelsedag")
else:
    print("Hoppas du får en bra dag!")