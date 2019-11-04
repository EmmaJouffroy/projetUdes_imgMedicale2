import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from numpy.linalg import inv


def interpol(i, j, I):
    i_new = int(np.round(i))
    j_new = int(np.round(j))
    out = False
    if (i_new < 0) or (i_new >= I.shape[0]):
        out = True
        return i_new, j_new, out
    if j_new < 0 or j_new >= I.shape[1]:
        out = True
        return i_new, j_new, out
    return i_new, j_new, out


def translation(I, p, q):
    new_img = np.zeros((I.shape[0], I.shape[1]))
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            # i,j est le pixel en cours d'analyse
            i_new, j_new, out = interpol(i+p, j+q, I)
            if out is not True:
                new_img[i_new, j_new] = I[i, j]
    return new_img

def rotation(I, theta):
    new_img = np.zeros((I.shape[0], I.shape[1]))
    theta = (theta*math.pi)/180
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            i_new_rotate = i*np.cos(theta) - j*np.sin(theta)
            j_new_rotate = i*np.sin(theta) + j*np.cos(theta)
            i_new, j_new, out = interpol(i_new_rotate, j_new_rotate, I)
            if out is not True:
                new_img[i_new, j_new] = I[i, j]
    return new_img

def translation_recalage(I, J, iterMax):
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
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2

def rotation_recalage(I, J, iterMax, lamb):
    SSD = []
    theta = 0
    # theta = (theta*math.pi)/180
    for i in range(0, iterMax):
        J = rotation(J, theta)
        SSD.append(np.sum((J-I)**2))
        Jx = np.gradient(J, axis=0)
        Jy= np.gradient(J, axis=1)
        error = J - I
        cnt = 0
        for x in range(I.shape[0]):
            for y in range(I.shape[1]):
                res1 = (- x * np.sin(theta) - y * np.cos(theta))*Jx[x, y]
                res2 = (x * np.cos(theta) - y * np.sin(theta))*Jy[x, y]
                cnt += error[x, y] * (res1 + res2)
        ssd_d = 2 * cnt
        print(ssd_d)
        theta = theta - lamb * ssd_d
        print(i, theta)
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J

if __name__ == '__main__':
    I = np.array(Image.open('Data/BrainMRI_1.jpg'))
    J = np.array(Image.open('Data/BrainMRI_2.jpg'))
    plt.figure()
    plt.imshow(rotation(I, 45))
    plt.figure()
    plt.imshow(I)
    plt.show()

