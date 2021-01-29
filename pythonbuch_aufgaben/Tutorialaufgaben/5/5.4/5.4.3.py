zahl = int(input("Gib eine max Zahl ein:"))
"""
for i in range(20, zahl+1):
    p = 0
    j = 2
    while j in range(10):
        if i % j == 0:
            p += 1
        j += 1
    if p == 1:
        print(i)
"""
liste = [2, 3, 5, 7]

for i in range(2, zahl+1):
    p = 0
    for j in range(4):
        if i % liste[j] == 0:
            p += 1
            if i == liste[j]:
                p -= 1
    if p == 0:
        print(i)

"""
for i in range(2, zahl+1):
    p = 0
    if i % 2 == 0:
        p += 1
        if i == 2:
            p -= 1
    elif i % 3 == 0:
        p += 1
        if i == 3:
            p -= 1
    elif i % 5 == 0:
        p += 1
        if i == 5:
            p -= 1
    elif i % 7 == 0:
        p += 1
        if i == 7:
            p -= 1
    if p == 0:
        print(i)
"""
