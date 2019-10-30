import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def JointHist(I, J, bin):
    """

    :param I: np.array()
    :param J: np.array()
    :param bin: Nombre de classes
    :return:
    """
    # On cherche les valeurs d'intensités maximales des deux images
    i_max = np.amax(I)
    j_max = np.amax(J)

    # On cherche le nombre de classes sur l'axe x pour I et y pour J
    # en divisant par le nombre de bin définis l'intensité maximale trouvée
    nb_bin_i = int(round(i_max / bin))+1
    nb_bin_j = int(round(j_max / bin))+1

    # On crée un np.array de la taille du nombre de classes
    # définies
    hist = np.zeros((nb_bin_i, nb_bin_j)).astype(int)

    # On parcours notre image I et on cherche dans quel bin il se trouve le voxel(i,j)
    # On fait de même pour l'image J, et on incrémente notre histogramme de cette façon
    for i in range(0, I.shape[0]):
        for j in range(0, I.shape[1]):
            bin_i = int(I[i, j]/bin)
            bin_j = int(J[i, j]/bin)
            hist[bin_i, bin_j] += 1

    # On affiche l'image de l'histogramme conjoint
    plt.suptitle('Histogramme conjont', fontsize=12)
    plt.imshow(hist, cmap='winter')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    bin = 20
    I = np.array(Image.open('Data/BrainMRI_1.jpg'))
    J = np.array(Image.open('Data/BrainMRI_2.jpg'))
    JointHist(I, J, bin)
    plt.show('Data/BrainMRI_1.jpg')


