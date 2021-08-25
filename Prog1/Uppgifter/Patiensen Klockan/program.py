###############################################
# Författare: Linus Jansson 2F
# Uppgift ; Patiensen Klockan
# Datum = 01/12/2020
# Programmet löser patiensen klockan och skriver ut resultatet på i konsolen
###############################################
import random

# räknar ut procent
def percentage(part, whole):
    return round( float(part) / float(whole) * 100, 5)


cardTypes = ["K", "S", "R", "H" ] # Klöver; Spader; Ruter; Hjärter
innerCardTypes = [ "A",  "2",  "3",  "4", "5",  "6",  "7",  "8", "9",  "T", "J", "D", "K"] # A: Ess, J: knekt


# Genererar kortleken
def generateDeckOfCards():

    # En lista som representerar kortleken; börjar med två jokrar
    deckOfCards = []

    # Generera en kortlek med 52 kort
    for typ in range(4): # 4 korttyper
        for val in range(13): # 13 typer av kort i korttypen
            card = cardTypes[typ] + innerCardTypes[val] # Kort = typen + värdet
            deckOfCards.append(card) # lägger till kortleken

    return deckOfCards

def isCorrectPos(card, pos):
    # Kollar ifall index av kortet[1] är samma som positionen
    if innerCardTypes.index( card[1:].upper() ) == pos:
        return True
    return False

# Hittar vilken lista av listor som är störst
def findLongest(INPUTLISTA):
    return max(len(elem) for elem in INPUTLISTA)

# Skriver ut patiensen i tabellformat
def printOut(INPUTLISTA):

        # Hittar den hur lång den längsta listan är i listan
        maxlen = findLongest(INPUTLISTA)

        # Skriver ut tal mellan 1-13 så det blir lättare att läsa
        for n in range(1, 14):
            print(f"{str(n):5}", end="")
        print()

        # För varje plats i en kolumn för maxlängden på listorna
        for y in range(maxlen):
            # Loopa över varje kolumn
            for column in INPUTLISTA:
                # Om lägnden på en kolumn är mindre än y så ska den skriva ut ett blanksteg
                if len(column) <= y:
                    print(f"{' ':5}", end="")
                else:
                    print(f"{column[y]:5}", end="")

            # Skriv ut ett radbyte efter varje rad
            print("\n"*0)

def realPatiensenClock(deckOfCards):

    
    # Du börjar med en kortlek med 52 kort; oplaceradekort ska innehålla hela kortleken
    #
    # Lägg ut första raden och kolla ifall kortet du lägger ut är rätt kort
    #   Om det är rätt kort så ska kolumnen låsas och så ska den tas bort från oplaceradekrot
    #   Annars lägger du bara ut kortet och fortsätter och så ska den tas bort från oplaceradekort
    #
    # Om det ligger kort innan det rätta kortet läggs ut så ska de tidigare korten läggas tillbaka i en lista med oplacerade kort
    #
    # K2 R9 S5 K6 KD RT K3 KK HK HD R2 S6 RK
    # SD H9 RJ ST H3 SK R7 HT K8 S2 H6 R8
    # SA HA R3 H7 HJ H4 S3 R4 K7 K9 RD
    #    K5    S4 S8 S7    S9 SJ H5 H2
    #    H8    RA KA       K4 R5 R6 KT 
    #    KJ
    # I detta exempel så skulle Spader dam hamna sist i högen av oplacerade kort och knekt 2 hamnar näst sist
    
    # När kort placeras ska första platsen alltid kollas; 
    # därav behövs inget index som ökar eftersom du bara tar första kortet ifrån oplaceradekort listan och tar bort det från listan när det placeras
    #

    # Gör detta tills alla kort är klarplacerade?
    # Placera ett kort
    #   Om platsen == 13: gör radbyte
    #   Om rättplaceradekort == 13: avsluta loppen
    #   
    #   if (är kortet på rätt plats?)
    #       if (Finns det några kort innan)
    #           Ta bort dom från placerade kort och lägg till kortet som är rätt till placerade kort listan
    #           
    #   else:
    #       Ta bort dom från listan av oplacerade kort
    
    # Blanda om listan med kort
    random.shuffle(deckOfCards)

    unPlacedCards = deckOfCards # En lista av kort som inte är palcerade

    placedCards = [[] for n in range(13)] # Håller koll på korten som placerats också denna lista som skickas ut till användaren sen
    column = [ False for n in range(13) ] # håller koll på ifall kolumnen är klar

    rowPos = 0 # Vilken position programmet är på
    row = 0 # Vilken rad programmet är på

    correctPlacements = 0 # Hur många gånger ett kort har placerats på rätt plats
    isSolved = False # Ifall programmet är löst
    
    while True:
        # Om längden på listan av oplacerade kort är mindre än 1 så är det slut på kort
        if len(unPlacedCards) < 1:
            break

        # Hämtar kortet högst upp i kortleken
        i = unPlacedCards[0]
        
        # Ifall totala placerade kort är 13 så har patiensen gått ut
        if correctPlacements == 13:
            isSolved = True
            break
        elif rowPos == 13:
            row += 1
            rowPos = 0
        
        # kollar ifall kolumnen är låst
        if column[rowPos]:
            rowPos += 1
        else:

            
            # Kollar ifall kortet är på rätt plats
            if (isCorrectPos(i, rowPos)):

                # Lägger till det rättplacerade kortet
                placedCards[rowPos].append(i.lower())

                
                printOut(placedCards)

                # Går igenom kolumnen och kollar ifall det finns några andra kort 
                for n in placedCards[rowPos]:
                    print(placedCards[rowPos])
                    if n != i:
                        # Tar bort korten från den placerade listan och lägger tillbaka dom i kortleken sist
                        unPlacedCards.append(n)
                        placedCards[rowPos].pop(placedCards[rowPos].index(n))


                # Låser kolumnen
                column[rowPos] = True
                correctPlacements += 1

            
            else:
                placedCards[rowPos].append(i) # Placera bara kortet och 
            
            unPlacedCards.pop(0) # ta bort det från placerade kort
            rowPos += 1
        
    return [placedCards, correctPlacements, isSolved]
  

# lägger Patiensen
def patiensenClock(deckOfCards):
    # Blanda om listan med kort
    random.shuffle(deckOfCards)

    unPlacedCards = deckOfCards # En lista av kort som inte är palcerade

    placedCards = [[] for n in range(13)] #
    column = [ False for n in range(13) ] # håller koll på ifall kolumnen är klar

    # Ifall användaren vill köra programet flera gånger
    # for a in range(numOfTimes):
    correctPlacements = 0
    rowPos = 0
    row = 0
    unPlacedCards = deckOfCards # En lista av kort som inte är palcerade
    correctPlacements = 0 # Hur många gånger ett kort har placerats på rätt plats
    isSolved = False # Ifall programmet är löst'
    
    while True:
        # Om längden på listan av oplacerade kort är mindre än 1 så är det slut på kort
        if len(unPlacedCards) < 1:
            break
        
        # hämtar ett kortet från kortleken
        i = deckOfCards[0]
        
        # Ifall totala placerade kort är 13 så har patiensen gått ut
        if correctPlacements == 13:
            isSolved = True
            break
        elif rowPos == 13:
            row += 1
            rowPos = 0
        
        # kollar ifall kolumnen är låst
        if column[rowPos]:
            rowPos += 1

        else:
            # Kollar ifall kortet är på rätt plats
            if (isCorrectPos(i, rowPos)):
                placedCards[rowPos].append( i.lower() )

                column[rowPos] = True # Låser kolumnen

                correctPlacements += 1  # Lägger till 1 till rättplacerade kortet
                
            else:
                # Placera bara kortet och ta bort det från placerade kort
                placedCards[rowPos].append(i)

            unPlacedCards.pop(0)
            rowPos += 1

    return [placedCards, correctPlacements, isSolved]

inp = input("Hej och välkommen till Patiensen klockan programmet, vilket program vill du köra?\n - Se utlägg av en patiens (a)\n - Se statistik på valt antal patienser hur ofta patiensen går ut (b)\n - avsluta (q)\n > ")

# En RUN loop
while True:
    if inp == 'a':
        
        programType = input("Vilket program vill du köra? Patiensklockan eller riktiga patiensklockan? (a eller b) > ")

        # Kör funktionen som lägger patiensen lägger resultatet i variabeln
        if programType == 'a':
            output = patiensenClock(generateDeckOfCards())
            
        elif programType == 'b':
            output = realPatiensenClock(generateDeckOfCards())

        else:
            continue

        listOfPlacedCards = output[0]
        numOfCorrectPlacements = output[1]


        printOut(listOfPlacedCards)

        # Skriver ut resultat till användaren efter patiensen
        if numOfCorrectPlacements < 13:
            print(f"\nKortleken är slut och lyckades få ut {numOfCorrectPlacements} kort rätt, Patiensen gick inte ut")

        else:
            print(f"\nLyckades få ut {numOfCorrectPlacements} kort rätt, Patiensen gick ut!")

        break

    elif inp == 'b':
        # Error handling ifall användaren inte skriver in ett heltal
        # Försöker ta in numOfRuns - om det inte går så skriver den ut err och frågar användaren igen pga continue
        try:
            numOfRuns = int(input("Hur många gånger vill du lägga patiensen? > "))
        except Exception as err:
            print(err)
            continue

        # variabler som börjar på basic betyder den simpla versionen av patisensen och real betyder den riktiga versionen av patiensen klockan
        # Håller hur många kort som placerades rätt och hur många gånger patiensen löstes
        basicTotalResult = 0
        basicNumOfSolves = 0

        realTotalResult = 0
        realNumOfSolves = 0


        for n in range(numOfRuns + 1):
            
            # Definerar de olika outputsen från vad funktionerna returnerar
            basicOutput = patiensenClock(generateDeckOfCards())
            realOutput = realPatiensenClock(generateDeckOfCards())
            
            basicTotalResult += basicOutput[1]
            realTotalResult += realOutput[1]

            
            # Om patiensen gick ut så ska den addera 1 till numOfSolves
            if (basicOutput[2]):
                basicNumOfSolves += 1

            # Om patiensen gick ut så ska den addera 1 till numOfSolves
            if (realOutput[2]):
                realNumOfSolves += 1

        # Det man bör se av detta är att den riktiga versionen går ut enormt mycket oftare än den simpla versionen
        print(f"Patiensen med den simpla versionen gick ut {basicNumOfSolves} gånger på {numOfRuns} körningar ({percentage(basicNumOfSolves, numOfRuns)}%) {basicTotalResult} kort placerades rätt!")
        print(f"Patiensen med den riktiga versionen gick ut {realNumOfSolves} gånger på {numOfRuns} körningar ({percentage(realNumOfSolves, numOfRuns)}%) {realTotalResult} kort placerades rätt!")

        break

    elif inp == 'q':
        break

    else:
        print("Valet finns inte med på listan")
        inp = input("Vilket program vill du köra?\n - Se utlägg av en patiens (a)\n - Se statistik på valt antal patienser (b)\n - sluta(q)\n > ")
