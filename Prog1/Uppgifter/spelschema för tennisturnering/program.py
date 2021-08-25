###############################################
# Författare: Linus Jansson 2F
# Uppgift ; Spelschema för tenninsturnering
# Datum = 25/11/2020
# Programmet hittar skapar ett spelschema för en tennisturnering med hjälp av seeding
###############################################
import math

def decimalToBinary(n):
    # Gör om talet till binärt och tar bort prefixen
    # Den formateras också så att tex 1 i decimal är "001" och inte "1".
    # Detta behövs senare när man spegelvänder de binaära talen
    return str( format(n, '#05b') ).replace("0b", "")


def binaryToDecimal(n):
    # Gör om talet från binart till decimal
    return int(n, 2)


def produceSkillBasedSchedule(spelarLista):
    # En lista som kommer hålla spelarnas spelschema;
    # Det är i formatet [ ["Spelare 1", "spelare 2"], ["spelare 1"] vs ["spelare 2"] ] (Nested List / en lista med pairs)
    schema = []

    # Anpassar listan så lägden är en potens av 2, så att alla kan spela med varandra
    x = math.ceil( math.log( len(spelarLista) ) / math.log(2) )
    
    while len(spelarLista) < 2**x:
        spelarLista.append("-")  

    # Läser in spelarplatsernas index i binärt både normalt och omvänt 
    # För varje nummer i längden på listan så gör man om det till binärt och lägger det i listIndexesBinary
    listIndexesBinary = [ decimalToBinary(i) for i in range(len(spelarLista)) ]
    # print(listIndexesBinary)

    # Ta varje binärt tal i listan och spegelvänder det så att tex 001 blir 100
    listIndexsesBinaryReverse = [ item[::-1] for item in listIndexesBinary ] 
    # print(listIndexsesBinaryReverse)


    # Producerar schemat
    for count in range( len(spelarLista) ):

        # Lägger till ett pair i listan [["spelare1", "Spelare 2"]]
        # Den lägger också till i schemat spelaren från spelarlistan med den vanliga platsen 
        #   Den använder även funktionen binaryToDecimal() eftersom eftersom den vill hitta positionen i spelarlistan i decimaltal från spelarplatser[count]
        spelare1 = spelarLista[ binaryToDecimal( listIndexesBinary[count] )]
        spelare2 = spelarLista[ binaryToDecimal( listIndexsesBinaryReverse[count] )] # Spelaren med den spegelvända positionen i binärt jämfört med spelare 1

        schema.append([spelare1, spelare2])

    # Returnerar schemat från functionen   
    return schema

# Läser in spelarListan och gör det till en lista vi kallar för spelarLista
fileInput = open("input.txt", "r", encoding="utf8")
inputLista = fileInput.readlines()

# Tar bort alla \n (LineBreaks) namnlistan
inputLista = [ n.replace("\n", "") for n in inputLista ]

schema = produceSkillBasedSchedule(inputLista)

# Skriver ut listan med spelare
print(f"Lista på spelare: {inputLista}")
print(f"======== SCHEMA ========")
for spelare in schema:
    print(f"{spelare[0]:<10} vs {spelare[1]:>10}")
print(f"========================")

