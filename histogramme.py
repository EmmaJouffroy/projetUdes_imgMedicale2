import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def jointHist(I, J, bin):
    """
    Méthode permettant la création d'un histogramme joint possèdant bin classes entre 2 images de même taille
    :param I: np.array()
    :param J: np.array()
    :param bin: Nombre de classes
    :return:
    """
    # On vérifie que les images partagent bien la même taille
    assert I.shape == J.shape
    # On cherche les valeurs d'intensités maximales des deux images:
    max = np.max(np.array([np.amax(I), np.amax(J)]))
    # On crée un histogramme vide carré de taille bin (ie de taille nombre de classes):
    hist = np.zeros((bin, bin)).astype(int)
    nb_val_per_bin = round(max / bin)
    # On parcourt en même temps les images I et J et on cherche dans quel bin se trouve le pixel(i,j)
    # de chaque image:
    for i in range(0, I.shape[0]):
        for j in range(0, I.shape[1]):
            bin_i = int(I[i, j] // nb_val_per_bin)
            if(bin_i > bin):
                bin_i = bin - 1
            bin_j = int(J[i, j] // nb_val_per_bin)
            if(bin_j > bin):
                bin_j = bin - 1
            hist[bin_i, bin_j] += 1
    return hist


if __name__ == '__main__':
    bin = 20
    I = np.array(Image.open('Data/I6.jpg'))
    J = np.array(Image.open('Data/J6.jpg'))
    hist = jointHist(I, J, bin)
    print("La somme de toutes les classes de l'histogramme est bien égale au nombre de pixels dans chaque image : {}.".
          format(np.sum(hist) == I.shape[0] * I.shape[1]))
    # On affiche l'image de l'histogramme conjoint
    plt.title('Histogramme conjont des images I6 et J6', fontsize=12)
    plt.imshow(hist, cmap='gray')
    plt.colorbar()
    plt.show()



