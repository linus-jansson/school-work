# inText = input("Skriv in ett ord eller flera för att kryptera > ")
# shiftNum = int(input("Med hur mycket vill du förskjuta varje ord? > "))



# print(handleUpper("Hej jag heter linus")) # Testar funktionen över -> hej jag heter linus

def shift(char, shiftAmount):
    # EXAMPLE
    # 122(z) + 1(shiftAmount) = 123
    # 123 - 97 = 26 
    # 26 % 26 = 0 + 97 = 97 = a

    return chr((ord(char) + shiftAmount - 97) % 26 + 97)
    
def encrypt(txt, shiftAmount):
    out = ""
    
    for n in txt:
        if not (ord(n) == 0 or ord(n) == 32):
            out += shift(n, shiftAmount)
        else:
            out += chr(32)
    return out


# Genom "bruteforce" så testar den att shifta tecknerna med alla ascii nummer av tecken i alfabetet
def bruteForce(txt):
    attemps = [] # lista som håller alla försök
    
    tmp = "" # en temporär sträng

    for num in range(1, 26): 
        for n in txt:
            if not (ord(n) == 0 or ord(n) == 32):
                tmp += shift(n, num)
            else:
                tmp += chr(32)
        attemps.append(tmp) # lägger till det forcerade försöket i listan
        tmp = "" # Tömmer den temporära strängen
    
    return attemps

# inText = handleUpper(inText)

# # print(encrypt(handleUpper(inText), shiftNum))
# lista = bruteForce(encrypt(inText, shiftNum))

# for n in lista:
#     print(n)

