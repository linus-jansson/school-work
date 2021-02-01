import csv
import matplotlib as plt

antal_testade = []

def get_covid_data():
    with open('covid-19_data.csv', newline='') as data:
        covid_data = csv.reader(data, delimiter=';') # Delar upp datat
        lista = []
        for row in covid_data:
            # print(row)
            lista.append(row) # lägger till en array i arrayen över covid data
        return lista

def get_number_of_population():
    with open('antal_invanare.csv', newline='') as data:
        antal_invanare = csv.reader(data, delimiter=';') # Delar upp datat
        lista = []
        for row in antal_invanare:
            # print(row)
            lista.append(row) # lägger till en array i arrayen över covid data
        return lista

def get_number_of_tested():
    with open('antal_testade.csv', newline='') as data:
        antal_testade = csv.reader(data, delimiter=';') # Delar upp datat
        lista = []
        for row in antal_testade:
            # print(row)
            lista.append(row) # lägger till en array i arrayen över covid data
        return lista
        
# [0][x] beskriver namnen på de olika talen i listan tex [0][2] Skulle returnera blekinge
# [1][x] och neråt är faktiska datat
covid_data = get_covid_data()
antal_invanare = get_number_of_population()
antal_testade = get_number_of_tested()

# print(antal_invanare[0][2])

# for dag in range(2, len(covid_data) - 1):
#     # date = dag[0] # The date
#     # total = dag[1] # total amount
#     for count, value in enumerate(covid_data[dag]):
#         print(f"{value}", end=" ")    
#     print()
storsta = 0
print(covid_data[0][2])
for x in range(2, len(covid_data) - 1):
    if int(covid_data[x][2]) > int(covid_data[x - 1][2]):
        print(f"{covid_data[x][2]} > {covid_data[x - 1][2]}")
        storsta = covid_data[x][2]
    
print(storsta)
    