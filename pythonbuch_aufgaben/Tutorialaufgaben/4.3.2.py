liste_a = ['Hallo', 'schönes', 'Wetter']
print(liste_a)
liste_b = liste_a
print("a: ", liste_a)
print("b:", liste_b)
liste_b[1] = 'schlechtes'
print("nach schlechte")
print("a: ", liste_a)
print("b:", liste_b)
print(liste_a[0], liste_a[1], liste_a[2])

a = 45
b = a
print("a: ", a)
print("b: ", b)
b = 3
print("a: ", a)
print("b: ", b)