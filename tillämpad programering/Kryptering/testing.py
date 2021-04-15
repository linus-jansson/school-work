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

def hello():
    return "hello world"

functionTable = {
    "1": hello()
}

print(functionTable["1"])