n = int(input("Geben Sie eine Zahl an"))
versuche = 0

while n > 1:
    if n % 2 == 0:
        n = n/2
    else:
        n = n* 3
        n = n+1
    versuche += 1

print(f"{versuche} Durchgänge musste man durchgehen um an die 1 zu kommen.")