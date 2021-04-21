def genCombos(a, d):
    return [(x, y) for x in range(1, a+1) for y in range(1, a+1)]

def numOfCombos(diceSides, n):
    return diceSides**n

def generatePairSums(combinations):
    outDict = {}
    
    for pair in combinations:
        # print(pair, '->', x, '+', y, ' = ', x + y)
        outDict[str(sum(pair))] = [ [num for num in testingPairs] for testingPairs in combinations if (sum(testingPairs) == sum(pair))]

    return outDict

        
def printTable(key, combo):
    print(key, combo)


numOfSides = 3
numOfDice = 2

print(genCombos(numOfSides, numOfDice))

combinations = genCombos(numOfSides, numOfDice)

tabell = generatePairSums(combinations)

print(f"{numOfDice} tärningar med {numOfSides} sidor kommer ge {numOfCombos(numOfSides, numOfDice)} kombinationer")
for key, val in tabell.items():
    printTable(key, val)


