def Array():
    Unsort = [1, 4, 3, 3, 5, 7, 2]
    print(Unsort)
    return Unsort

Unsort= Array()

def bubblesort(Unsort):
    for a in range(len(Unsort)):
        for i in range(0, len(Unsort)-a-1):
            if Unsort[i] > Unsort[i+1]:
                temp = Unsort[i]
                Unsort[i] = Unsort[i+1]
                Unsort[i+1] = temp
    print(Unsort)

bubblesort(Unsort)