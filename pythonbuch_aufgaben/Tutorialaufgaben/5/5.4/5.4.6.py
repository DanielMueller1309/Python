liste = [1, 4, 3, 3, 5, 7, 2]
a = liste
print(sorted(a))
user_input = 'j'
nutzer_liste = []
while user_input in ['j', 'J']:
    nutzer_liste.append(int(input("geben sie nun zahlen ein:")))
    user_input = input("Möchten sie noch eine Zahl eingeben?(J/N):")
    while user_input not in ['j', 'J', 'n', 'N']:
        print('Eingabe ungültig!')
        user_input = input("Möchten sie noch eine Zahl eingeben?Geben Sie 'J' für ja oder 'N' für Nein ein:")
print("Hier ihre Liste (extra für Sie sortiert, macht dann 1 Mark 50)")
print(sorted(nutzer_liste))
