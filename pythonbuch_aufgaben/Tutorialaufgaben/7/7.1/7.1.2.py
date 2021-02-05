
def summe(z):
    s = 0
    for i in range(z+1):
        s = s + i
    return s




#Hauptprogramm
print("Deine Summe:",summe(int(input("Gib eine Zahl ein:"))))