import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from numpy.linalg import inv


def interpol(i, j, I):
    i_new = int(np.round(i))
    j_new = int(np.round(j))
    if (i_new < 0) or (i_new >= I.shape[0]):
        i_new = -1
        return i_new, j_new
    if j_new < 0 or j_new >= I.shape[1]:
        i_new = -1
        return i_new, j_new
    return i_new, j_new


def translation(I, p, q):
    new_img = np.zeros((I.shape[0], I.shape[1]))
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            # i,j est le pixel en cours d'analyse
            i_new, j_new = interpol(i+p, j+q, I)
            if i_new != -1:
                new_img[i_new, j_new] = I[i, j]
    return new_img


def two_dimensions_recalage(I, J, iterMax):
    SSD = []
    u = np.array([0, 0])
    J2 = J
    for i in range(0, iterMax):
        J2 = translation(J2, u[0], u[1])
        SSD.append(np.sum((J2-I)**2))
        J2x = np.gradient(J2, axis=0)
        J2y= np.gradient(J2, axis=1)
        Jt = J2 - I

        J2x_ss = np.sum(J2x**2)
        J2y_ss = np.sum(J2y**2)
        J2yx = np.sum(J2x * J2y)
        J2xt = np.sum(J2x * Jt)
        J2yt = np.sum(J2y * Jt)
        M = np.array(([J2x_ss, J2yx], [J2yx, J2y_ss]))
        b = np.array(([J2xt], [J2yt]))
        u = u + np.squeeze(np.linalg.solve(M, b), axis=1)
        print(SSD[-1])
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2

if __name__ == '__main__':
    I = np.array(Image.open('Data/BrainMRI_1.jpg'))
    J = np.array(Image.open('Data/BrainMRI_2.jpg'))
    plt.figure()
    plt.imshow(two_dimensions_recalage(I, J, 500))
    plt.figure()
    plt.imshow(I)
    plt.show()

