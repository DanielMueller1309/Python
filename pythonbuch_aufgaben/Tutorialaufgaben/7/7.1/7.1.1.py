#Funktion:

def buchstabenklau(string):
    buchstaben = string[0] + string[len(string)-1]
    return buchstaben

#Hauptprogramm
print(buchstabenklau(input("Gib ein Wort ein:")))