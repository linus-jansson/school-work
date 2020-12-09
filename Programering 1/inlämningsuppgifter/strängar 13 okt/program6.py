###############################################
# Författare: Linus Jansson 2F
# Uppgift 6
# Frågar efter ett personnummer och avgör om man är man eller kvinna; 
#   udda om du är man och jämnt om du är kvinna
###############################################
nmr = input("Skriv in ditt personnummer yymmddxxxx > ") # Frågar efter personens personnummer

# Kollar bitwise med en XOR operator 
if int(nmr[8]) & 1: # Om det är blir 1 så är nmr[8] udda; Om det är 0 så är nmr[8] jämnt 
    print(f"Du är en man enligt ditt personnummer {nmr} : {nmr[8]}")
else:
    print(f"Du är en kvinna enligt ditt personnummer {nmr} : {nmr[8]}")
