###############################################
# Författare: Linus Jansson 2F
# Uppgift 5.7
# Kollar ifall två texter är ett anagram av varandra
###############################################

text = input("Skriv en text på svenska för att översätta till engelskt format och vice versa (aa = å, ae = ä, oe = ö)? > ")
textNew = ""

# Används för att hoppa över iterationer för att undvika att skriva ut e i ae
skip = False 
# Håller koll på vilken bokstav den är på
idx = 0

# För varje bokstav i texten som användaren skriver in
for n in text:

    # Om skip är true så ska den sätta skip till False och gå vidare
    if skip: 
        skip = False

    else:

        # Kollar ifall bokstaven är a och skip är false och att längden på texten inte blir mindre än index + 1
        if (n == "a") and (not skip) and len(text) > idx + 1: 
            
            # Kollar ifall nästa bokstav är a
            if text[idx + 1] == "a": 
                skip = True # Sätter skip till True och skippar sen så den inte lägger till a i strängen efter å
                textNew += "å" # lägger till å till nya strängen  
            elif text[idx + 1] == "e":
                skip = True
                textNew += "ä"
            else:
                textNew += n

        elif (n == "o") and (not skip) and len(text) > idx + 1:
            # Fungerar på samma sätt som över
            if text[idx + 1] == "e":
                skip = True
                textNew += "ö"
            else:
                textNew += n

        # Om användaren skriver på svenska vill vi översätta till engelskt format
        elif (n == "å"):
            textNew += "aa"
        elif (n == "ä"):
            textNew += "ae"
        elif (n == "ö"):
            textNew += "oe"
        
        # Om inget av de över stämmer så ska den bara lägga till samma bokstav 
        else:
            textNew += n

    # "Nästa ord"
    idx += 1

print("Översatta texten:")
print(textNew)