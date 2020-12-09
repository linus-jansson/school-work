###############################################
# Författare: Linus Jansson 2F
# Uppgift 9
# Programet ber användaren mata in namn och en gruppstorlek 
# Sen delar programet upp namnen i grupper i rätt storlek
###############################################

from random import shuffle

# Funktionen som gör grupper
def make_groups(elevLista, gruppStorlek):

    # Skriver ut hur många elever det är och hur stor max gruppen får vara
    print(f"{len(elevLista)} elever")
    print(f"Gruppstorlek: {gruppStorlek}")
    print("--------------")
    
    # Shufflar om elevlistan
    shuffle(elevLista)

    # Håller koll på grupp nummret
    groupCount = 1

    # Håller koll på vilken rad som programet är på
    rad = 0
    
    # För varje elev i en lista 
    for elev in elevLista:

        # Kollar om den ska skriva ut en ny grupp genom att kolla ifall rad variabeln % gruppstorleken == 0
        if rad % gruppStorlek == 0:        
            print(f"Grupp {groupCount}")
            groupCount += 1

        # Skriver ut eleven i gruppen
        print(f"\t{elev}")
        
        rad += 1

# Frågar användaren efter namnen på eleverna och storleken på listan
elevLista = input("Skriv in eleverna som ska placeras i grupper tex \"(Linus Erik Vilhelm)\" > ").split(" ")
gruppStorlek = int(input("Hur många elever ska det vara i varje grupp? > "))

# Kommentera ut under för att testa med förgjord grupper och gruppstorlek och kommentera input raderna ovan
# elevLista = ["Kalle", "Linus", "Frans", "Emil", "Erik", "Benny", "Joakim", "Talos", "Lisa", "Jonas", "Max"]
# gruppStorlek = 3

# Kör funktionen
make_groups(elevLista, gruppStorlek)