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

# def hello():
#     return "hello world"

# functionTable = {
#     "1": hello()
# }

# print(functionTable["1"])


# listOfChars = 'abcd'
# list(listOfChars)
# key = "abc"


# for char in range(len(listOfChars)):
#     for char2 in listOfChars:
#         print(char, char2)


# def all_perms(s):
#     if len(s) <= 1: 
#         yield s
#     else:
#         for i in range(len(s)):
#             for p in all_perms(s[:i] + s[i+1:]):
#                 yield s[i] + p


# allPerms = all_perms("password")

# for n in allPerms:
#     print(n)

# charList = "abcde"

# for n in range(8):
#     a = [i for i in charList]
#     print(a)
#     # for y in range(n):
#         # print(y)

# for n in range(10):
#     print(n)


# your_list = 'abcdefghijklmn opqrstuvwxyz'
# complete_list = []
# for current in range(4):
#     a = [i for i in your_list]
#     for y in range(current):
#         print([x+i for i in your_list for x in a] )
#         a = [x+i for i in your_list for x in a] 
#         # print(complete_list)
#         # print(a)
        
#     complete_list = complete_list+a

# print(complete_list)

# for n in complete_list:
#     if n == "he j":
#         print(n)
# # # print(complete_list)


# def all_combos(s, l):
#     if l <= 10:
#         print(l)
#         all_combos(s, l + 1)


# all_combos("s", -10)

#import time
#
#def shift(char, shiftAmount):
#    return chr((ord(char) + shiftAmount - 97) % 26 + 97)
#
#def getCharNum(char):
#    return ord(char)
#
#shiftNum = 1
#char = 'a'
#attempt = ''
#
#while True:
#    time.sleep(0.5)
#    
#    print(char)
#
#    if getCharNum(char) == 122:
#        print("startar om")
#        attempt += char
#
#    char = shift(char, shiftNum)

# your_list = 'abc'
# complete_list = []
# for current in range(4):
#     a = [i for i in your_list]
#     for y in range(current):
#         a = [x+i for i in your_list for x in a] 
#         # print(complete_list)
#         # print(a)
#         print(a, len(a), end="\n") 
#     complete_list = complete_list+a



# password = "hej"

# for n in range(len(password)):
#     pass

# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# inPassword = "qwerty"
# password = list(inPassword)
# # Varje bokstav i försöket ska storeas i listan test ['a', 'a', 'z', 'a']
# test = []

# for n in range(len(password)):
#     if test == password:
#         print("Ja!")
#         break

