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
    i_max = np.amax(I)
    j_max = np.amax(J)
    nb_bin_i = int(round(i_max / bin))
    nb_bin_j = int(round(j_max / bin))
    hist = np.zeros((nb_bin_i+1, nb_bin_j+1)).astype(int)
    for i in range(0, I.shape[0]):
        for j in range(0, I.shape[1]):
            bin_i = int(I[i, j]/bin)
            bin_j = int(J[i, j]/bin)
            hist[bin_i, bin_j] += 1
    plt.suptitle('Histogramme conjont', fontsize=12)
    plt.imshow(hist, cmap='winter')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    bin = 2
    I = np.array(Image.open('Data/I1.png'))
    J = np.array(Image.open('Data/I1.png'))
    JointHist(I, J, bin)


