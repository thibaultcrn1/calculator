from sys import platform as _platform
import subprocess


def Clear():
    if _platform == 'win32':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)


def home():
    print("[------------------------------------------]")
    print(" -              Calculator                - ")
    print("[------------------------------------------]")

    print("\n1 - Diode \n2 - Transistor\n3 - Condensateur\n")


home()
result = float(input("Syntaxe : < 1, 2, 3 > "))


def diode():
    Clear()

    print("[------------------------------------------]")
    print(" -                 Diode                  - ")
    print("[------------------------------------------]")


def transistor():
    Clear()

    print("[------------------------------------------]")
    print(" -              Transistor                - ")
    print("[------------------------------------------]")


def condensateur():
    Clear()

    print("[------------------------------------------]")
    print(" -             Condensateur               - ")
    print("[------------------------------------------]")

    print("\n1 - Capacité d'un condensateur")
    print("2 - Charge emmagasinée en Coulomb")
    print("3 - Energie stockée en joules")
    print("4 - Association Parallèle")
    print("5 - Association Série")
    print("6 - Charge d'un condensateur")
    print("7 - Décharge d'un condensateur")

    condresult = float(input("Quel section ? (Syntaxe : 1, 2, 3, 4...) "))

    if condresult == 1:
        Clear()

        print("1 - Capacité d'un condensateur")

    if condresult == 2:
        Clear()

        print("2 - Charge emmagasinée en Coulomb")

    if condresult == 3:
        Clear()

        print("3 - Energie stockée en joules")

    if condresult == 4:
        Clear()

        print("4 - Association Parallèle")

    if condresult == 5:
        Clear()

        print("5 - Association Série")

    if condresult == 6:
        Clear()

        print("6 - Charge d'un condensateur")

    if condresult == 7:
        Clear()

        print("7 - Décharge d'un condensateur")
        print("\nFormule : \nLorem ipsum dolor inpum lorem plor.\n\n")
        esc7 = float(input("1 - Calculer, 2 - Retourner à l'Accueil."))

    else:
        return;




if result == 1:
    diode()

if result == 2:
    transistor()

if result == 3:
    condensateur()
