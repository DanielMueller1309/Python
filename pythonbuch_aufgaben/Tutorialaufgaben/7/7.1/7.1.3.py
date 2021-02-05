#Funktion
def teilermenge(z):
    liste = []
    for i in range(z, 0, -1):
        if z % i == 0:
            liste.append(int(z/i))
    return liste

def verteilung(t_liste, p_liste):
    vert_list = []
    for i in range(len(p_liste)):
        vert_list.append(0)

    for i in range(len(t_liste)):
        for j in range(len(vert_list)):
            if t_liste[i] % p_liste[j] == 0:
                vert_list[j] += 1
    return vert_list

def primzahlen(zahl):
    liste = [2, 3, 5, 7]
    p_liste = []
    for i in range(2, zahl + 1):
        p = 0
        for j in range(4):
            if i % liste[j] == 0:
                p += 1
                if i == liste[j]:
                    p -= 1
        if p == 0:
            p_liste.append(i)
    return p_liste

#Hauptprogramm
zahl = int(input("Gib eine Zahl ein:"))
p_liste = primzahlen(zahl)
t_liste = teilermenge(zahl)
print("Deine liste:",teilermenge(zahl))
print("Primzahlen bis zu dieser Zahl:", primzahlen(zahl))
print("Häufugkeitsverteilung der Teiler:", verteilung(teilermenge(zahl), primzahlen(zahl)))
