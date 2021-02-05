class Person:
    pass

dummy = Person()
dummy.name = "Müller"
dummy.vorname = "Jürg"

print(dummy.vorname, dummy.name)
x = dummy
x.vorname = "Gido"
print(dummy.vorname, dummy.name)
