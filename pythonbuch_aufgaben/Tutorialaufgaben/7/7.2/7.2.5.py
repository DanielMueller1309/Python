#Funktionen
#Prüft ob die eingabe der binzahl auch eine ist.
def eingabe_bin(binzahl):
    i = 0
    while i in range(len(binzahl)):
        if binzahl[i] not in ['1', '0']:
            print("Ihre eingebene Zahl ist keine vollwertige Binärzahl")
            binzahl = input("Bitte erneut ihre zahl eingeben:")
            i = -1
        i += 1
    return binzahl

#wandelt dezimal zu binär
def dez_to_bin(dezzahl):
    binzahl = []
    p = 0
    while int(dezzahl) > 0:
        binzahl.append(str(int(dezzahl) % 2))
        p += 1
        if p % 4 == 0:
            binzahl.append(' ')
            p = 0
        dezzahl = dezzahl//2
    binzahl.reverse()
    binzahl = ''.join(binzahl)
    return binzahl
#wandelt binär zu dezimal
def bin_to_dez(binzahl):
    binzahl = eingabe_bin(binzahl)
    dezzahl = 0
    z = 0
    for i in range(len(binzahl)-1, -1, -1):
        dezzahl = dezzahl + (2**z)*int(binzahl[i])
        z += 1
    return dezzahl
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
    zahl = input("Geben sie nun hier ihre Zahl ein:")

    # if auswahl welche umwandlung genutz wird
    if antwort in ['B', 'b']:
        print(f'Ihre umgewandelte Zahl laute: {bin_to_dez(zahl)}')
    if antwort in ['D', 'd']:
        print(f'Ihre umgewandelte Zahl laute: {dez_to_bin(int(zahl))}')

    schleife = input("Möchten sie noch eine weitere Zahl umwandeln? (J/N)")

    # fehleingabe bei der programmwiederholung
    while schleife not in ['j', 'J', 'n', 'N']:
        print("Es wurde eine Fehleingabe entdeckt, veruchen sie es erneut...")
        schleife = input("Möchten sie noch eine weitere Zahl umwandeln? (J/N)")
