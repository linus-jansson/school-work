###############################################
# Författare: Linus Jansson 2F
# Selektion extrauppgifter del 2; Uppgift 2
# Programet frågar efter en temperatur och sen ska programmet bestämma vilka kläder man borda ha på sig
###############################################

# Definerar temp utifrån vad användaren skriver in 
temp = int(input("Vilken temperatur är det utomhus > "))


# Kollar vilka kläder som är lämpligt att ha på sig
if temp >= 23:
    print("Tror du inte behöver så mycket kläder på dig, kanske t-shirt och kanske en shorts")   
elif 15 < temp < 22:
    print("Kanske behövs en hoodie") 
elif 0 < temp < 15:
    print("kanske behövs en vår/höst jacka")
else:
    print("Dags att ha på sig en tjock jacka")

