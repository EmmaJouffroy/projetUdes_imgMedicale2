from histogramme import test_afficher_histogramme, test_joint_histogramme
from transformation import *
from similarite import *
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
    elif sys.argv[1] == 2:
        print('allo')
    elif sys.argv[1] == 3:
        print('allo')
    elif sys.argv[1] == 4:
        print('allo')
