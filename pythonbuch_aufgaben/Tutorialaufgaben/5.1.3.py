print("Dies ist ein Program zur Berechnung der Fakultät")
f = int(input("Geben Sie nun die Zahl ein aus der die Fakulät berechnet werden soll:"))
ergebnis = 1
for i in range(1, f + 1):
    ergebnis = ergebnis * i
print("Ergebnis:", ergebnis)
