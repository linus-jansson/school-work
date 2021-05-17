import time
import random
import math


def shift(char, shiftAmount):
    # EXAMPLE -> chr((ord(char) + shiftAmount - 97) % 26 + 97) 
    # 122(z) + 1(shiftAmount) = 123
    # 123 - 97 = 26 
    # 26 % 26 = 0 + 97 = 97 = a

    # Hanterar icke ascii tecken
    if char == 'å':
        return 'å'
    elif char == 'ä':
        return 'ä'
    elif char == 'ö':
        return 'ö'
    else:
         # Hanterar gemener och versaler
        if char.isupper():
            return chr((ord(char) + shiftAmount - 65) % 26 + 65)
        elif char.islower():
            return chr((ord(char) + shiftAmount - 97) % 26 + 97)    
        elif ord(char) == 0 or ord(char) == 32: # hanterar mellanslag
            return chr(32)
        else:
            return ''

    
def caesarEncrypt(txt, shiftAmount):
    out = ""
    
    for n in txt:
        out += shift(n, shiftAmount)
    return out


# Genom "bruteforce" så testar den att shifta tecknerna med alla ascii nummer av tecken i alfabetet
def caesarBruteForce(txt):
    attemps = [] # lista som håller alla försök
    
    tmp = "" # en temporär sträng

    for num in range(1, 26): 
        for n in txt:
            tmp += shift(n, num)
        attemps.append(tmp) # lägger till det forcerade försöket i listan
        tmp = "" # Tömmer den temporära strängen
    
    return attemps


def fillArray(txt, arr):
    currentChar = 0
    
    rCount = 0
    cCount = 0
    
    # För varje karaktär, fyll ut listan
    while currentChar <= len(txt) - 1:
        # Om raden är slut gå till nästa rad kolumn 0
        if len(arr[0]) - 1 < cCount:
            rCount += 1
            cCount = 0
        
        arr[rCount][cCount] = txt[currentChar]
        cCount += 1
        currentChar += 1
    
    return arr


def matrixToString(arr):
    output = ""
    
    # För varje bokstav i matrisen så ska den lägga till det i strängen
    for idx in range(len(arr)):
        for val in arr[idx]:
            output += val
    
    return output


def transposeMatrix(inArr, outArr):
    for r in range(len(inArr)):
        # Varje kolumn
        for c in range(len(inArr[0])):
            # Byt platsen på Kolumnen och raden från arry till outArr
            outArr[c][r] = inArr[r][c]

    return outArr


def transpositionEncrypt(txt, cAmount, encrypt):
    cols = cAmount
    rows = math.ceil(len(txt) / cols)
    
    if encrypt: 
        arr = fillArray(txt, [["" for n in range(cols)] for m in range(rows)]) # fyller en lista med en sträng
        print("Fyll listan: ", arr)
        outArr = transposeMatrix(arr, [["" for n in range(rows)] for m in range(cols)])  # Vänder på listan
        print("Vända listan", outArr)
    else: # Meddelandet ska avkrypteras då så börjar arrayen som omvänd jämfört med den orginella
        arr = fillArray(txt, [["" for n in range(rows)] for m in range(cols)])
        outArr = transposeMatrix(arr, [["" for n in range(cols)] for m in range(rows)])
    
    return matrixToString(outArr)


def traspositionBruteForce(string, comparing):
    tests = [] 
    n = 1

    while n < 100:
        current = transpositionEncrypt(string, n, False)
        tests.append(current)

        if current == comparing:
            return tests

        n += 1
    else:
        return "Kunde inte hitta rätt lösenord"
    



def passerad_tid():
    return time.time()


# Knäcka lösenord med en rekrussiv funktion
def bruteForce(current, passwordToCrack):
    # Om längden på längden på försök strängen är längre än lösenordet så ska den avsluta     
    if len(current) >= len(passwordToCrack):
        return None
 
    # För varje karaktär i alfabetet     
    for char in "abcdefghijklmnopqrstuvwxyz":
        # Lägg på nuvarande test med bokstaven
        newTest = current + char
        # Kolla ifall testet är lika med lösenordet
        if newTest == passwordToCrack:
            return {"password": newTest, "p_time": passerad_tid()}
        # Annars gör samma sak igen och spara de den returnerar
        isPassword = bruteForce(newTest, passwordToCrack)

        # Kollar ifall det funktionen returnerar inte är lika med if-statsen jag kollar över
        # Antingen så är det None eller så är det det knäckta lösenordet
        if isPassword is not None:
            return isPassword


# Ett annat sätt att knäcka lösenord. Genom att bara testa sig fram slumpmässigt
def randomBruteForce(passwordToCrack):
    test = ""
    while passwordToCrack != test:
        test = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(passwordToCrack)))
    return {"password": test, "p_time": passerad_tid()}


def main():
    for test in traspositionBruteForce("Irmd åadnged taä g", "Idag är det måndag"):
        print(test)
    choosenProgram = input("Vilket av följande program vill du köra? \n1 - Caesar Chiper\n2 - Transposition Chiper\n3 - Knäcka ett lösenord med bruteforce\nq - avsluta\n>> ")

    while True:
        if choosenProgram == "1":
            shiftAmount = int(input("Hur många steg ska varje bokstav skiftas med? > "))
            encrypt = input("Ska texten krypteras (1 / True) eller avkrypteras (0 / False)")

            if encrypt == "True" or encrypt == "true" or encrypt == "1":
                inText = input("Skriv in ett ord eller en mening ska krypters > ")
            elif encrypt == "False" or encrypt == "false" or encrypt == "0":
                inText = input("Skriv in ett ord eller en mening ska avkrypteras > ")
                shiftAmount *= -1

            outText = caesarEncrypt(inText, shiftAmount)

            print(f"Texten '{inText}' krypterades till '{outText}'")

            break
        elif choosenProgram == "2":
            rows = int(input("Hur många rader ska det vara i matrisen? "))
            
            inText = input("Skriv in ett ord eller en mening ska hanteras > ")
            
            encrypt = input("Ska texten krypteras (1 / True) eller avkrypteras (0 / False)")

            if encrypt == "True" or encrypt == "true" or encrypt == "1":
                outText = transpositionEncrypt(inText, rows, True)
                print(f"Texten '{inText}' krypterades till '{outText}'")
            elif encrypt == "False" or encrypt == "false" or encrypt == "0":
                outText = transpositionEncrypt(inText, rows, False)
                print(f"Texten '{inText}' avkrypterades till '{outText}'")
            
            break
        elif choosenProgram == "3":
            passwordToCrack = input("Vad är vilket lösenord vill du jämföra med? ")

            start_time = time.time()
            response = bruteForce("", passwordToCrack)
            
            print(response)
            break
        elif choosenProgram == "q":
            break
        else:
            print("Alternativet du valde finns inte i listan av program")
            choosenProgram = input("Vilket av följande program vill du köra? \n1 - Caesar Chiper\n2 - Transposition Chiper\n3 - Knäcka ett lösenord med bruteforce\nq - avsluta\n>> ")


if __name__ == "__main__":
    main()