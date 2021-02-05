def add_function(f, g):
    return int(f) + int(g)
f = lambda f: f**2
g = lambda g: g**2
print(add_function(f(2), g(3)))
print(add_function(f(5), f(7)))
