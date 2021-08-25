###############################################
# Författare: Linus Jansson 2F
# Uppgift 2
# Datum = 10/11/2020
# Löser skillnaden mellan två åldrar som användaren skriver in 
###############################################

ålder1 = int(input("Skriv in den första personens ålder > "))
ålder2 = int(input("Skriv in den andra personens ålder > "))

# Räknar ut skillnaden
skillnad = ålder1 - ålder2

# Ifall talet är negativt så ska den ändra det till ett positivt tal
if skillnad < 0:
    skillnad *= -1

# Skriver ut åldern
print(f"Ålderskillnaden mellan {ålder1} och {ålder2} är {skillnad} år")