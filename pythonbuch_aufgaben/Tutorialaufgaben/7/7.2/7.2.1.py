#funktionen:
def fakultaet(zahl):
    for i in range(zahl, 1, -1):
        zahl = zahl*(i-1)
    return  zahl

#Hauptprogramm:
zahl = int(input("geben sie bitte die zahl ein aus welcher die fakultät berechnet werden soll:"))
print(f'ihre fakultät ist: {fakultaet(zahl)}')
