###############################################
# Författare: Linus Jansson 2F
# Uppgift 8
# Låter användaren öva på 7ans multiplikations tabell
###############################################

from random import shuffle

# Genererar en lista med 10 tal 1-10
tal = [i for i in range(1, 11)]
points = 0

while True:
    # Kollar ifall användaren har svarat på alla frågor
    if len(tal) < 1:
        if points == 10:
            print("Du hade rätt på alla frågor. Grattis!")
        else:
            print(f"Du hade rätt på {points} frågor; Bättre kan du nästa gång!")

        break

    # Slänger om listan med nummer
    shuffle(tal)
    # Sätter x till första talet på listan
    x = tal[0]
    # Frågar användaren efter 7 gånger första talet på listan (x)
    guess = int(input(f"vad är 7 * {x} lika med? > "))

    # Tar bort talet x från listan
    tal.remove(x)

    if guess == (7 * x):
        # Lägger till ett poäng om användaren har rätt
        points += 1

    