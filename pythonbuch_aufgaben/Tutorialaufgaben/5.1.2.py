print("Geben Sie im folgenden die anzahl der Wörter ein die sie eingeben wollen")
anzahl = int(input("Anzahl:"))
liste = []
for i in range(anzahl):
    liste.append(input("Eingabe_" + str(i) + ":"))
print(liste)

