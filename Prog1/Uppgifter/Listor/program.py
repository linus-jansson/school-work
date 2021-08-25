###############################################
# Författare: Linus Jansson 2F
# Funktioner och listor; Uppgift 1
# Datum = 03/03/2021
# Skriver ut slumpgenererade temperaturer i form av en tabell med olika klockslag över ett vist antal dagar
# Skriver även ut temperaturenas största värde på en dag och mediantemperaturen
###############################################
import random

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
            dag.append(random.randint(A*10, B*10) / 10)

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

# Hittar den varmaste dagen av lista av temperaturer
def warmest_day(temps):
    mean = []
    for n in range(len(temps)):
        m = 0
        for x in temps[n]:
            m += x
        # lägger till dagens temperaturer som medelvärde och rundar av den i listan av medlvärden
        mean.append( round((m / len(temps[n])), 3) )
    # returnerar en lista med vilken dag som den högsta temperaturen va på 
    dag = mean.index(max(mean)) + 1 # Adderar 1 annars kommer den att returnera index och inte vilken dag (get_day tar hand om index)
    value = max(mean)
    return [dag, value]

# Hämtar temperaturerna från en specefik dag
def get_day(temps, dag):
    if len(temps) >= dag:
        return temps[dag - 1] # i listan så kommer dag 1 vara index 0 därför tar vi bort 1
    else:
        return None

# Skriver ut den varmaste dagen
def display_warmest(tider, temps):

    warmest = warmest_day(temps)
    
    print()
    print(f"Den varmaste dagen va dag {warmest[0]}, medelvärdet {warmest[1]}")

    print("Kl", end="\t")
    for t in tider:
        print(f"{t}\t", end="")
    print()

    
    for c in get_day(temps, warmest[0]):
        print(f"\t{c}C", end="")

# Hittar mittenvärdet på en lista
def find_middle(input_list):
    middle = float(len(input_list)) / 2 # hittar mitten index på listan

    if middle % 2 != 0: # kollar ifall listan är udda eller inte
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[(int(middle - 1))])

# returnerar medianen på listan av temperaturer
def get_median_temp(temps):
    print()
    tmp = []
    for day in temps:
        for temp in day:
            tmp.append(temp)

    tmp.sort()
    median = find_middle(tmp)
    x = 0
    if len(median) > 1: # om listan är udda så ska den hitta medelvärdet på de två medianerna och returnera det som median
        for n in median:
            x += n
        return x / len(median)
    else:
        return median


def display_median(median):
    print(f"Median temperaturen: {median}")


# Genererar en lista med temperaturer
t = generate(D,A,B, tider)

# Kör display funktionerna
display(t, tider)
display_median(get_median_temp(t))
display_warmest(tider, t)
