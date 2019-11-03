import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
from PIL import Image


def interpol(i, j, I):
    i_new = np.round(i)
    j_new = np.round(j)
    if i_new < 0 or i_new >= I.shape[0]:
        i_new = -1
        return i_new, j_new
    if j_new < 0 or j_new >= I.shape[1]:
        i_new = -1
        return i_new, j_new
    return i_new, j_new


def translation(I, p, q):
    new_img = np.zeros((I.shape[0], I.shape[1]))
    print(new_img.shape)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            # i,j est le pixel en cours d'analyse
            i_new, j_new = interpol(i+p, j+q, I)
            if i_new != -1:
                new_img[i_new, j_new] = I[i, j]
    return new_img

if __name__ == '__main__':
    I = np.array(Image.open('Data/I6.jpg'))
    plt.figure()
    plt.imshow(translation(I, 190, 190))
    plt.figure()
    plt.imshow(I)
    plt.show()

