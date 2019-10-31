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

def IM(I, J):
    """
    Méthode calculant l'information mutuelle entre deux images I et J de même taille
    :param I:
    :param J:
    :return:
    """
    hist = jointHist(I, J, bin=100)
    # Pour avoir les histogramme de I et J on utilise la même fonction et on ne considérera que la diagonale:
    histJ = jointHist(J, J, bin=100)
    histI = jointHist(I, I, bin=100)
    IM = 0
    for i in range(100):
        for j in range(100):
            IM += hist[i, j] * (np.log2(hist[i, j]/(histI[i, i]*histJ[j, j])))
    return IM


if __name__ == '__main__':
    I = np.array(Image.open('Data/I2.jpg'))
    J = np.array(Image.open('Data/J2.jpg'))
    print(IM(I, J))
