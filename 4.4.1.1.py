#Wörter und Buchstaben zählen

Satz = input("Geben Sie einen Satz ein: ")

Satzsplit = Satz.split()
temp = 0

print(f"Wörter: {len(Satzsplit)}")

for i in range(0, len(Satzsplit)):
    a = len(Satzsplit[i])
    temp += a

print(f"Buchstaben: {temp}")

for j in range(0, len(Satzsplit)):
    a = len(Satzsplit[i].isupper())
    temp += a

print(f"Großbuchstaben: {temp}")