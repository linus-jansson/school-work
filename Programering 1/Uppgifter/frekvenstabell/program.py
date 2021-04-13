activities = ["Games",
              "Basketball",
              "Track",
              "Football",
              "Dancing",
              "Track",
              "Horses",
              "Football",
              "Basketball",
              "Football",
              "Basketball",
              "Horses",
              "Rpg's",
              "Track",
              "Horses",
              "Football",
              "Basketball",
              "Basketball",
              "Track",
              "Football",
              "Dancing",
              "Track",
              "Horses",
              "Football",
              "Basketball",
              "Football",
              "Football",
              "Basketball",
              "Horses",
              "Rpg's",
              "Football",
              "Track",
              "Football"]

frekvenstabell = {}

# För varje aktivitet
for n in activities:
    # Om nyckeln inte finns så lägger den till den med antalet som uppkommer som värde
    if not n in frekvenstabell.keys():
        frekvenstabell[n] = activities.count(n)

print("Aktivitet : Frekvens : Relativt Frekvens")
for key, item in frekvenstabell.items():
    # Skriver ut nyckeln, antalet och procenten
    print('{0:<12}{1:^13}{2:>12}%'.format(key, item, round(item/len(activities), 3)*100 ))    
