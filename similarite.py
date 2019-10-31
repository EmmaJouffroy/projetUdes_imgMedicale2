import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def SSD(I, J):
    """
    Méthode calculant la somme des différences au carré des deux images I et J de même taille
    :param I:
    :param J:
    :return:
    """
    return np.sum((I-J)**2)

def CR(I, J):
    """
    Méthode calculant le coefficient de corrélation de deux images I et J de même taille
    :param I:
    :param J:
    :return:
    """
    return

def IM(I, J):
    """
    Méthode calculant l'information mutuelle entre deux images I et J de même taille
    :param I:
    :param J:
    :return:
    """
    return


if __name__ == '__main__':
    I = np.array(Image.open('Data/I2.jpg'))
    J = np.array(Image.open('Data/J2.jpg'))
    print(SSD(I,J))