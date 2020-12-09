###############################################
# Författare: Linus Jansson 2F
# Uppgift 3 Beräkna bashuskostnaden
# Programet beräknar efter hur lång tid det blir billigare att köpa medlemskort än om man betalar för varje besök bara
###############################################

# While loop som kör så länge 200x är mindre än 100x + 800
x = 0
while 200 * x < 800 + 100 * x:
    x += 1
print ("Efter " + x + " besök blir medlemskortet billigare än att betala för varje besök")
