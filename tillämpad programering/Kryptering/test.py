def skifta(karaktar, steg):
    if karaktar == 'å': # Kollar ifall det är å, ä eller ö
        return 'å'
    elif karaktar == 'ä':
        return 'ä'
    elif karaktar == 'ö':
        return 'ö'
    elif ord(karaktar) == 32: # Hanterar mellanslag
        return chr(32)
    elif karaktar.isupper(): # Hanterar stora bokstäver
        return chr((ord(karaktar) + steg - 65) % 26 + 65)
    elif karaktar.islower(): # Hanterar små bokstäver
        return chr((ord(karaktar) + steg - 97) % 26 + 97)
    else: # returnar inget ifall inget över stämmer
        return ''

def kryptera(text, steg):
    text2 = ""

    # För varje karaktär i texten så ska den skifta med antalet steg
    for karaktar in text:
        text2 += skifta(karaktar, steg)
    
    return text2

def force(text):
    for n in range(26):
        text2 = kryptera(text, -n) # Krypterar baklänges med alla steg från 1 till 26
        print(text2) # Skriver ut försöket 

    
text_att_kryptera = input("Vad för text ska du kryptera?")
steg = int(input("Hur många steg vill du skifta varje bokstav?"))

krypterad_text = kryptera(text_att_kryptera, steg)

print("Texten", text_att_kryptera, "Blev krypterad till", krypterad_text)

forcerad_text = input("Är det någon text du vill forcera? ")
force(forcerad_text)