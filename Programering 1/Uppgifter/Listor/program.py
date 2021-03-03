###############################################
# Författare: Linus Jansson 2F
# Funktioner; Uppgift 1
# Datum = 03/03/2021
# Skriver ut slumpgenererade temperaturer i form av en tabell med olika klockslag över ett vist antal dagar
###############################################
import random as r

D = int(input("Hur många dagar ska vi genera temperaturer? > "))
A = float(input("Ge en minigräns > "))
B = float(input("Ge en maxgräns > "))

# Har bara reda på de tidpunkter som den ska loopa igenom senare 
# man kan även ändra listan med klockslag för att få flera klockslag på utskriften
tider = ["07:00", "12:00", "19:00", "02:00"]

# genererar en lista med inre listor med klockslag
def generate(D, A, B, klockslag):
    temperatures = []
    for i in range(D):
        dag = []
        for n in range(len(klockslag)):
            dag.append(r.randint(A*10, B*10) / 10)

        temperatures.append(dag)
    return temperatures

# Visar temperaturerna i en tabell med dagar och tidpunkter
def display(temps, klockslag):
    print("Tid\t", end="")

    # skriver ut antalet dagar beroende på hur många listor som finns i temp listan tex dag1,dag2,dag 3 om det finns 3 listor
    for dag in range(len(temps)):
        print(f"dag {dag + 1}\t", end="")
    print()

    # Skriver ut de olika temperaturerna per klockslag
    for tid in range(len(klockslag)):
        print(f"{klockslag[tid]}\t", end="")
        dag = 0
        for n in temps:
            print(f"{temps[dag][tid]}\t", end="") # hittar temperaturen i den tidpunkten
            dag += 1

        print()

def warmest_day(temps):
    mean = []
    for n in range(len(temps)):
        m = 0
        for x in temps[n]:
            m += x
        # lägger till dagens temperaturer som medelvärde och rundar av den i listan av medlvärden
        mean.append( round((m / len(temps[n])), 3) ) 
    # returnerar en lista med vilken dag som den högsta temperaturen va på 
    return [mean.index(max(mean)), max(mean)]

# Hämtar temperaturerna från en specefik dag
def get_day(temps, dag):
    if len(temps) >= dag:
        return temps[dag - 1] # i listan så kommer dag 1 vara index 0 därför tar vi bort 1
    else:
        return None

# Kör funktionen display som med genererade temperaturer
t = generate(D,A,B, tider)
print(t)
display(t, tider)

# print(get_day(t, 1))

print(warmest_day(t))