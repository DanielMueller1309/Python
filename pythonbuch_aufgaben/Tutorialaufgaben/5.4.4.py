import random
tip = []
print("Dieses Programm zieht 6 aus 49")
zahlen = sorted(random.sample(range(1, 50), 6))
print("Gib deinen Tip ein")
for i in range(6):
    tip.append(int(input("Zahl" + str(i+1) + ":")))
tip = sorted(tip)

print("Die heutigen Lottozahlen lauten:", zahlen)
print("Du hast folgendes getippt:      ", tip)
z = 0
for i in range(6):
    if zahlen[i] - tip[i] != 0:
        z += 1
if z == 0:
    print("Herzlichen Glückwunsch, hättest du mal echtes Lotto gespielt :D")
else:
    print("Satz mit x das war wohl nix :D")