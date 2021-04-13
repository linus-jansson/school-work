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
def transpose(txt, cols):
    # arr = [[""]* cols] * 3
    arr = [[] for n in range(cols)] for m in range(3)
    
    # math.ceil(len(txt) / columoner)

    # För varje karaktär, fyll ut listan
    currentChar = 0
    rCount = 0
    cCount = 0

    while currentChar <= len(txt) - 1:
        # Om raden är slut gå till nästa rad kolumn 0
        if len(arr[0]) - 1 < cCount:
            rCount += 1
            cCount = 0
        
        arr[rCount][cCount] = txt[currentChar]
        print(arr, arr[rCount][cCount], txt[currentChar])
        cCount += 1
        currentChar += 1
    
    # print(txt)
    # arr[0][1] = txt[4].upper()
    # print(len(arr[0]*len(arr)))
    # print(arr[0])
    
    print(arr)
    # Skapar en array/lista som är omvänd jämfört med orginella listan
    outArr = [["A"] * 3] * cols
    # print(outArr)
    outTxt = ""

    # För varje rad
    for r in range(len(arr)):
        # Varje kolumn
        for c in range(len(arr[0])):
            # Byt platsen på Kolumnen och raden från arry till outArr
            outArr[c][r] = arr[r][c]
    
    # För varje bokstav i matrisen så ska den lägga till det i outTxt
    # for idx in range(len(outArr)):
    #     for val in outArr[idx]:
    #         outTxt += val
    
    return outTxt        

inT = "Hello World"
lista = transpose(inT, 6)

# for n in lista:
# print(lista)
