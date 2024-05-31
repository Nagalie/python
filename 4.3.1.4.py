prozent = float(input("Bitte geben Sie den jährlichen Prozentsatz der Wertsteigerung ein: "))
anfangswert = float(input("Bitte geben Sie den Anfangswert der Immobilie ein: "))

zielwert = anfangswert * 2
jahre = 0

while anfangswert <= zielwert:
    anfangswert += anfangswert * (prozent / 100)
    jahre += 1

print("Es dauert " + str(jahre) + " Jahre, bis der Wert der Immobilie mehr als doppelt so groß ist wie der Anfangswert.")