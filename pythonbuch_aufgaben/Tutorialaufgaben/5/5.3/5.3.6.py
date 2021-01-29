print("Wir berechnen ihr Kapital")
sparbetrag = float(input("Welchen Betrag legen Sie Jährlich zurück? Betrag:"))
zinsen = float(input("Wie hoch ist der Zinssatz? Satz:"))/100
ziel = float(input("Bis wohin soll gespart werden? Betrag:"))
jahre = 1
guthaben = sparbetrag + sparbetrag*zinsen
while guthaben <= ziel:
    guthaben += (guthaben + sparbetrag)*zinsen
    jahre += 1
print("Es dauert", jahre, "Jahre bis der gewünschte betrag erreicht ist")
