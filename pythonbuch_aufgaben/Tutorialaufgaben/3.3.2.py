import math

print("Dies ist ein Programm welches die Diagonale jeder seite eines Quaders mit der Seitenlänge a und b und c berechnet.")
a = float(input("Geben Sie Seite a ein:"))
b = float(input("Geben Sie Seite b ein:"))
c = float(input("Geben Sie Seite b ein:"))


ab = math.sqrt(pow(a, 2)+pow(b, 2))
print("Die Diagonale der Seite ab ist: ", ab, "lang.")

ac = math.sqrt(pow(a, 2)+pow(c, 2))
print("Die Diagonale der Seite ac ist: ", ac, "lang.")

bc = math.sqrt(pow(b, 2)+pow(c, 2))
print("Die Diagonale der Seite bc ist: ", bc, "lang.")

rd = math.sqrt(pow(bc, 2)+pow(a, 2))
print("Die Raumdiagonale ist: ", rd)
