###############################################
# Författare: Linus Jansson 2F
# Uppgift; Eratosthenes Såll
# Programet räknar ut hur primtal med hjälp av eratosthens såll
###############################################

nmr = int(input("Hur många primtal vill du räkna ut? > "))

# Generera en lista med tal från 2 till den längd som användaren vill
lista = [i for i in range(2, nmr + 1)]

# För varje position i listan
for pos in range(len(lista)):
    # Kolla varje postion mellan positionen och längden på listan
    for index in range(pos+1, len(lista)):

        # Kollar ifall index är längre än längden på listan
        # Kollar om värdet på index i listan är jämnt delbart med värdet på pos i listan
        if index < len(lista) and lista[index] % lista[pos] == 0:
            # Ta bort värdet från listan
            lista.remove(lista[index])

print(f"Primtalen mellan 2 och {nmr} är:")
print(lista)