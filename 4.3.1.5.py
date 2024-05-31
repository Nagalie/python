Preis = int(input("Bitte geben Sie den Einkaufspreis der Maschine ein: "))
Jahre = int(input("Bitte geben Sie die Jahre ein die linear abgeschrieben werden."))

Zahlung = Preis / Jahre

for jahr in range(1, Jahre + 1):
    restwert = Preis - (Zahlung * jahr)
    print("Jahr " +jahr + ": " + restwert)