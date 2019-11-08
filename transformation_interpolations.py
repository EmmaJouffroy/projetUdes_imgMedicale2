import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image
from scipy import ndimage


def interpol_nn(i, j, img):
    """
    Méthode non utilisée pour le recalage, dévéloppement "à la main" de l'interpolation au plus proche voisin
    :param i:
    :param j:
    :param img:
    :return:
    """
    i_new = int(np.round(i))
    j_new = int(np.round(j))
    out = False
    if (i_new < 0) or (i_new >= img.shape[0]):
        out = True
        return i_new, j_new, out
    if j_new < 0 or j_new >= img.shape[1]:
        out = True
        return i_new, j_new, out
    return i_new, j_new, out


def interpol_bilin(i, j, img):
    """
    Méthode non utilisée pour le recalage, dévéloppement "à la main" de l'interpolation bilineaire
    :param i:
    :param j:
    :param img:
    :return:
    """
    out = False
    left_corners = (np.floor(i))
    right_corners = (np.ceil(i))
    top_corners = (np.floor(j))
    bottom_corners = (np.ceil(j))
    index = [int(left_corners), int(right_corners), int(top_corners), int(bottom_corners)]
    aires = []
    if (left_corners > 0) & (right_corners < img.shape[0]) & (top_corners > 0) & (bottom_corners < img.shape[1]):
        aires.append((i - left_corners)*(j - top_corners))
        aires.append((right_corners - i) * (j - top_corners))
        aires.append((i - left_corners) * (bottom_corners - j))
        aires.append(1 - sum(aires))
        return aires, index, out
    else:
        out = True
        return aires, index, out


def translation(img, p, q, type="NN"):
    """
    Méthode non utilisée pour le recalage, dévéloppement "à la main" d'une translation utilisant les méthodes d'inter-
    polation développé ci-avant.
    Note: Pour éviter d'avoir une image présentant des "trous", on parcourt la grille de l'image d'arrivée (et on
    revient à l'image de départ)
    :param img:
    :param p:
    :param q:
    :param type:
    :return:
    """
    new_img = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if type == "NN":
                # i,j est le pixel en cours d'analyse
                i_new, j_new, out = interpol_nn(i + p, j + q, img)
                if out is not True:
                    new_img[i_new, j_new] = img[i, j]
            elif type == "Bilineaire":
                aires, index, out = interpol_bilin(i-p, j-q, img)
                if out is not True:
                    new_img[i, j] = aires[0]*img[index[0], index[2]] \
                                    + aires[1]*img[index[1], index[2]] \
                                    + aires[2]*img[index[0], index[3]] \
                                    + aires[3]*img[index[1], index[3]]
    return new_img


def rotation(img, theta, type="NN"):
    new_img = np.zeros((img.shape[0], img.shape[1]))
    theta = (theta*math.pi)/180
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            i_origin = i*np.cos(theta) + j*np.sin(theta)
            j_origin = -i*np.sin(theta) + j*np.cos(theta)
            if type == "NN":
                i_origin, j_origin, out = interpol_nn(i_origin, j_origin, img)
                if out is not True:
                    new_img[i, j] = img[i_origin, j_origin]
            elif type == "Bilineaire":
                aires, index, out = interpol_bilin(i_origin, j_origin, img)
                if out is not True:
                    new_img[i, j] = aires[0]*img[index[0], index[2]] \
                                    + aires[1]*img[index[1], index[2]] \
                                    + aires[2]*img[index[0], index[3]] \
                                    + aires[3]*img[index[1], index[3]]
    return new_img


def rotation_scipy(img, theta_rad):
    """
    :param img:
    :param theta_rad: Toujours fournir un angle en radian!!!
    :return:
    """
    dims = img.shape
    # theta_rad = np.rad2deg(theta)
    x, y = np.meshgrid(np.arange(dims[1]), np.arange(dims[0]))
    x, y = x*np.cos(theta_rad) + y*np.sin(theta_rad),   -x*np.sin(theta_rad) + y*np.cos(theta_rad)
    rotated = ndimage.map_coordinates(img, [y, x], mode='constant', cval=0, order=3)
    return rotated


def translation_scipy(img, t):
    dims = img.shape
    x, y = np.meshgrid(np.arange(dims[1]), np.arange(dims[0]))
    xp = x - t[0]
    yp = y - t[1]
    translated = ndimage.map_coordinates(img, [yp, xp], mode='constant', cval=0, order=3)
    return translated


if __name__ == '__main__':
    img = np.array(Image.open('Data/BrainMRI_2.jpg'))
    # img = np.array([[1, 2, 3], [4, 5, 6]])
    plt.figure()
    plt.imshow(img)
    plt.title('Image de 20 degres (traduit en radian)')
    plt.imshow(rotation_scipy(img, np.deg2rad(20)))
    plt.show()

