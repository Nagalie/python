wortzahl = input("Wie viele Wörter willst du eingeben?: ")

liste = []
for eingabe in range(int(wortzahl)):
    eingabe = input("Wort: ")
    liste.append(eingabe)

print(liste)