# Linus Jansson 2F
# Det här programet gör om celcius från fahrenheit till celcius
#
#
print("Det här porgramet gör om celcius till fahrenheit")

celciusTemperatur = int(input("Ge en temperatur i celcius som du vill göra om till fahrenheit > ")) # Fråga efter celcius temperaturen

fahrenheitTemp = celciusTemperatur * 9 / 5 + 32 # Räkna ut fahrenheit från celcius

print("Din " + str(celciusTemperatur) +"C temperatur i Fahrenheit är " + str(fahrenheitTemp)+ "F") # Skriver ut vad Temperaturen är i fahrenheit 