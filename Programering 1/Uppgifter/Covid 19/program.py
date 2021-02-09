import csv
import matplotlib.pyplot as plt

def load_file_content_into_array(filename):
    with open(filename, newline='') as data:
        antal_testade = csv.reader(data, delimiter=';') # Delar upp datat
        lista = []
        for row in antal_testade:
            lista.append(row) # lägger till en array i arrayen över covid data
        return lista

def antal_per_hundatusen(smitta, antal_invanare): # räknar ut smnittan per 100k invånare
    return smitta // (antal_invanare / 10000)

def hamta_antal_invanare(region, antal_invanare): # hämtar antalet invånare i en region
    index = antal_invanare[0].index(region)
    return int(antal_invanare[1][index])


# TODO: ifall en region har ett högsta smittotal flera gånger ska den sparas ändå
def storst_smitta_per_region(covid_data, antal_invanare):
    # covid_data[0][x] beskriver namnen på de olika talen i listan tex [0][2] Skulle returnera blekinge
    # covid_data[1][x] och neråt är faktiska datat
    storsta_smitta = [] # används för att hålla koll på smittan i olika regioner senare
    for region in range(1, len(covid_data[0])): # Hittar största smittan för varje region
        storsta = 0
        datum = ""
        for x in range(1, len(covid_data) - 1): # hittar det största smittantalet som regionen har haft
            if int(covid_data[x][region]) >= storsta: # Kollar värdet med största och jämför vilken som är störst
                storsta = int(covid_data[x][region]) # sätt största värdet till nuvarande värdet
                datum = covid_data[x][0] # hämtar datumet som smittan var störst
                hundrak = antal_per_hundatusen(storsta, int(antal_invanare[1][region]))
                # print(f"{storsta} // ({int(antal_invanare[1][region])} / {100000}) = {hundrak}" )
        storsta_smitta.append([covid_data[0][region], datum, storsta, hundrak])
    return storsta_smitta

# Skriver ut covid data i tabell format
def print_covid_data(storsta_smitta):
    print(f"Region/Riket\t\tDatum\t\t Antal smittade per 100 000 inv.")
    print("-"*75)
    for item in storsta_smitta: # för varje objekt i listan så ska några regler anpassas på den för att snygga till utskriften
        if len(item[0]) <= 7:# om längden är mindre än 7 så ska det vara 3 tabs
            print(f"{item[0]}\t\t\t", end="")
        elif len(item[0]) >= 16: # om längden är större än 16 så ska det vara 1 tabs
            print(f"{item[0]}\t", end="")
        else: # Annars ska det bara var en tab
            print(f"{item[0]}\t\t", end="")
            
        print(f"{item[1]}\t {item[3]}")    

def visa_smitt_graf(smitt_lista = []): # Används för att visa hur smittan utvecklts på en graf
    names = ["Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov"] # en lista på namnen som ska användas i X-ledet

    for n in range(len(smitt_lista)): # plottar smittan per varje region
        region = smitt_lista[n][0]
        plt.plot(names, smitt_lista[n][1:], label=region)

    if len(smitt_lista) > 1: # om listan är tom har något gott fel och detta ska meddelas
        plt.suptitle("Smitta per månad och 100 000 inv.")
    else: 
        plt.suptitle("Smitta per månad och 100 000 inv. Ett fel har inträffat.") 
    # Allmäna graf inställningar    
    plt.grid(color='grey', linestyle='-', linewidth=0.5)
    plt.xlabel("2020")
    plt.ylabel("Smitta per månad och 100 000 inv.")
    plt.legend() # Visar vilken linje som betyder vad
    plt.show() # Visa grafen

def smitta_per_manad_per_region():
    graf_regioner = ["Hela_riket", "Norrbotten", "Dalarna", "Stockholm", "Gotland", "Vastra_gotaland", "Skane"] # Lista på regioner som den ska hämta datat ifrån
    graf_data = []
    for region in range(1, len(covid_data[0]) - 1):

        if covid_data[0][region] in plot_regioner: # den behöver bara köra på regionerna som ska plottas
            smitta_per_manad = 0
            nuvarande_region = covid_data[0][region] # hämtar namnet på den nuvarande regionen som loopen är på
            enskild_region = [nuvarande_region, 0]
            
            for x in range(1, len(covid_data) - 1):
                month = int(covid_data[x][0][5:7])
                
                try: # Testar ifall det är ett nummer om det inte är det så betyder det att det är första 
                    if month == int(covid_data[x - 1][0][5:7]): # kollar ifall månaden är samma som förra
                        if int(covid_data[x][region]) != int(covid_data[x - 1][region]): # om antalet inte har ändrats så ska den inte lägga till smittan
                            smitta_per_manad += int(covid_data[x][region]) # addera dagens smitta med totalen
                    else:
                        enskild_region.append(antal_per_hundatusen(smitta_per_manad, hamta_antal_invanare(nuvarande_region, antal_invanare))) # är månaden slut så ska den lägga till måndens antal för regionen över 100 000 invånare
                except ValueError:
                    continue
            print(nuvarande_region, enskild_region, len(enskild_region))
                
            graf_data.append(enskild_region)
    return graf_data

covid_data = load_file_content_into_array("covid-19_data.csv")
antal_invanare = load_file_content_into_array("antal_invanare.csv")
antal_testade = load_file_content_into_array("antal_testade.csv")

# print(hamta_antal_invanare("Stockholm", antal_invanare))

alternativ = input("Vill du se en graf eller en tabell över covid 19 utveckling (statistik = 1, graf = 2) > ")

while True:
    if alternativ == "1":
        print_covid_data( storst_smitta_per_region(covid_data, antal_invanare) )
        break
    elif alternativ == "2":
        data_till_graf = smitta_per_manad_per_region()
        visa_smitt_graf( data_till_graf )
        break
    else:
        break

    