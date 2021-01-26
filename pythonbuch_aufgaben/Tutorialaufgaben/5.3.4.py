print("Dies ist ein Programm zur berechnung der Wertsteigerung einer Immobilie bei einem Bestimmten Prozentsatz.")
prozent = int(input("Geben Sie die Prozentuale wertung ihrer Immobilie an:"))/100
wert = 1
jahr = 0
while wert <= 2:
    wert = wert + wert * prozent
    jahr += 1

print("Es dauert", jahr, "Jahre bis die Immobiele doppelt so viel wert ist")
