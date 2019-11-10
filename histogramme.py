import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.colors import LogNorm


def jointHist(img1, img2, bin):
    """
    Méthode permettant la création d'un histogramme joint possèdant bin classes entre 2 images de même taille
    :param img1: np.array()
    :param img2: np.array()
    :param bin: Nombre de classes
    :return:
    """
    # On vérifie que les images partagent bien la même taille
    assert img1.shape == img2.shape
    # On cherche les valeurs d'intensités maximales des deux images:
    max = np.max(np.array([np.amax(img1), np.amax(img2)]))
    # On crée un histogramme vide carré de taille bin (ie de taille nombre de classes):
    hist = np.zeros((bin, bin)).astype(int)
    nb_val_per_bin = round(max / bin)
    # On parcourt en même temps les images I et J et on cherche dans quel bin se trouve le pixel(i,j)
    # de chaque image:
    for i in range(0, img1.shape[0]):
        for j in range(0, img1.shape[1]):
            bin_i = int(img1[i, j] // nb_val_per_bin)
            if bin_i >= bin:
                bin_i = bin - 1
            bin_j = int(img2[i, j] // nb_val_per_bin)
            if bin_j >= bin:
                bin_j = bin - 1
            hist[bin_i, bin_j] += 1
    return hist


def afficher_histogrammes_joints(images_I, images_J, hist_joint):
    """
    Méthode permettant l'affichage des histogrames joints
    :param images_I:
    :param images_J:
    :param hist_joint:
    :return:
    """

    ax1 = plt.subplot2grid((3, 6), (0, 0), colspan=1)
    ax1.axis('off')
    ax1.set_title('Image I1')
    ax1.imshow(images_I[0])

    ax2 = plt.subplot2grid((3, 6), (1, 0), colspan=1)
    ax2.axis('off')
    ax2.set_title('Image J1')
    ax2.imshow(images_J[0])

    ax3 = plt.subplot2grid((3, 6), (2, 0), colspan=1)
    ax3.axis('off')
    ax3.set_title('Histogramme I1-J1')
    ax3.imshow(hist_joint[0], cmap='jet', origin="lower")

    ax4 = plt.subplot2grid((3, 6), (0, 1), colspan=1)
    ax4.axis('off')
    ax4.set_title('Image I2')
    ax4.imshow(images_I[1])

    ax5 = plt.subplot2grid((3, 6), (1, 1), colspan=1)
    ax5.axis('off')
    ax5.set_title('Image J2')
    ax5.imshow(images_J[1])

    ax6 = plt.subplot2grid((3, 6), (2, 1), colspan=1)
    ax6.axis('off')
    ax6.set_title('Histogramme I2-J2')
    ax6.imshow(hist_joint[1], cmap='jet', origin="lower")

    ax7 = plt.subplot2grid((3, 6), (0, 2), colspan=1)
    ax7.axis('off')
    ax7.set_title('Image I3')
    ax7.imshow(images_I[2])

    ax8 = plt.subplot2grid((3, 6), (1, 2), colspan=1)
    ax8.axis('off')
    ax8.set_title('Image J3')
    ax8.imshow(images_J[2])

    ax9 = plt.subplot2grid((3, 6), (2, 2), colspan=1)
    ax9.axis('off')
    ax9.set_title('Histogramme I3-J3')
    norm = LogNorm(1, np.amax(hist_joint[2]), clip='True')
    ax9.imshow(hist_joint[2]+1, norm=norm, cmap='jet', origin="lower")

    ax10 = plt.subplot2grid((3, 6), (0, 3), colspan=1)
    ax10.axis('off')
    ax10.set_title('Image I4')
    ax10.imshow(images_I[3])

    ax11 = plt.subplot2grid((3, 6), (1, 3), colspan=1)
    ax11.axis('off')
    ax11.set_title('Image J4')
    ax11.imshow(images_J[3])

    ax12 = plt.subplot2grid((3, 6), (2, 3), colspan=1)
    ax12.axis('off')
    ax12.set_title('Histogramme I4-J4')
    norm = LogNorm(1, np.amax(hist_joint[3]), clip='True')
    ax12.imshow(hist_joint[3]+1, norm=norm, cmap='jet', origin="lower")

    ax13 = plt.subplot2grid((3, 6), (0, 4), colspan=1)
    ax13.axis('off')
    ax13.set_title('Image I5')
    ax13.imshow(images_I[4])

    ax14 = plt.subplot2grid((3, 6), (1, 4), colspan=1)
    ax14.axis('off')
    ax14.set_title('Image J5')
    ax14.imshow(images_J[4])

    ax15 = plt.subplot2grid((3, 6), (2, 4), colspan=1)
    ax15.axis('off')
    ax15.set_title('Histogramme I5-J5')
    norm = LogNorm(1, np.amax(hist_joint[4]), clip='True')
    ax15.imshow(hist_joint[4]+1, norm=norm, cmap='jet', origin="lower")

    ax16 = plt.subplot2grid((3, 6), (0, 5), colspan=1)
    ax16.axis('off')
    ax16.set_title('Image I6')
    ax16.imshow(images_I[5])

    ax17 = plt.subplot2grid((3, 6), (1, 5), colspan=1)
    ax17.axis('off')
    ax17.set_title('Image J6')
    ax17.imshow(images_J[5])

    ax18 = plt.subplot2grid((3, 6), (2, 5), colspan=1)
    ax18.axis('off')
    ax18.set_title('Histogramme I6-J6')
    norm = LogNorm(1, np.amax(hist_joint[5]), clip='True')
    ax18.imshow(hist_joint[5]+1, norm=norm, cmap='jet', origin="lower")

    plt.show()


def test_joint_histogramme(nbr):
    if nbr == 1:
        I = np.array(Image.open('Data/I'+str(nbr)+'.png'))
        J = np.array(Image.open('Data/J'+str(nbr)+'.png'))
    else:
        I = np.array(Image.open('Data/I'+str(nbr)+'.jpg'))
        J = np.array(Image.open('Data/J'+str(nbr)+'.jpg'))

    hist = jointHist(I, J, 50)
    assert np.sum(hist) == I.shape[0]*I.shape[1]
    norm = LogNorm(1, np.amax(hist), clip='True')
    plt.imshow(hist+1, norm=norm, cmap='jet', origin="lower")
    plt.colorbar()
    plt.title("Histogramme I"+str(nbr)+"/J"+str(nbr)+"\n Nombre de classes = 50")
    plt.show()


def test_afficher_histogramme():
    bin = 50
    images_I = [np.array(Image.open('Data/I1.png')), np.array(Image.open('Data/I2.jpg')),
                np.array(Image.open('Data/I3.jpg')),  np.array(Image.open('Data/I4.jpg')),
                np.array(Image.open('Data/I5.jpg')), np.array(Image.open('Data/I6.jpg'))]
    images_J = [np.array(Image.open('Data/J1.png')), np.array(Image.open('Data/J2.jpg')),
                np.array(Image.open('Data/J3.jpg')), np.array(Image.open('Data/J4.jpg')),
                np.array(Image.open('Data/J5.jpg')), np.array(Image.open('Data/J6.jpg'))]
    hist = []
    for i in range(0, 6):
        hist.append(jointHist(images_I[i], images_J[i], bin))
    afficher_histogrammes_joints(images_I, images_J, hist)


if __name__ == '__main__':
    """
    L'ensemble des fonctions ont été utilisé dans la phase de test et de rédaction du manuscrit du projet 
    """

    test_joint_histogramme(1)
    # test_afficher_histogramme()
