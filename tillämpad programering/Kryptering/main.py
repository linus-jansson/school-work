import caesarCipher as cc
import transpositionCipher as tc


inText = input("Skriv in ett ord eller flera för att kryptera > ")

def handleUpper(txt):
    out = ""
    # Går igenom varje bokstav / tecken i strängen och gör om den till en lite bokstav
    for n in txt:
        if n.isupper():
            out += chr(ord(n) + 32)
        else:
            out += n
    
    return out
