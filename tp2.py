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
                print("python main.py 1 NumeroDuCouple")
                print("Les couples sont indexes de 1 à 6")
    elif int(sys.argv[1]) == 2:
        # lancer les tests des fonctions de similarité
        print("Patientez, les images comparées s'afficheront et les résulats des différentes mesures de similarité "
              "seront affichés dans la console.")
        test_afficher_similarites()
    elif sys.argv[1] == 3:
        # lancer l'affichage d'une transformation
        print('allo')
    elif sys.argv[1] == 4:
        print('allo')
