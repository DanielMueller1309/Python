print("Dies ist ein Programm welches das Colatz-Problem wiederspiegelt.")
zahl = int(input("Geben Sie eine beliebige Natürliche Zahl ein:"))
print("[" + str(zahl) + "]")
while zahl != 1:
    if zahl % 2 == 0:
        zahl = zahl/2
    else:
        zahl = zahl * 3 + 1
    print("[" + str(zahl) + "]")
