from histogramme import test_afficher_histogramme, test_joint_histogramme
from transformation import *
from similarite import test_afficher_similarites
from transformation_interpolations import test_rotation_scipy, test_rotation_nn, test_translation_bilineaire, \
     test_translation_scipy
from recalage import test_lucas_kanade_recalage, test_translation_recalage, test_rotation_recalage, \
    test_iconique_recalage
import sys

if __name__ == '__main__':
    if len(sys.argv) > 0:
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
            # On test tout d'abord si l'on souhaite utiliser ou non scipy
            if len(sys.argv) > 2:
                if int(sys.argv[2]) == 1:
                    if len(sys.argv) > 3:
                        if sys.argv[3] == "rotation":
                            if len(sys.argv) > 4:
                                test_rotation_scipy(float(sys.argv[4]))
                            else:
                                print("Pour une rotation avec scipy ajouter un angle en degres")
                                print("ex python tp2.py 4 1 rotation 45")
                        elif sys.argv[3] == "translation":
                            if len(sys.argv) > 5:
                                test_translation_scipy(float(sys.argv[4]), float(sys.argv[5]))
                            else:
                                print("Pour une translation avec scipy ajouter deux elements de translation x et y")
                                print("ex python tp2.py 4 1 translation 5 5")
                        else:
                            print("Pour une transformation avec scipy ajouter type de transformation")
                            print("ex python tp2.py 4 1 rotation 45")
                elif int(sys.argv[2]) == 0:
                    if len(sys.argv) > 3:
                        if sys.argv[3] == "rotation":
                            if len(sys.argv) > 4:
                                test_rotation_scipy(float(sys.argv[4]))
                            else:
                                print("Pour une rotation sans scipy ajouter un angle en degres")
                                print("ex python tp2.py 4 0 rotation 45")
                        elif sys.argv[3] == "translation":
                            if len(sys.argv) > 5:
                                test_translation_scipy(float(sys.argv[4]), float(sys.argv[5]))
                            else:
                                print("Pour une translation sans scipy ajouter deux elements de translation x et y")
                                print("ex python tp2.py 4 0 translation 5 5")
                        else:
                            print("Pour une transformation sans scipy ajouter type de transformation")
                            print("ex python tp2.py 4 0 rotation 45")
                else:
                    print("Pour lancer la question 4, suivre l'usage suivant:")
                    print("utilisation de scypi 1 avec, 0 sans")
                    print("ex python tp2.py 4 1 rotation 45")
            else:
                print("Pour lancer la question 4, suivre l'usage suivant:")
                print("python tp2.py 4 scipy typeTransformation paramsTransform")
                print("ex python tp2.py 4 1 rotation 45")
        elif int(sys.argv[1]) == 5:
            if len(sys.argv) > 2:
                if sys.argv[2] == 'lucasKanade':
                    if len(sys.argv) > 3:
                        test_lucas_kanade_recalage(sys.argv[3])
                    else:
                        test_lucas_kanade_recalage()
                elif sys.argv[2] == 'translationGD':
                    if len(sys.argv) > 4:
                        test_translation_recalage(int(sys.argv[3]), float(sys.argv[4]))
                    else:
                        test_translation_recalage()
                elif sys.argv[2] == 'rotationGD':
                    if len(sys.argv) > 4:
                        test_rotation_recalage(int(sys.argv[3]), float(sys.argv[4]))
                    else:
                        test_rotation_recalage()
                elif sys.argv[2] == 'iconiqueGD':
                    if len(sys.argv) > 4:
                        test_iconique_recalage(int(sys.argv[3]), float(sys.argv[4]))
                    else:
                        test_iconique_recalage()
                else:
                    print("Pour lancer la question 5 de recalage veuillez suivre l'usage \n")
                    print("ex python tp2.py 5 iconiqueGD 10000 0.0000001")
            else:
                print("Pour lancer la question 5 de recalage veuillez suivre l'usage \n")
                print("ex python tp2.py 5 iconiqueGD 10000 0.0000001")
    else :
        print("Chacune des questions du devoir peuvent être lancées grâce à ce script")
        print("Il suffit de commencer par : python tp2.py numQuestion")
        print("Une aide est affichée pour passer les arguments attendus")
