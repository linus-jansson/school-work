flytal = float(input("Skriv in ett flytal > "))
heltal = int(input("Skriv in ett heltal > "))
string = str(input("Skriv in en sträng > "))

arr = [flytal, heltal, string]

print("Din inmatade data:")
for n in arr:
    if type(n) == float:
        # print('{0:>12.02f}'.format(round(n, 2)))
        print('{0:>12.02f}'.format(n))
    else:
        print('{0:>12}'.format(n))


