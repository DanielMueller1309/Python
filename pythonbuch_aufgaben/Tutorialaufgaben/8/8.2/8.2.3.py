class Person:
  pass

class Auto:
  pass

dummy = Person()
my_car = Auto()
my_car.marke = "Seat"
dummy.car = my_car
print(dummy.car.marke)