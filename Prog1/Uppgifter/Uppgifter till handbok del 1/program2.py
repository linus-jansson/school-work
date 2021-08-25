###############################################
# Författare: Linus Jansson 2F
# Uppgift Förändringsfaktor; 
# Datum = 01/13/2021
###############################################
changeFactor = float(input("Ange en förändringsfaktor: "))

pdec = changeFactor - 1
proc = pdec * 100
print(f"Förändringsfaktorn {changeFactor} motsvarar ", end = '')

if proc > 0:
    print(f"en ökning med {round(proc, 2)}%.")
    if changeFactor >= 2: # förändringsfaktorn är större än 2 så ska den också skriva ut hur många gånger större den är också
        print(f"Det bilr då {changeFactor} större")
elif proc < 0:
    print(f"en minskning med {abs(round(proc, 2))}%.")
else:
    print("ingen förändring alls.")

proc = float(input("Ange en procentuell förändring: "))
changeFactor = 1 + (proc / 100) # gör om procenten till en förändringsfaktor

print(f"Förändringsfaktorn är {abs(changeFactor)} av {proc}%")

