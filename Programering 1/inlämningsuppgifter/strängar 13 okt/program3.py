###############################################
# Författare: Linus Jansson 2F
# Uppgift 3
# Frågar användaren efter ett datum i svenskt format och sen gör den om det till amerikanskt format
###############################################

sv_datum = str(input("Skriv ett svenskt datun år-mm-dd > "))

# Bestämmer år, dag och månad efter den template som användaren skriver in
year = sv_datum[:2]
month = sv_datum[3:5]
day = sv_datum[6:]

# Gör om till amerikanskt datum
am_datum = month + "/" + day + "/" + "20" + year 

# Skriver ut
print(f"Amerikanskt datum: {am_datum}")

