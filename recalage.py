import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformation_interpolations import translation, rotation


def translation_recalage(I, J, iterMax):
    SSD = []
    u = np.array([0, 0])
    J2 = J
    for i in range(0, iterMax):
        J2 = translation(J2, u[0], u[1], type="NN")
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
    J2 = J
    for i in range(0, iterMax):
        J2 = rotation(J2, theta)
        SSD.append(np.sum((J2-I)**2))
        J2x = np.gradient(J2, axis=0)
        J2y= np.gradient(J2, axis=1)
        error = J2 - I
        cnt = 0
        for x in range(J2.shape[0]):
            for y in range(J2.shape[1]):
                x_p = int(np.ceil(x*np.cos(theta)-y*np.sin(theta)))
                y_p = int(np.ceil(x * np.sin(theta) + y * np.cos(theta)))
                print(x_p, y_p)
                if (x_p > 0) & (x_p < J2.shape[0]-1):
                    if (y_p > 0) & (y_p < J2.shape[1]-1):
                        res1 = J2x[x_p, y_p] * ((- x * np.sin(theta)) - (y * np.cos(theta)))
                        res2 = J2y[x_p, y_p] * ((x * np.cos(theta)) - (y * np.sin(theta)))
                        cnt = cnt + error[x, y] * (res1 + res2)
        ssd_d = 2 * cnt
        theta = theta - lamb * ssd_d
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2

#scipy.map_coordinate

if __name__ == '__main__':
    I = np.array(Image.open('Data/BrainMRI_1.jpg')).astype(np.int32)
    J = np.array(Image.open('Data/BrainMRI_2.jpg')).astype(np.int32)
    # J = rotation(I, 5)
    plt.figure()
    plt.imshow(rotation_recalage(I, J, 10, (10**-8)))
    plt.title("image recalée")
    plt.figure()
    plt.title("image de base")
    plt.imshow(I)
    plt.show()

