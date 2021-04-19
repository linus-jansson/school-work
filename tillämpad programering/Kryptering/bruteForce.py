import time
import threading

def passeradTid():
    return time.time()

def bruteForce(passwordToCrack):
    permuationResult = ""
    isDone = False
    listOfChars = "abcdefghijklmnopqrstuvwxyz"
    

    while isDone == False:        
        permuationResult += passwordToCrack
        if permuationResult == passwordToCrack:
            isDone = True
            # Returnerar den passerade tiden då lösenordet blev knäcked
            return (passeradTid(), permuationResult)
   
def main():
    start_time = time.time()
    password = "password"

    elapsedTime, crackedPassword = bruteForce(password)
    print(f"Cracked the password '{crackedPassword}' in {elapsedTime - start_time} ms")

if __name__ == "__main__":
    main()
