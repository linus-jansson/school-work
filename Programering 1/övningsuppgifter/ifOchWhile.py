# Författare: Linus Jansson 2F
# Det här pogrammet frågar efter ett lösenord
#
#
correctPassword = "1337"
passwordGuess = str(input("What is the password > "))

if (correctPassword == passwordGuess):
    print("Correct Password")
else:
    print("Invalid Password")
    passwordGuess = str(input("What is the password > "))