###############################################
# Författare: Linus Jansson 2F
# Uppgift 1 
# Programet undersöker ifall string som användaren matar in; slutar och börjar på samma sak.
###############################################

# Definerar string till det som användaren skriver in
string = input("Skriv in en sträng > ")

# Kollar första indexet i strängen och sista index och kollar ifall de är samma
if (string[0] == string[-1]):
    print(f" {string} börjar & slutar på samma bokstav; {string[0]} och {string[-1]}")