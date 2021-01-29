satz = input("Geben Sie einen Satz ein:")
print("Wortanzahl:", len(satz.split()))
print("Buchstabenanzahl:", len("".join(satz.split())))
i = 0
for b in "".join(satz.split()):
    if b.isupper():
        i += 1
print("Großbuchstabenanzahl:", i)
