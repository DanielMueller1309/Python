#Main-Programm:
print("Dieses Programm wandelt eine dez in eine bin und anders herum.")

#damit die erste schleife startet
schleife = 'j'
while schleife in ['j', 'J']:
    antwort = input("Was wollen sie Umwandeln?(D[ezimalzahl] oder B[inärzahl]")

    #fehleingaben bei der umrechnungsauswahl abfangen
    while antwort not in ['D', 'd', 'B', 'b']:
        print("Ihre Eingabe war leider falsch...Versuchen sie es erneut.")
        antwort = input("Was wollen sie Umwandeln?(D[ezimalzahl] oder B[inärzahl]")

    # Zahleneingabe:
    zahl = int(input("Geben sie nun hier ihre Zahl ein:"))

    # if auswahl welche umwandlung genutz wird
    if antwort in ['B', 'b']:
        print(f'Ihre umgewandelte Zahl laute: {int(zahl, 2)}')
    if antwort in ['D', 'd']:
        print(f'Ihre umgewandelte Zahl laute: {bin(zahl)}')

    schleife = input("Möchten sie noch eine weitere Zahl umwandeln? (J/N)")

    # fehleingabe bei der programmwiederholung
    while schleife not in ['j', 'J', 'n', 'N']:
        print("Es wurde eine Fehleingabe entdeckt, veruchen sie es erneut...")
        schleife = input("Möchten sie noch eine weitere Zahl umwandeln? (J/N)")