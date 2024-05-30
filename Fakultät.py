Fakultät = input("Bitte geben Sie eine Zahl ein die Sie Fakultieren wollen: ")

Zahl = 1

for i in range(1, 1 + int(Fakultät)):
    Zahl *= i

print("Die Fakultät von " + str(Fakultät) + " ist " + str(Zahl) + ".")