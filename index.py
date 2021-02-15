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
        print("\nFormule : \nLorem ipsum dolor inpum lorem plor.\n\n")
        esc1 = float(input("1 - Calculer, 2 - Retourner à l'Accueil."))

        if esc1 == 1:
            print("TODO MAKE CALCULATOR SYSTEM")
        if esc1 == 2:
            condensateur()
        else:
            return;

    if condresult == 2:
        Clear()

        print("2 - Charge emmagasinée en Coulomb")
        print("\nFormule : \nLorem ipsum dolor inpum lorem plor.\n\n")
        esc2 = float(input("1 - Calculer, 2 - Retourner à l'Accueil."))

        if esc2 == 1:
            print("TODO MAKE CALCULATOR SYSTEM")
        if esc2 == 2:
            condensateur()
        else:
            return;

    if condresult == 3:
        Clear()

        print("3 - Energie stockée en joules")
        print("\nFormule : \nLorem ipsum dolor inpum lorem plor.\n\n")
        esc3 = float(input("1 - Calculer, 2 - Retourner à l'Accueil."))

        if esc3 == 1:
            print("TODO MAKE CALCULATOR SYSTEM")
        if esc3 == 2:
            condensateur()
        else:
            return;

    if condresult == 4:
        Clear()

        print("4 - Association Parallèle")
        print("\nFormule : \nLorem ipsum dolor inpum lorem plor.\n\n")
        esc4 = float(input("1 - Calculer, 2 - Retourner à l'Accueil."))

        if esc4 == 1:
            print("TODO MAKE CALCULATOR SYSTEM")
        if esc4 == 2:
            condensateur()
        else:
            return;

    if condresult == 5:
        Clear()

        print("5 - Association Série")
        print("\nFormule : \nLorem ipsum dolor inpum lorem plor.\n\n")
        esc5 = float(input("1 - Calculer, 2 - Retourner à l'Accueil."))

        if esc5 == 1:
            print("TODO MAKE CALCULATOR SYSTEM")
        if esc5 == 2:
            condensateur()
        else:
            return;

    if condresult == 6:
        Clear()

        print("6 - Charge d'un condensateur")
        print("\nFormule : \nLorem ipsum dolor inpum lorem plor.\n\n")
        esc6 = float(input("1 - Calculer, 2 - Retourner à l'Accueil."))

        if esc6 == 1:
            print("TODO MAKE CALCULATOR SYSTEM")
        if esc6 == 2:
            condensateur()
        else:
            return;

    if condresult == 7:
        Clear()

        print("7 - Décharge d'un condensateur")
        print("\nFormule : \nLorem ipsum dolor inpum lorem plor.\n\n")
        esc7 = float(input("1 - Calculer, 2 - Retourner à l'Accueil."))

        if esc7 == 1:
            print("TODO MAKE CALCULATOR SYSTEM")
        if esc7 == 2:
            condensateur()
        else:
            return;

    else:
        return;




if result == 1:
    diode()

if result == 2:
    transistor()

if result == 3:
    condensateur()
