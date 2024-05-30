Variable = 0
print("Welche Zeitangabe haben Sie? (S = Stunde, m = minuten, s = sekunden): ")
Zeit = input()

print("Wie viele " + Zeit + " haben Sie?: ")
ZeitZahl = input()


if Zeit == "S":
    #minuten
    StundenMinuten = float(ZeitZahl) * 60
    #sekunden
    StundenSekunden = float(StundenMinuten) * 60

    print("Minuten: " + str(StundenMinuten))
    print("Sekunden: "+ str(StundenSekunden))
elif Zeit == "m":
    #Stunden
    MinutenStunden = float(ZeitZahl) / 60
    #sekunden
    MinutenSekunden = float(ZeitZahl) * 60

    print("Stunden: " + str(MinutenStunden))
    print("Sekunden: " + str(MinutenSekunden))
elif Zeit == "s":
    SekundenMinuten = float(ZeitZahl) / 60
    SekundenStunden = float(SekundenMinuten) / 60

    print("Stunden: " + str(SekundenStunden))
    print("Minuten: " + str(SekundenMinuten))
    