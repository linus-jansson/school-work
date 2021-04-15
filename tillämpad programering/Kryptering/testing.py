# print(chr(122-32))

# txt = "z"

# encrypted = ""
# shift = 1

# for char in txt:
#     encrypted += chr((ord(char) + shift - 97) % 26 + 97)

# 122(z) + 1 = 123
# 123 - 97 = 26 
# 26 % 26 = 0 + 97 = 97 = a

# print((ord("a") + shift - 97) % 26 + 97)
# print((ord("a") + shift - 97) % 26)
# print(shift % 26)
# print(chr((ord("a") + 1 - 97) % 26 + 97))

# print(2%10)
# print(encrypted)

import math

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
    print(arr)
    
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

   
def transposeChipher(txt, rAmount, encrypt):
    rows = rAmount
    cols = math.ceil(len(txt) / rows)
    
    arr = fillArray(txt, [["" for n in range(cols)] for m in range(rows)])
    outArr = transposeMatrix(arr, [["" for n in range(rows)] for m in range(cols)]) # Skapar en array/lista som är omvänd jämfört med orginella listan
    
    return matrixToString(outArr)


def transposeReverse(txt):
    rows = 3
    cols = math.ceil(len(txt) / rows)
    
    arr = [["" for n in range(cols)] for m in range(rows)]
    outArr = [["" for n in range(rows)] for m in range(cols)] # Skapar en array/lista som är omvänd jämfört med orginella listan
    outTxt = ""

    currentChar = 0
    rCount = 0
    cCount = 0

    # För varje karaktär, fyll ut listan
    while currentChar <= len(txt) - 1:
        # Om raden är slut gå till nästa rad kolumn 0
        if len(outArr[0]) - 1 < cCount:
            rCount += 1
            cCount = 0
        
        outArr[rCount][cCount] = txt[currentChar]
        cCount += 1
        currentChar += 1
        # print(arr, arr[rCount][cCount], txt[currentChar])    
    print(outArr)

    for r in range(len(outArr)):
        # Varje kolumn
        for c in range(len(outArr[0])):
            # Byt platsen på Kolumnen och raden från arry till outArr
            arr[c][r] = outArr[r][c]

    print(arr)
    
 
    # För varje bokstav i matrisen så ska den lägga till det i outTxt
    for idx in range(len(arr)):
        for val in arr[idx]:
            outTxt += val
    
    return outTxt        


   
# Har argumenten "inmatade strängen" och en boolean ifall den ska kryptera eller dekryptera 
def transpose(txt): 
    rows = 3
    cols = math.ceil(len(txt) / rows) # Anpassar antalet kolumner 

    arr = [["" for n in range(cols)] for m in range(rows)]
    outArr = [["" for n in range(rows)] for m in range(cols)] # Skapar en array/lista som är omvänd jämfört med orginella listan

    outTxt = ""    

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
        # print(arr, arr[rCount][cCount], txt[currentChar])    
    print(arr)


    # För varje rad
    for r in range(len(arr)):
        # Varje kolumn
        for c in range(len(arr[0])):
            # Byt platsen på Kolumnen och raden från arry till outArr
            outArr[c][r] = arr[r][c]
    
    # För varje bokstav i matrisen så ska den lägga till det i outTxt
    for idx in range(len(outArr)):
        for val in outArr[idx]:
            outTxt += val
    
    return outTxt        

transposeText = "Hello world"
transposeReverseTxt = "Hore llWdlo"

encryptedText = transposeChipher(transposeText, 3, True)
decryptedText = transposeReverse(transposeReverseTxt)

# print(lista)
print(encryptedText)  
print(decryptedText)
