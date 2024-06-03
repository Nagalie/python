from tkinter import *

root = Tk()

def GUI():
    Login = "LOGIN"
    Loginmsg = "Bitte geben Sie Ihre Login Daten ein."
    Text(root, text = Login)

def Auswählen():
    Auswahl = input("Registrieren(1) oder Einloggen(0)")
    return Auswahl

def Datenbank():   
    return []

def Registrierung(Array):
    print("Registrierung")
    RegName = input("Geben Sie bitte Ihren Namen ein mit dem Sie sich Registrieren wollen: ")
    RegPasswort = input("Bitte geben Sie Ihre Passwort ein: ")
    Array.append((RegName, RegPasswort))

def Einlog(Array):
    Versuch = 1
    Zugang = False

    while Zugang == False:
        Name = input("Name: ")
        Passwort = input("Passwort: ")

        for Regname, Regpasswort in Array:

            if Name == Regname and Passwort == Regpasswort:
                print("Erfolgreich eingeloggt!")
                Zugang = True

            else:
                print(f"Falsche zugangsdaten. {Versuch}. Versuch.")
                Zugang = False
                Versuch += 1

Array = Datenbank()
Auswahl = Auswählen()

if Auswahl == "0":
    GUI()
    Einlog(Array)

elif Auswahl == "1":
    Registrierung(Array)
    GUI()
    Einlog(Array)

else:
    print("Ungültige eingabe.")