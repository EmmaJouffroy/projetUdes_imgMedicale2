import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from skimage.restoration import denoise_nl_means, denoise_bilateral


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

def translation_recalage2(I, J, iterMax, lamb):
    SSD = []
    theta = 0
    J2 = J
    for i in range(0, iterMax):
        J2 = rotation(J2, theta)
        SSD.append(np.sum((J2-I)**2))
        J2x = np.gradient(J2, axis=0)
        J2y= np.gradient(J2, axis=1)
        error = J2 - I
        print(np.sum(error))
        cnt = 0
        for x in range(J2.shape[0]):
            for y in range(J2.shape[1]):
                res1 = J2x[x, y] * ((- x * np.sin(theta)) - (y * np.cos(theta)))
                res2 = J2y[x, y] * ((x * np.cos(theta)) - (y * np.sin(theta)))
                cnt = cnt + error[x, y] * (res1 + res2)
                print(res1+res2)
        ssd_d = 2 * cnt
        theta = theta - lamb * ssd_d
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2

def rotation_recalage(I, J, iterMax, lamb):
    ## DEUX PROBLEMES : ERROR TRES GRAND, ET SHAPE DE RES1 + RES2, POURQUOIIII SCALAIRES
    SSD = []
    theta = 0
    # theta = (theta*math.pi)/180
    for i in range(0, iterMax):
        J = rotation(J, theta)
        SSD.append(np.sum((I-J)**2))
        Jx = np.gradient(J, axis=0)
        Jy= np.gradient(J, axis=1)
        error = J - I
        cnt = 0
        ssd_d = 0
        print("init cnt = ", cnt)
        print("init ssd_d = ", ssd_d)
        for x in range(I.shape[0]):
            for y in range(I.shape[1]):
               # print("theta", theta)
                res1 = ((- x * np.sin(theta)) - (y * np.cos(theta)))*Jx[x, y]
                res2 = ((x * np.cos(theta)) - (y * np.sin(theta)))*Jy[x, y]
                cnt = cnt + error[x, y] * (res1 + res2)
                # print("res1 + res2 = ", res1+res2)
               # print("cnt", cnt)
               # print("error", x, y, error[x, y])
               # print("----------------------------------------")
        print("somme error = ", np.sum(error))
        print("amax error", np.amax(error))
        print("amix error", np.amin(error))
        print("theta 1 : ", theta)
        print("cnt = cnt + ( error * (res1+res2) ) = ", cnt)
        #print("ssd_d 1 : ", ssd_d)
        ssd_d = 2 * cnt
        print("ssd_d 2 :", ssd_d)
        theta = theta - lamb * ssd_d
        print("theta 2 : ", theta)
        print("----------------------------------------")

    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J

if __name__ == '__main__':
    I = np.array(Image.open('Data/BrainMRI_2.jpg'))
    J = np.array(Image.open('Data/BrainMRI_3.jpg'))
  #  I = denoise_nl_means(I, patch_size=5, patch_distance=10, h=10)
  #  J = denoise_nl_means(J, patch_size=5, patch_distance=10, h=10)
    #J = np.array(Image.open('Data/BrainMRI_3.jpg'))
    J = rotation(I, 5)
    plt.figure()
    plt.imshow(translation_recalage2(I, J, 10, 0.000001))
    plt.figure()
    plt.imshow(I)
    plt.show()

