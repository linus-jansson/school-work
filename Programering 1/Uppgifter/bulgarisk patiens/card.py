

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

