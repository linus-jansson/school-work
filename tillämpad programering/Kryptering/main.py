import caesarCipher as cc
import transpositionCipher as tc


# ÄNDRA SÅ ATT DEN HANTERAR STORA BOKSTÄVER I CEASAR CHIPER


#def handleUpper(txt):
#    out = ""
#    # Går igenom varje bokstav / tecken i strängen och gör om den till en lite bokstav
#    for n in txt:
#        if n.isupper():
#            out += chr(ord(n) + 32)
#        else:
#            out += n
#    
#    return out

textToEncrypt = input("Skriv in ett ord eller en mening ska hanteras > ")
encryptOrDecrypt = bool(input("Ska det krypteras(1) eller avkrypteras?(0) > "))
choosenProgram = input("Hur vill du köra? \n1 - Caesar Chiper\n2 - Transposition Chiper\nq - avsluta\n>> ")

while True:
    if choosenProgram == "1":
        shiftAmount = int(input("Hur många steg ska varje bokstav skiftas med? > "))

        encryptedText = cc.encrypt(textToEncrypt, shiftAmount)

        print(f"Texten '{textToEncrypt}' krypterades till '{encryptedText}'")

        break
    elif choosenProgram == "2":
        rows = int(input("Hur många rader ska det vara i matrisen? "))

        encryptedText = tc.encrypt(textToEncrypt, rows, encryptOrDecrypt)

        print(f"Texten '{textToEncrypt}' krypterades till '{encryptedText}'")

    elif choosenProgram == "q":
        break
    else:
        print("Detta program finns inte i listan av program")
        choosenProgram = input("Hur vill du köra? \n1 - Caesar Chiper\n2 - Transposition Chiper\nq - avsluta\n>> ")
