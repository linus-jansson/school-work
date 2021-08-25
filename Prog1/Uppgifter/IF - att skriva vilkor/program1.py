###############################################
# Författare: Linus Jansson 2F
# Uppgift 1
# Datum = 10/11/2020
# Löser ekvationen 7/x + 4x + 121 = 208
###############################################

def f(x):
    return x/7 + 4*x + 121

x = 0
marginal = 1
trys = 0
# så länge den inte har hittat svaret
while True: 
    x += marginal

    if (f(x) == 208): 
        print(f"f(x) är: {x}")
        break # Hoppa ut ur loopen
    elif (f(x) > 208):
        # Om talet f(x) är större än 208 så ska den sänka sökmarginalen som den letar på och sänka / 10
        if trys > 10: # Programet har 10 försök på sig att lösa uppgiften
            print("Kan inte lösa den uppgiften")
            break
        
        # Sänker marginalen med / 10; ökar antalet försök och sätter x till default igen
        marginal /= 10
        trys += 1
        x = 0

    