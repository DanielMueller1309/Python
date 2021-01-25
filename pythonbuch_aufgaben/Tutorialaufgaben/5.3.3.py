print("Dies ist ein Porgramm welches die Fibonacci-Reihe bis zu einer Ausgewählten Zahl ausgibt.")
zahl = int(input("Gib nun die zahl ein bis wohin die Folge ausgegeben werden soll:"))
liste = [0, 1]
i = 1
while liste[i] < zahl:
    liste.append(liste[i-1] + liste[i])
    i += 1
print(liste)
