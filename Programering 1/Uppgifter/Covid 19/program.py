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

def visa_smitt_graf(smitt_lista):
    names = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov"]
    for n in smitt_lista:
        plt.plot(names, n)
    plt.xlabel("2020")
    plt.ylabel("Smitta per månad och 100 000 invånare")
    plt.show()

covid_data = load_file_content_into_array("covid-19_data.csv")
antal_invanare = load_file_content_into_array("antal_invanare.csv")
antal_testade = load_file_content_into_array("antal_testade.csv")

alternativ = input("Vill du se en graf eller en tabell över covid 19 utveckling (statistik = 1, graf = 2) > ")

while True:
    if alternativ == "1":
        print_covid_data( storst_smitta_per_region(covid_data, antal_invanare) )
        break
    elif alternativ == "2":
        visa_smitt_graf( [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]])
        break
    else:
        break

    