from random import randint

Würfel1 = randint(1, 6)
Würfel2 = randint(1, 6)
Würfel3 = randint(1, 6)

Würfel = Würfel1, Würfel2, Würfel3
print(Würfel)
print("Summe der Würfel: ")
print(sum(Würfel))