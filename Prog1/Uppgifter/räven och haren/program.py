###############################################
# Författare: Linus Jansson 2F
# Uppgift ; Räven och haren
# Datum = 17/11/2020
# Programet tar reda på hur många sekunder det skulle ta för en räv att få tag i en hare
#   Programet löser ut de två komposanter från rävens hastighet som är hypotenusan
#   Sedan lägger man till rävens fart till x och y komposanten, för att uppnå att den springer rakt mot haren
###############################################

import math
import matplotlib.pyplot as plt

# Harens fart och rävens fart i m/s
hareFart = 35.0/3.6 # m/s
ravFart = 50.0/3.6 # m/s

# Harens och Rävens start positioner
harensX = 60.0
harensY = 0.0

ravensX = 0.0
ravensY = 20.0

# Börjar räkna från 0 sekunder
tid = 0
# Litet tidssteg för att öka precision
tidssteg = 0.001

# Delar upp cordinater i 4 listor för att kunna plotta dom
# INTE RELEVANT FÖR LÖSNINGEN
harenXlist = [harensX]
harenYlist = [harensY]

ravenXlist = [ravensX]
ravenYlist = [ravensY]

# Sätter hypotenusan till något stort så att den inte hoppar ut while loopen direkt
hypotenusan = 10

# Så länge avståndet mellan haren och räven är större än 0.5 meter
while hypotenusan >= 0.5:

    # Hittar skillnaden mellan räven och harens x och y positioner
    deltaX = harensX - ravensX
    deltaY = harensY - ravensY

    # Hittar hypotenusan mellan rävens nuvarande position och harens nuvarande position
    hypotenusan = math.sqrt( deltaX**2 + deltaY ** 2 )

    # Räknar ut cosinus och sinus av vinkeln
    #   cos(alfa) = ( Närligande / Hypotenusan )
    #   sin(alfa) = ( Motstående / Hypotenusan )
    cos_alfa = deltaX / hypotenusan
    sin_alfa = deltaY / hypotenusan

    # Öka harens y kordinat med harens fart
    harensY += hareFart * tidssteg

    # Öka rövens y och x efter komposanterna
    ravensX += cos_alfa * ravFart * tidssteg
    ravensY += sin_alfa * ravFart * tidssteg

    # Öka tiden med tidssteg
    tid += tidssteg

    # lägger till i listorna för att sen kunna plotta ut kordinaterna
    ravenXlist.append(ravensX)
    ravenYlist.append(ravensY)

    harenXlist.append(harensX)
    harenYlist.append(harensY)


print(f"Det tog {round(tid, 3)} sekunder att komma ikapp haren")

# Visualisering av rörelse av haren och räven
#############################################
ax = plt.figure().add_subplot(1, 1, 1)
ax.grid(linestyle='-', linewidth=1) # Lägger till rutnät på grafen
plt.plot(harenXlist, harenYlist, linestyle='solid', color='red', label='hare') # Plottning av hur Haren rör sig
plt.plot(ravenXlist, ravenYlist, linestyle='dashed', color='blue', label='räv') # Plottning av hur Räven rör sig
plt.savefig('Result.png')
plt.show()
#############################################

