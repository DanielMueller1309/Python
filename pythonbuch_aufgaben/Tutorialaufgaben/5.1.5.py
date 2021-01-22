notenliste = []
a = int(input("Gib deine Notenanzahl ein:"))
notensumme = 0
for i in range(a):
    print(i)
    notenliste.append(int(input("Note_" + str(i) + ":")))
    notensumme = notensumme + int(notenliste[i])
print(notenliste)
wd = float(input("Wunschdurchschnitt:"))

n = (len(notenliste) + 1) * wd - notensumme
print("Du benötigst mindestens die Note: ", n)
