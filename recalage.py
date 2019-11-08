import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformation_interpolations import translation_scipy, rotation_scipy, translation
from scipy import ndimage
import math


def lucas_kanade_recalage(I, J, iterMax):
    """

    :param I:
    :param J:
    :param iterMax:
    :return:
    """
    SSD = []
    u = np.array([0, 0])
    J2 = translation_scipy(J, u)
    for i in range(0, iterMax):
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
        print(M)
        b = np.array(([J2xt], [J2yt]))
        u = u - np.squeeze(np.linalg.solve(M, b), axis=1)
        print(u)
        J2 = translation_scipy(J, u)
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2



# def recalage_test(I, J, lamb):


def gradient_descent_translation_recalage(I, J, iterMax, lamb):
    SSD = []
    u = np.array([0, 0])
    J2 = J
    J2 = translation_scipy(J2, u)
    J_derivate_x = np.gradient(J, axis=0)
    J_derivate_y = np.gradient(J, axis=1)
    for i in range(1, iterMax):
        error = J2 - I
        SSD.append((np.sum(error)**2))
        J2_derivate_xp = translation_scipy(J_derivate_x, u)
        J2_derivate_yp = translation_scipy(J_derivate_y, u)
        print((error*J2_derivate_xp).shape)
        ssd_p = 2 * np.sum(error*J2_derivate_xp)
        ssd_q = 2 * np.sum(error*J2_derivate_yp)
        u = u + [(lamb/i) * ssd_p, (lamb/i) * ssd_q]
        J2 = translation_scipy(J, u)
        print(u)
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2


def rotation_recalage(I, J, iterMax, lamb):
    SSD = []
    theta = 0
    J2 = J
    for i in range(0, iterMax):
        J2 = rotation_scipy(J2, theta)
        SSD.append(np.sum((J2-I)**2))
        J2x = np.gradient(J2, axis=0)
        J2y= np.gradient(J2, axis=1)
        error = J2 - I
        cnt = 0
        for x in range(J2.shape[0]):
            for y in range(J2.shape[1]):
                x_p = int(np.ceil(x*np.cos(theta)-y*np.sin(theta)))
                y_p = int(np.ceil(x * np.sin(theta) + y * np.cos(theta)))
                if (x_p < 0) & (x_p > J2.shape[0]-1):
                    if (y_p < 0) & (y_p > J2.shape[1]-1):
                        res1 = J2x[x_p, y_p] * ((- x * np.sin(theta)) - (y * np.cos(theta)))
                        res2 = J2y[x_p, y_p] * ((x * np.cos(theta)) - (y * np.sin(theta)))
                        cnt = cnt + error[x, y] * (res1 + res2)
        ssd_d = 2 * cnt
        theta = theta - lamb * ssd_d
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2


if __name__ == '__main__':
    I = np.array(Image.open('Data/BrainMRI_1.jpg')).astype(np.int32)
    J = np.array(Image.open('Data/BrainMRI_2.jpg')).astype(np.int32)
    I = I / np.amax(I)
    J = J / np.amax(J)
    # J = rotation(I, 5)
    plt.figure()
    plt.imshow(gradient_descent_translation_recalage(I, J, 3000, 0.1))
    plt.title("image recalée")
    plt.figure()
    plt.title("image de base")
    plt.imshow(I)
    plt.colorbar()
    plt.show()

