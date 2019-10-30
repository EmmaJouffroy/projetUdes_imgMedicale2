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
    # On trouve d'abbord la plage de valeurs conjointes
    intensiteI_min = I.amin()
    intensiteJ_min = J.amin()


if __name__ == '__main__':
    I = np.array(Image.open('Data/I1.png'))
    print(type(I))
    plt.imshow(I)
    plt.show()

