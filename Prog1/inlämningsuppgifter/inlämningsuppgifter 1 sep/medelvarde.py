# Linus Jansson 2F
# Uppgift: Beräkna medelvärdet
# Det här programet frågar efter tre tal och sedan räknar ut medelvärdet och skriver ut det
#
tal1 = int(input("Skriv ett heltal > ")) # Första heltalet
tal2 = int(input("Skriv ett till heltal > ")) # Andra heltalet
tal3 = int(input("Skriv ett sita heltal > ")) # Tredje Heltalet

medelvarde = (tal1 + tal2 + tal3) / 3 # Räcknar ut medeltalet på de tre heltalen

print("Medelvärdet på dina tre tal är: %s" % medelvarde)