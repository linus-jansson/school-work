import time
import random

def passerad_tid():
    return time.time()

# Ett annat sätt att knäcka lösenord. Genom att bara testa sig fram
def randomTest(passwordToCrack):
    test = ""
    while passwordToCrack != test:
        test = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(passwordToCrack)))
    return test

# Knäcka lösenord med en rekrussiv funktion
def bruteForce(current, passwordToCrack):
    # Om längden på längden på försök strängen är längre än lösenordet så ska den avsluta     
    if len(current) >= len(passwordToCrack):
        return None
 
    # För varje karaktär i alfabetet     
    for char in "abcdefghijklmnopqrstuvwxyz":
        # Lägg på nuvarande test med bokstaven
        newTest = current + char
        # Kolla ifall testet är lika med lösenordet
        if newTest == passwordToCrack:
            return {"password": newTest, "p_time": passerad_tid()}
        # Annars gör samma sak igen och spara de den returnerar
        isPassword = bruteForce(newTest, passwordToCrack)

        # Kollar ifall det funktionen returnerar inte är lika med if-statsen jag kollar över
        # Antingen så är det None eller så är det det knäckta lösenordet
        if isPassword is not None:
            return isPassword
