einzahlung = float(input("Fester Jahresbetrag: "))
Zinssatz = float(input("Gebe den Zinssatz ein: "))
Wunschbetrag = float(input("Gebe deinen Betrag ein den du erreichen willst: "))

aktueller_betrag = 0.0
jahre = 0

while aktueller_betrag <= Wunschbetrag:
    aktueller_betrag += einzahlung
    aktueller_betrag += aktueller_betrag * (Zinssatz / 100)
    jahre+=1

print(f"{aktueller_betrag:.2f} Jahre: {jahre}")