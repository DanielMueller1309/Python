print("Dies ist ein Programm welches eine Abschreibung berechnet.")
wert = [float(input("geben Sie die kosten des Produkts an:"))]
zeit = float(input("Geben Sie die zeit in jahren an:"))
i = 0
senkung = wert[i] / zeit
while wert[i] > 0:
    wert.append(wert[i] - senkung)
    i += 1
i = 0
for i in range(len(wert)):
    print("Jahr", str(i) + ":", wert[i])
