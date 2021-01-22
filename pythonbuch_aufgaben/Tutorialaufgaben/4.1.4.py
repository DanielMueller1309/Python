print("Gib deine Noten ein:")
n1 = int(input("Note1:"))
n2 = int(input("Note2:"))
n3 = int(input("Note3:"))
wd = float(input("Wunschdurchschnitt:"))

n4 = 4*wd-(n1+n2+n3)
print("Du benötigst mindestens die Note: ", n4)
