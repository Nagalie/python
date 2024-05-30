print("Gebe 10 Zahlen ein: ")

def Eingaben():
    liste = []
    for i in range(1, 11):
        eingabe = int(input())
        liste.append(eingabe)
    return liste

Eingaben()
print(liste)

def Bubblesort(liste):
    for i in range(len(liste)):
        for a in range(0, len(liste) - i - 1):
            if liste[a] > liste[a+1]:
                Tausch = liste[a]
                liste[a] = liste[a+1]
                liste[a+1] = Tausch
    return liste

Bubblesort(liste)
print(liste)