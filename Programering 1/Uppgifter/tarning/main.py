def genCombos(amount):
    return [[x, y] for x in range(1, amount + 1) for y in range(1, amount + 1)]

print(genCombos(2))
