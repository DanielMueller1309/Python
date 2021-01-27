print("ich nehme ihre worte und sortiere diese.")
anzahl = int(input("geben sie die Anzahl der worte ein die sie eintragen wollen:"))
worte = []
for i in range(anzahl):
    worte.append(str(input("Wort" + str(i+1) + ":")))
worte.sort(key=str.lower)
print(worte)

"""

# Python program to sort a list of strings

lst = ['Zweck', 'Entflammen', 'Schneiden', 'Granit', 'Gewinn', 'Schubkarre']

# Using sorted() function
for ele in sorted(lst):
    print(ele)

print("")
# Python program to sort a list of strings

lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']

# Using sorted() function
for ele in sorted(lst):
    print(ele)
"""
