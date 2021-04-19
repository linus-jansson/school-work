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


def all_perms(s):
    if len(s) <= 1: 
        yield s
    else:
        for i in range(len(s)):
            for p in all_perms(s[:i] + s[i+1:]):
                yield s[i] + p


allPerms = all_perms("password")

for n in allPerms:
    print(n)

# charList = "abcde"

# for n in range(8):
#     a = [i for i in charList]
#     print(a)
#     # for y in range(n):
#         # print(y)

# for n in range(10):
#     print(n)


# your_list = 'ab'
# complete_list = []
# for current in range(3):
#     a = [i for i in your_list]
#     for y in range(current):
#         print([x+i for i in your_list for x in a] )
#         a = [x+i for i in your_list for x in a] 
#         # print(complete_list)
#         # print(a)
        
#     complete_list = complete_list+a

# # print(complete_list)
