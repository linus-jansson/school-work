###############################################
# Författare: Linus Jansson 2F
# Uppgift 5
# Tar bort element 0, 4 och 5 från en lista
###############################################

lista = ["Röd", "Grön", "Vit", "Svart", "Rosa", "Gul"]

print(lista) # Skriver ut listan innan den tagit bort ifrån listan

del(lista[5], lista[4], lista[0]) # Tar bort från listan

print(lista) # Skriver ut listan efter den tagit bort från listan
    

