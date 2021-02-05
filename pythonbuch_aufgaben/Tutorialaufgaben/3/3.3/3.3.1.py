import math

print("Dies ist ein Programm welches die Diagonale eines Rechtecks mit der Seitenlänge a und b berechnet.")
a = float(input("Geben Sie Seite a ein:"))
b = float(input("Geben Sie Seite b ein:"))
c = math.sqrt(pow(a, 2)+pow(b, 2))
print("Das Ergebnis lautet: ", c)
