liste = []
for i in range(10):
    liste.append(int(input("Zahl_" + str(i+1))))
liste.sort()
print("kleinste Zahl:" + str(liste[0]))
print("größte Zahl:" + str(liste[len(liste)-1]))
