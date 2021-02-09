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

def print_covid_data(storsta_smitta):
    print(f"Region/Riket\t\tDatum\t\t Antal smittade per 100 000 inv.")
    print("-"*75)
    for item in storsta_smitta:
        if len(item[0]) <= 7:
            print(f"{item[0]}\t\t\t", end="")
        elif len(item[0]) >= 16:
            print(f"{item[0]}\t", end="")
        else:
            print(f"{item[0]}\t\t", end="")
            
        print(f"{item[1]}\t {item[3]}")    

def visa_smitt_graf(smitt_lista = []): # Används för att visa hur smittan utvecklts på en graf
    names = ["Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov"]
    for n in range(2, len(smitt_lista) - 1):
        print(smitt_lista[n])

    for n in smitt_lista: # plottar smittan per varje region
        
        print(n, len(n))
        plt.plot(names, n, label="smitt_lista[smitt_lista.index(n)][0]")

    if len(smitt_lista) > 1:
        plt.suptitle("Smitta per månad och 100 000 inv.")
    else: # om listan är tom har något gott fel och detta ska meddelas
        plt.suptitle("Smitta per månad och 100 000 inv. Ett fel har inträffat.") 

    plt.xlabel("2020")
    plt.ylabel("Smitta per månad och 100 000 inv.")
    plt.legend()
    plt.show()



plot_regioner = ["Hela_riket", "Norrbotten", "Dalarna", "Stockholm", "Gotland", "Vastra_gotaland", "Skane"]
covid_data = load_file_content_into_array("covid-19_data.csv")
antal_invanare = load_file_content_into_array("antal_invanare.csv")
antal_testade = load_file_content_into_array("antal_testade.csv")

alternativ = input("Vill du se en graf eller en tabell över covid 19 utveckling (statistik = 1, graf = 2) > ")

while True:
    if alternativ == "1":
        print_covid_data( storst_smitta_per_region(covid_data, antal_invanare) )
        break
    elif alternativ == "2":
        graf_att_printa = [] # 8=====B
        for region in range(1, len(covid_data[0]) - 1):

            if covid_data[0][region] in plot_regioner: # den behöver bara köra på regionerna som ska plottas
                smitta_per_manad = 0
                nuvarande_region = covid_data[0][region]
                enskild_region = [0]
                
                for x in range(1, len(covid_data) - 1):
                    month = int(covid_data[x][0][5:7])
                    # kolla ifall månaden är samma som förra; är den det så ska den addera förra med den som är nu
                    # Kan orsaka fel: på första x - 1 så kommer den att hämta "Statistikdatum" vilket inte går att göra om till en int
                    try:
                        if month == int(covid_data[x - 1][0][5:7]):
                            if int(covid_data[x][region]) != int(covid_data[x - 1][region]):
                                smitta_per_manad += int(covid_data[x][region])
                        else:
                            enskild_region.append(smitta_per_manad)
                    except ValueError:
                        continue
                print(nuvarande_region, enskild_region, len(enskild_region))
                    
                graf_att_printa.append(enskild_region)

        # visa_smitt_graf()
        visa_smitt_graf( graf_att_printa)
        break
    else:
        break

    