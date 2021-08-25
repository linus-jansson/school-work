###############################################
# Författare: Linus Jansson 2F
# Uppgift 7
# Datum = 10/11/2020
# Räknar ut skatten beroende på vilken lön som användaren skriver in
###############################################

salary = int(input("Hur mycket lön får du per månad? > "))

# Returnerar vilken skattetabell man ska använda sig av
def taxProcentage(salary):
    if salary < 20000:
        return 0.2
    elif 20000 <= salary <= 30000:
        return 0.25
    elif salary > 30000:
        return 0.3
    
# Skriver ut resultat
print(f"Du får betala {salary * taxProcentage(salary)} kr i skatt")
print(f"Din lön efter skatt är {salary * (1 - taxProcentage(salary))} kr")


