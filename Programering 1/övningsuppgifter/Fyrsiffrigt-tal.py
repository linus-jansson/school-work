# Författare: Linus Jansson 2F
# Frågar efter ett fyrsifrigt tal och sen skriver ett tal åt gången
#

tal = input("Ge mig ett fyrasiffrigt tal > ") # Fråga efter ett tal (String)

if (1000 < int(tal) < 9999 ): # Convertera talet till int och kolla ifall det är en int och ifalld et är ett 4 siffrigt tal
    for n in tal: # Ta varje index i en string och printa varje "nummer"
        print(n)
else: 
    print("Det där är inte ett fyrsiffrigt tal eller så är det en sträng") # Om det inte är ett fyrsiffrigt tal så ska den skriva ut att det inte är det