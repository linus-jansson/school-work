
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

   
def transposositionEncrypt(txt, rAmount, encrypt):
    rows = rAmount
    cols = math.ceil(len(txt) / rows)
    
    if encrypt: 
        arr = fillArray(txt, [["" for n in range(cols)] for m in range(rows)])
        outArr = transposeMatrix(arr, [["" for n in range(rows)] for m in range(cols)]) # Skapar en array/lista som är omvänd jämfört med orginella listan
    else:
        arr = fillArray(txt, [["" for n in range(rows)] for m in range(cols)])
        outArr = transposeMatrix(arr, [["" for n in range(cols)] for m in range(rows)]) # Skapar en array/lista som är omvänd jämfört med orginella listan
    
    return matrixToString(outArr)

# transposeText = input("Skriv in en mening som du vill kryptera > ")

# encryptedText = transposeChipher(transposeText, 3, True)
# decryptedText = transposeChipher(encryptedText, 3, False)

# print(f"Krypterad text: {encryptedText}")  
# print(f"Avkrypterad text: {decryptedText}")
