def meine_funktion(a,b):
    while b != 0:
        t = a%b
        a = b
        b = t
    return a

a = int(input("Gib A ein"))
b = int(input("Gib B ein"))
print(f'Ergebnis: {meine_funktion(a,b)}')
