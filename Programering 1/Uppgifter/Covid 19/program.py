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

def hamta_antal_invanare(region = "Hela_riket", antal_invanare = [[]]): # hämtar antalet invånare i en region
    index = antal_invanare[0].index(region)
    # print(f"{region} ligger på index {index} och har {int(antal_invanare[1][index])} antal invanare")
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

def visa_graf(smitt_lista, title, ytitle): # Används för att visa hur smittan utvecklts på en graf
    names = ["Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov"] # en lista på namnen som ska användas i X-ledet
    
    if any(isinstance(x, list) for x in smitt_lista): # Kolla ifall listan har några innre listor
        for n in range(len(smitt_lista)): # plottar smittan per varje region
            region = smitt_lista[n][0]
            plt.plot(names, smitt_lista[n][1:], label=region)
    else:
        region = smitt_lista[0]
        plt.plot(names, smitt_lista[1:], label=region)

    if len(smitt_lista) > 1: # om listan är tom har något gott fel och detta ska meddelas
        plt.suptitle(title)
    else: 
        plt.suptitle(f"{title} Ett fel har inträffat.") 
    # Allmäna graf inställningar    
    plt.grid(color='grey', linestyle='-', linewidth=0.5)
    plt.xlabel("2020")
    plt.ylabel(ytitle)
    plt.legend() # Visar vilken linje som betyder vad
    plt.show() # Visa grafen

def smitta_per_manad_per_region():
    graf_regioner = ["Hela_riket", "Norrbotten", "Dalarna", "Stockholm", "Gotland", "Vastra_gotaland", "Skane"] # Lista på regioner som den ska hämta datat ifrån
    graf_data = []
    for region in range(1, len(covid_data[0])):

        if covid_data[0][region] in graf_regioner: # den behöver bara köra på regionerna som finns med i graf_regioner listan
            smitta_per_manad = 0
            nuvarande_region = covid_data[0][region] # hämtar namnet på den nuvarande regionen som loopen är på
            enskild_region = [nuvarande_region, 0]
            
            for x in range(1, len(covid_data)):
                month = int(covid_data[x][0][5:7])
                
                try: # Testar ifall det är ett nummer om det inte är det så betyder det att det är första 
                    if month == int(covid_data[x - 1][0][5:7]): # kollar ifall månaden är samma som förra
                        if int(covid_data[x][region]) != int(covid_data[x - 1][region]): # om antalet inte har ändrats så ska den inte lägga till smittan
                            smitta_per_manad += int(covid_data[x][region]) # addera dagens smitta med totalen
                    else:
                        enskild_region.append(antal_per_hundatusen(smitta_per_manad, hamta_antal_invanare(nuvarande_region, antal_invanare)) ) # är månaden slut så ska den lägga till måndens antal för regionen över 100 000 invånare
                        smitta_per_manad = 0 
                except ValueError:
                    continue
                
            graf_data.append(enskild_region)
    return graf_data

def smittstyrka(covid_data, antal_testade, antal_invanare):
    antal_smittade_per_manad = []
    smitta_per_manad = 0
    landets_invanare = hamta_antal_invanare("Hela_riket", antal_invanare)
    for dag in range(1, len(covid_data)):
        month = int(covid_data[dag][0][5:7])
        
        try: # Testar ifall det är ett nummer om det inte är det så betyder det att det är första 
            dagens_smitta = int(covid_data[dag][1])

            if month == int(covid_data[dag - 1][0][5:7]): # kollar ifall månaden är samma som förra
                if int(covid_data[dag][1]) != int(covid_data[dag - 1][1]): # om antalet inte har ändrats så ska den inte lägga till smittan
                    smitta_per_manad += dagens_smitta # addera dagens smitta med totalen
            else:
                antal_smittade_per_manad.append(antal_per_hundatusen(smitta_per_manad, landets_invanare)) # är månaden slut så ska den lägga till måndens antal för regionen över 100 000 invånare
                smitta_per_manad = 0

        except ValueError:
            continue

    smittstyrka_per_manad = ["Antal smittade per testade", 0]
    
    for month in range(len(antal_smittade_per_manad)):
        
        testade_per_hundratusen = antal_per_hundatusen(int(antal_testade[1][month]), landets_invanare)
        smittade_per_hundatusen = antal_smittade_per_manad[month]
        
        if testade_per_hundratusen > 0:
            smittstyrka_per_manad.append(round(smittade_per_hundatusen / testade_per_hundratusen, 3))
        else:
            smittstyrka_per_manad.append(0)

    return smittstyrka_per_manad


covid_data = load_file_content_into_array("covid-19_data.csv")
antal_invanare = load_file_content_into_array("antal_invanare.csv")
antal_testade = load_file_content_into_array("antal_testade.csv")

alternativ = input("Välj mellan följande alternativ\n====\nTabell datumet som smittan var störst per 100k inv. = 1\nGraf över smittspridningen per region per 100k inv. per månad  = 2\nAntal smittade per testade per 100k inv. = 3\n> ")

while True:
    smitta = smitta_per_manad_per_region()
    styrka = smittstyrka(covid_data, antal_testade, antal_invanare)

    if alternativ == "1":
        print_covid_data( storst_smitta_per_region(covid_data, antal_invanare) )
        break
    elif alternativ == "2":
        visa_graf( smitta, "Antal smittade per månad och 100.000 inv.", "Antal per månad och 100.000 inv." )
        break
    elif alternativ == "3":
        visa_graf(styrka, "Antal smittade per testade per 100.000 inv.", "Antal smitade per testade")
        break        
    else:
        break

    