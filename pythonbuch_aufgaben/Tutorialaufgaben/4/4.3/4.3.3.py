print("Gib deine Noten ein:")
notenliste = []
notenliste[0] = int(input("Note1:"))
notenliste[1] = int(input("Note2:"))
notenliste[2] = int(input("Note3:"))
print(notenliste)
wd = float(input("Wunschdurchschnitt:"))

n4 = (len(notenliste) + 1)*wd-(notenliste[1] + notenliste[2] + notenliste[3])
print("Du benötigst mindestens die Note: ", n4)
