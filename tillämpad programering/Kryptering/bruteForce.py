from hashlib import new
import time
import random

def randomTest(passwordToCrack):
    test = ""
    while passwordToCrack != test:
        test = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(passwordToCrack)))
    return test
# Knäcka lösenord med en rekrussiv funktion
def bruteForce(current, passwordToCrack):
    # Om längden på längden på försök strängen är längre än lösenordet så ska den sluta eller om den är klar så returnerar den
    # if len(current) != len(passwordToCrack) - 1: 
    #     return None
    if len(current) >= len(passwordToCrack):
        # print("Kunde inte hitta lösenordet")1
        # return "Kunde inte hitta lösenordet"
        return None
 
    # För varje karaktär i alfabetet     
    for char in "abcdefghijklmnopqrstuvwxyz":
        # Lägg på nuvarande test med bokstaven
        newTest = current + char
        # print(newTest)
        # Kolla ifall testet är lika med lösenordet
        if newTest == passwordToCrack:
            return newTest
        # Annars gör samma sak igen
        x = bruteForce(newTest, passwordToCrack)
        if x is not None:
            return x
   
def main():
    passwordToCrack = "pwda"
    c = ""
    start_time = time.time()
    res = bruteForce(c, passwordToCrack)
    stop_time = time.time()

    print(res, stop_time - start_time)
    # for i in range(100):
    #     start_time2 = time.time()
    #     res2 = randomTest(passwordToCrack)
    #     stop_time2 = time.time()
    #     sum2 += stop_time2 - start_time2
    #     print(i)

    # print(res2, "random",  sum2)


    # print(f"Cracked the password '{crackedPassword}' in {elapsedTime - start_time} ms")

if __name__ == "__main__":
    main()
