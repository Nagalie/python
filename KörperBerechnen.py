from random import randint
from math import sqrt

print("QUADER BERECHNUNG:")
print(" ")

def Eingabe1():
    print("Bitte geben Sie die Länge ein: ")
    Länge = float(input())
    return Länge

Input1 = Eingabe1()

def Eingabe2():
    print("Bitte geben Sie die Breite ein: ")
    Breite = float(input())
    return Breite

Input2 = Eingabe2()

def Eingabe3():
    print("Bitte geben Sie die höhe ein: ")
    höhe = float(input())
    return höhe

Input3 = Eingabe3()

def Berechnen1(Input1, Input2):
    Diagonale = sqrt(Input1 ** 2 + Input2 ** 2)
    print("Die erste Diagonale ist " + str(Diagonale) + " groß.")
    return Diagonale

result1 = Berechnen1(Input1, Input2)

def Berechnen2(Input1, Input3):
    Diagonale = sqrt(Input1 ** 2 + Input3 ** 2)
    print("Die zweite Diagonale ist " + str(Diagonale) + " groß.")
    return Diagonale

result2 = Berechnen2(Input1, Input3)

def Berechnen3(Input2, Input3):
    Diagonale = sqrt(Input2 ** 2 + Input3 ** 2)
    print("Die dritte Diagonale ist " + str(Diagonale) + " groß.")
    return Diagonale

result3 = Berechnen3(Input2, Input3)

def Berechnen4(Input1, Input2, Input3):
    Raumdiagonale = sqrt(Input1 ** 2 + Input2 ** 2 + Input3 ** 2)
    print("Das heißt die Raumdiagonale ist " + str(Raumdiagonale) + " groß.")

result4 = Berechnen4(Input1, Input2, Input3)