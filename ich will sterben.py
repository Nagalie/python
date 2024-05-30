liste = ['Schwalbe', 'Kokosnuss', 13, 'Spam', 3.14]
liste[2] = 666

print(liste)
len(liste)
print(liste)

liste.append('Ni')
print(liste)

liste.extend([4, 5, 3.14])
print(liste)

liste.insert(2, 'Taube')
print(liste)

print(liste.count(3.14))

print(liste.index(3.14))

print(liste.remove(3.14))

liste.pop()

print(liste)

liste.reverse()

print(liste)

print(sum([1, 3, 5]))

print(liste)

liste_a = ['Hallo', 'schönes', 'Wetter']
liste_b = liste_a
liste_b[1] = 'schlechtes'
print(liste_a[0], liste_a[1], liste_a[2])
