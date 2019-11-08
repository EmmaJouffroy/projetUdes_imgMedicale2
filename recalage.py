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
    # J2 = translation_scipy(J, u)
    J2 = ndimage.interpolation.shift(J, u)
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
        b = np.array(([J2xt], [J2yt]))
        u = u + np.squeeze(np.linalg.solve(M, b), axis=1)
        print(u)
        J2 = ndimage.interpolation.shift(J, u)
        # J2 = translation_scipy(J, u)
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2


def gradient_descent_translation_recalage(I, J, iterMax, lamb):
    SSD = []
    u = np.array([0, 0])
    J2 = J
    J2 = translation_scipy(J, u)
    J_derivate_x = np.gradient(J, axis=1)
    J_derivate_y = np.gradient(J, axis=0)
    evol_lamb = [lamb]
    for i in range(1, iterMax):
        error = J2 - I
        SSD.append((np.sum(error**2)))
        J2_derivate_xp = translation_scipy(J_derivate_x, u)
        J2_derivate_yp = translation_scipy(J_derivate_y, u)
        print((error*J2_derivate_xp).shape)
        ssd_p = 2 * np.sum(error*J2_derivate_xp)
        ssd_q = 2 * np.sum(error*J2_derivate_yp)
        u = u + [(lamb/i) * ssd_p, (lamb/i) * ssd_q]
        J2 = translation_scipy(J, u)
        print(u)
        evol_lamb.append(lamb/i)
    plt.figure()
    plt.plot(SSD)
    plt.figure()
    plt.plot(evol_lamb)
    plt.show()
    return J2


def rotation_recalage(I, J, iterMax, lamb):
    SSD = []
    theta = 0
    J2 = rotation_scipy(J, theta)
    J_derivate_x = np.gradient(J, axis=0)
    J_derivate_y = np.gradient(J, axis=1)
    x, y = np.meshgrid(range(I.shape[0]), range(I.shape[1]))
    # theta = np.deg2rad(theta)
    for i in range(1, iterMax):
        error = J2 - I
        SSD.append(np.sum(error**2))
        J2_derivate_xp = rotation_scipy(J_derivate_x, theta)
        J2_derivate_yp = rotation_scipy(J_derivate_y, theta)
        res1 = J2_derivate_xp * ((- x * np.sin(theta)) - (y * np.cos(theta)))
        res2 = J2_derivate_yp * ((x * np.cos(theta)) - (y * np.sin(theta)))
        ssd_d = 2 * np.sum((error*(res1 + res2)))
        theta = theta - (lamb * ssd_d)
        J2 = rotation_scipy(J, theta)
        print(np.rad2deg(theta))
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2


if __name__ == '__main__':
    I = np.array(Image.open('Data/BrainMRI_3.jpg'))
    # J = np.array(Image.open('Data/BrainMRI_4.jpg'))
    J = rotation_scipy(I, np.deg2rad(15))
    I = ndimage.gaussian_filter((I / np.amax(I)), sigma=1)
    J = ndimage.gaussian_filter((J / np.amax(J)), sigma=1)
    # J = rotation(I, 5)
    # J2 = lucas_kanade_recalage(I, J, 1000)
    # J2 = gradient_descent_translation_recalage(I, J, 10000, lamb=0.1)
    J2 = rotation_recalage(I, J, 5000, lamb=0.00000001)
    plt.figure()
    plt.imshow(J2)
    plt.title("image recalée")
    plt.figure()
    plt.imshow(I-J2)
    plt.figure()
    plt.title("image de base")
    plt.imshow(I)
    plt.colorbar()
    plt.show()

