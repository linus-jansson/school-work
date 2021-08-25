def genCombos(a, d):
    return [(x, y) for x in range(1, a+1) for y in range(1, a+1)]

def numOfCombos(diceSides, n):
    return diceSides**n

def generateTable(combinations):
    outDict = {}
    
    for pair in combinations:
        # print(pair, '->', x, '+', y, ' = ', x + y)
        # Lägger till alla summor till tabellen om summan av de är samma som namnet på nyckeln i tabellen 
        outDict[str(sum(pair))] = [ [num for num in testingPairs] for testingPairs in combinations if (sum(testingPairs) == sum(pair))]

    return outDict

def printTable(key, combo):
    print(f"Sum {key}: {'*' * len(combo)}")

def main():
    numOfSides = int(input("Hur många sidor finns det på tärningen? > "))
    numOfDice = int(input("Hur många tärningar finns det? > "))
    
    combinations = genCombos(numOfSides, numOfDice)
    print(combinations)

    tabell = generateTable(combinations)
    
    print(f"{numOfDice} tärningar med {numOfSides} sidor kommer ge {numOfCombos(numOfSides, numOfDice)} kombinationer")
    
    for key, val in tabell.items():
        printTable(key, val)

if __name__ == "__main__":
    main()