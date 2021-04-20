# inText = input("Skriv in ett ord eller flera för att kryptera > ")
# shiftNum = int(input("Med hur mycket vill du förskjuta varje ord? > "))



# print(handleUpper("Hej jag heter linus")) # Testar funktionen över -> hej jag heter linus
def shift(char, shiftAmount):
    # EXAMPLE -> chr((ord(char) + shiftAmount - 97) % 26 + 97) 
    # 122(z) + 1(shiftAmount) = 123
    # 123 - 97 = 26 
    # 26 % 26 = 0 + 97 = 97 = a

    if char.isupper():
        return chr((ord(char) + shiftAmount - 65) % 26 + 65)
    elif char.islower():
        return chr((ord(char) + shiftAmount - 97) % 26 + 97)    
    elif ord(char) == 0 or ord(char) == 32:
        return chr(32)
    else:
        return ''

    
def encrypt(txt, shiftAmount):
    out = ""
    
    for n in txt:
        out += shift(n, shiftAmount)
    return out


# Genom "bruteforce" så testar den att shifta tecknerna med alla ascii nummer av tecken i alfabetet
def bruteForce(txt):
    attemps = [] # lista som håller alla försök
    
    tmp = "" # en temporär sträng

    for num in range(1, 26): 
        for n in txt:
            tmp += shift(n, num)
        attemps.append(tmp) # lägger till det forcerade försöket i listan
        tmp = "" # Tömmer den temporära strängen
    
    return attemps
