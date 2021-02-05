zahl = float(input("Gib eine Zahl ein:"))
p = 1
for i in range(2, 9):
    if zahl % i == 0:
        p = 0
        i = 10
if p == 1:
    print("Die Zahl", zahl, "ist eine Primzahl")
else:
    print("Die Zahl", zahl, "ist keine Primzahl")