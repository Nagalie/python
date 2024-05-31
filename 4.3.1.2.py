zahl = [4, 5, 7, 11, 21]
i = 0
a = 0

while a < 5:
    summe = zahl[i] + 2
    print("Wenn ich zu " + str(zahl[i]) + " zwei addiere, erhalte ich " + str(summe) + ".")
    i += 1
    a += 1

print("Fertig")