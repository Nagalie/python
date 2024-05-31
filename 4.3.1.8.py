from random import randint
found = 1
tries = 0

while found == 1:
    Würfel = randint(1, 6)
    
    if Würfel == 6:
        break

    tries += 1

print(tries)