###############################################
# Författare: Linus Jansson 2F
# Uppgift 5.6 
# Kollar ifall två texter är ett anagram av varandra
###############################################

# Tar bort alla mellanslag ifrån txt
def removeBlankSpace(txt):
    output = ""
    for n in txt:
        if n != " ":
            output += n

    return output

# Räknar hur många gånger en bokstav uppkommer i en text
def count(text, letter):
    count = 0

    for n in text:
        if n == letter:
            count += 1

    return count


text1 = input("Skriv in ett ord eller en mening >")
text2 = input("Skriv in ett till ord eller en mening > ")

anagram = False

# Sätter en variabel till texterna utan mellanslag
text1new = removeBlankSpace(text1)
text2new = removeBlankSpace(text2)

for n in text1new:
    # Kollar om n finns i text1 samma antal gånger som i text2.
    if count(text1new, n) == count(text2new, n):
        anagram = True
    else: 
        anagram = False
        break

if anagram == True:
    print(f"{text1} går att göra om till {text2}")
else:
    print(f"\"{text1}\" går inte att göra om till \"{text2}\"")