import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from histogramme import jointHist


def SSD(I, J):
    """
    Méthode calculant la somme des différences au carré des deux images I et J de même taille
    :param I:
    :param J:
    :return:
    """
    return np.sum((I-J)**2)


def CR(I, J):
    """
    Méthode calculant le coefficient de corrélation de deux images I et J de même taille
    :param I:
    :param J:
    :return:
    """
    mean_I = np.mean(I)
    mean_J = np.mean(J)
    centered_I = I - mean_I
    centered_J = J - mean_J
    num = np.sum(centered_I*centered_J)
    denom = np.sqrt(np.sum(centered_I**2))*np.sqrt(np.sum(centered_J**2))
    return num / denom


def IM(hist):
    """
    Méthode calculant l'information mutuelle entre deux images I et J de même taille
    A partir de leur histogramme conjoint
    :param hist:
    :return:
    """
    hist = hist / float(np.sum(hist))
    px = np.sum(hist, axis=1)
    px = np.expand_dims(px, axis=0)
    py = np.sum(hist, axis=0)
    py = np.expand_dims(py, axis=1)
    px_py = np.dot(px.T, py.T)
    # Fonctionnalité "geniale" de numpy pour ne pas conserver les indices des 0 de l'array hist:
    nzs = hist > 0
    # Autre fonctionnalité géniale pour ne pas utiliser de boucle:
    mutual_info = np.sum(hist[nzs] * np.log(hist[nzs] / px_py[nzs]))
    return mutual_info


def afficher_similarites(images_I,images_J, ssd, cr, im ):
    """
    Fonction permettant l'affichage des différentes images à comparer
    :param images_I:
    :param images_J:
    :param ssd:
    :param cr:
    :param im:
    :return:
    """
    ax1 = plt.subplot2grid((2, 6), (0, 0), colspan=1)
    ax1.axis('off')
    ax1.imshow(images_I[0])
    ax2 = plt.subplot2grid((2, 6), (1, 0), colspan=1)
    ax2.axis('off')
    ax2.imshow(images_J[0])
    ax6 = plt.subplot2grid((2, 6), (0, 1), colspan=1)
    ax6.axis('off')
    ax6.imshow(images_I[1])
    ax7 = plt.subplot2grid((2, 6), (1, 1), colspan=1)
    ax7.axis('off')
    ax7.imshow(images_J[1])
    ax11 = plt.subplot2grid((2, 6), (0, 2), colspan=1)
    ax11.axis('off')
    ax11.imshow(images_I[2])
    ax12 = plt.subplot2grid((2, 6), (1, 2), colspan=1)
    ax12.axis('off')
    ax12.imshow(images_J[2])
    ax16 = plt.subplot2grid((2, 6), (0, 3), colspan=1)
    ax16.axis('off')
    ax16.imshow(images_I[3])
    ax17 = plt.subplot2grid((2, 6), (1, 3), colspan=1)
    ax17.axis('off')
    ax17.imshow(images_J[3])
    ax21 = plt.subplot2grid((2, 6), (0, 4), colspan=1)
    ax21.axis('off')
    ax21.imshow(images_I[4])
    ax22 = plt.subplot2grid((2, 6), (1, 4), colspan=1)
    ax22.axis('off')
    ax22.imshow(images_J[4])
    ax26 = plt.subplot2grid((2, 6), (0, 5), colspan=1)
    ax26.axis('off')
    ax26.imshow(images_I[5])
    ax27 = plt.subplot2grid((2, 6), (1, 5), colspan=1)
    ax27.axis('off')
    ax27.imshow(images_J[5])
    plt.show()


def test_afficher_similarites():
    images_I = [np.array(Image.open('Data/I1.png')), np.array(Image.open('Data/I2.jpg')),
                np.array(Image.open('Data/I3.jpg')),  np.array(Image.open('Data/I4.jpg')),
                np.array(Image.open('Data/I5.jpg')), np.array(Image.open('Data/I6.jpg'))]

    images_J = [np.array(Image.open('Data/J1.png')), np.array(Image.open('Data/J2.jpg')),
                np.array(Image.open('Data/J3.jpg')), np.array(Image.open('Data/J4.jpg')),
                np.array(Image.open('Data/J5.jpg')), np.array(Image.open('Data/J6.jpg'))]
    ssd = []
    cr = []
    im = []

    for i in range(0, 6):
        ssd.append(SSD(images_I[i], images_J[i]))
        cr.append(CR(images_I[i], images_J[i]))
        im.append(IM(jointHist(images_I[i], images_J[i], bin=20)))

    afficher_similarites(images_I, images_J, ssd, cr, im)
    print("SSD=", ssd)
    print("Coefficient de corrélation=", cr)
    print("Information mutuelle=", im)


if __name__ == '__main__':
    pass
    # test_afficher_similarites()
