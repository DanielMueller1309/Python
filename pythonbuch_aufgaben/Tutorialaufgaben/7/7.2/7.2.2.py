#funktion
def quersumme(zahl):
    summe = 0
    for i in range(len(zahl)):
        summe += int(zahl[i])
    return summe
#Hauptprogramm:
zahl = str(input("Wir berechnen ihre Quersumme von ihrer Zahl:"))
print(f'Ihre quersumme ist: {quersumme(zahl)}')