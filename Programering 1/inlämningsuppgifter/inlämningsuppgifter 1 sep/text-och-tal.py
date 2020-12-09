# Linus Jansson 2F
# Uppgift: Text och tal
# Det här programet frågar efter 2 heltal och 2 strängar
# Konkatinerar strängarna
# och adderar heltalen
# och skriver ut det
#
str1 = input("Skriv en mening eller ett ord > ") # Första strängen
str2 = input("Skriv en TILL mening eller ett ord > ") # Andra strängen

tal1 = int(input("Skriv ett heltal > ")) # Första heltalet
tal2 = int(input("Skriv ett TILL heltal > ")) # Andra Heltalet

print (str1 + str2 + str(tal1 + tal2)) # Utskrivning och concationation av strängarna samt addition av talen