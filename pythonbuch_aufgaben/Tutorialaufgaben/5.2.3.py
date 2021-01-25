print("Dies ist ein Programm, welches dazu dient herrauszufinden ob ein Jahr ein Schaltjahr ist.")
jahr = int(input("Gib hier das gesuchte Jahr ein:"))
if jahr % 4 == 0:
    if jahr % 100 != 0:
        print("Das Jahr", jahr, "ist ein Schaltjahr")
    else:
        if jahr % 400 == 0:
            print("Das Jahr", jahr, "ist ein Schaltjahr")
        else:
            print("Das Jahr", jahr, "ist kein Schaltjahr")
else:
    print("Das Jahr", jahr, "ist kein Schaltjahr")