import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from histogramme import jointHist


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
    mean_I = np.mean(I)
    mean_J = np.mean(J)
    centered_I = I - mean_I
    centered_J = J - mean_J
    num = np.sum(centered_I*centered_J)
    denom = np.sqrt(np.sum(centered_I**2))*np.sqrt(np.sum(centered_J**2))
    return num / denom


def IM(hist):
    """
    Méthode calculant l'information mutuelle entre deux images I et J de même taille
    A partir de leur histogramme conjoint
    :param hist:
    :return:
    """
    hist = hist / float(np.sum(hist))
    # probabilité d'avoir x dans un vecteur
    px = np.sum(hist, axis=1)
    px = np.expand_dims(px, axis=0)
    # probabilité d'avoir y dans un vecteur
    py = np.sum(hist, axis=0)
    py = np.expand_dims(py, axis=1)
    # Ici je ne comprends pas, comment ça fonctionne ?
    px_py = np.dot(px.T, py.T)
    # Pour ne pas avoir de problème on garde uniquement les valeurs différentes de 0
    nzs = hist > 0
    mutual_info = np.sum(hist[nzs] * np.log(hist[nzs] / px_py[nzs]))
    return mutual_info

if __name__ == '__main__':
    I = np.array(Image.open('Data/I2.jpg'))
    J = np.array(Image.open('Data/J2.jpg'))
    hgram = jointHist(I, J, 10)
    print(IM(hgram))
