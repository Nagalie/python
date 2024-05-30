while True:
    eingabe = input("Geben Sie eine Zahl ein: ")

    zahl = int(eingabe)

    if zahl<10:
        print("Deine Zahl ist kleiner 10")
    else:
        print("Deine Zahl ist größer als 10")

    erneut = input("Nochmal? (J/N)")

    if erneut == "N":
        break

print("Auf Wiedersehen")