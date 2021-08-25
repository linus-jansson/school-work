from random import randint

def bulgariskPatiens(deckOfCards):
    # En del av en vanlig kortlek (minst 2 kort, högst 52) f ̈ordelas godtyckligt i n ̊agra högar
    # på bordet (val ̈oren på korten är ointressant i detta spel).

    # Ett kort tas från varje hög och dessa får bilda en ny hög. Upprepa detta tills det går att
    # avgöra att patiensen har gått ut