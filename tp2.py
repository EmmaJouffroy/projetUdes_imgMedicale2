from histogramme import test_afficher_histogramme, test_joint_histogramme
from transformation import *
from similarite import test_afficher_similarites
from transformation_interpolations import *
import sys


if __name__ == '__main__':

    if int(sys.argv[1]) == 1:
        # lancer construction histogramme
        if len(sys.argv) == 2:
            # Pas de paramètre donc affichage de tous les couples:
            print("Patientez quelques instants")
            test_afficher_histogramme()
        elif len(sys.argv) == 3:
            if int(sys.argv[2]) < 7:
                test_joint_histogramme(int(sys.argv[2]))
            else:
                print("Pour lancer la question 1, suivre l'usage suivant:")
                print("python tp2.py 1 NumeroDuCouple")
                print("Les couples sont indexes de 1 à 6")
    elif int(sys.argv[1]) == 2:
        # lancer les tests des fonctions de similarité
        print("Patientez, les images comparées s'afficheront et les résulats des différentes mesures de similarité "
              "seront affichés dans la console.")
        test_afficher_similarites()
    elif int(sys.argv[1]) == 3:
        # lancer l'affichage d'une transformation
        if len(sys.argv) > 2:
            if sys.argv[2] == "transrigide":
                if len(sys.argv) == 9:
                    theta = int(sys.argv[3])
                    omega = int(sys.argv[4])
                    phi = int(sys.argv[5])
                    p = int(sys.argv[6])
                    q = int(sys.argv[7])
                    r = int(sys.argv[8])
                    test_transrigide(theta, omega, phi, p, q, r)
                else:
                    print("Pour lancer la transformation rigide de la question 3, suivre l'usage suivant:")
                    print("python tp2.py 3 transrigide theta omega phi p q r")
            elif sys.argv[2] == "similitude":
                if len(sys.argv) == 10:
                    s = float(sys.argv[3])
                    theta = float(sys.argv[4])
                    omega = float(sys.argv[5])
                    phi = float(sys.argv[6])
                    p = float(sys.argv[7])
                    q = float(sys.argv[8])
                    r = float(sys.argv[9])
                    test_similitude(s, theta, omega, phi, p, q, r)
                else:
                    print("Pour lancer la transformation similitude de la question 3, suivre l'usage suivant:")
                    print("python tp2.py similitude s theta omega phi p q r")
                    print("ex: python tp2.py 3 similitude 0.5 45 45 20 5 5 10")
            elif sys.argv[2] == "choixMatrice":
                if len(sys.argv) > 3:
                    test_similitude(0, 0, 0, 0, 0, 0, 0, int(sys.argv[3]))
                else:
                    print("Pour tester l'effet des matrices M1, M2, M3 de la question 3, suivre l'usage suivant:")
                    print("python tp2.py choixMatrice numMatrice")
        else:
            print("Pour lancer la question 3, suivre l'usage prévu pour chaque sous question")
            print("ex : python tp2.py 3 similitude 1.5 90 0 0 5 5 5")
    elif int(sys.argv[1]) == 4:
        print('allo')
