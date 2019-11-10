import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformation_interpolations import translation_scipy, rotation_scipy
from scipy import ndimage


def lucas_kanade_recalage(I, J, iterMax):
    """
    Méthode de recalage utilisant la formule de lucas-kanade
    :param I: img1
    :param J: img a recaler
    :param iterMax: nombre d'itérations
    :return:
    """
    SSD = []
    u = np.array([0, 0])
    J2 = ndimage.interpolation.shift(J, u)
    for i in range(0, iterMax):
        # On calcule l'erreur entre l'image transformée et l'image sur laquelle recalée
        SSD.append(np.sum((J2-I)**2))
        # On calcule tous les éléments pour appliquer la formule de Lucas-Kanade
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
        # On modifie notre vecteur de translation:
        u = u + np.squeeze(np.linalg.solve(M, b), axis=1)
        # On translate l'image initiale avec ce nouveau vecteur
        J2 = ndimage.interpolation.shift(J, u)
    return J2, SSD


def translation_recalage(I, J, iterMax, lamb):
    """
    Méthode de recalage par translation utilisant l'algorithme descente de gradient.
    :param I:
    :param J:
    :param iterMax:
    :param lamb:
    :return:
    """
    SSD = []
    u = np.array([0, 0])
    J2 = translation_scipy(J, u)
    J_derivate_x = np.gradient(J, axis=1)
    J_derivate_y = np.gradient(J, axis=0)
    for i in range(1, iterMax):
        print(u)
        error = J2 - I
        # Sauvegarde de l'erreur:
        SSD.append((np.sum(error**2)))
        # Calcul des dérivés "translatés"
        J2_derivate_xp = translation_scipy(J_derivate_x, u)
        J2_derivate_yp = translation_scipy(J_derivate_y, u)
        ssd_p = 2 * np.sum(error*J2_derivate_xp)
        ssd_q = 2 * np.sum(error*J2_derivate_yp)
        # Mise à jour du vecteur de translation selon la formule de la descente de gradient
        u = u + [lamb * ssd_p, lamb * ssd_q]
        J2 = translation_scipy(J, u)
    return J2, SSD


def rotation_recalage(I, J, iterMax, lamb):
    """
    Méthode de recalage par rotation utilisant l'algorithme descente de gradient.
    :param I:
    :param J:
    :param iterMax:
    :param lamb:
    :return:
    """
    SSD = []
    theta = 0
    J2 = rotation_scipy(J, theta)
    J_derivate_x = np.gradient(J, axis=0)
    J_derivate_y = np.gradient(J, axis=1)
    x, y = np.meshgrid(range(I.shape[0]), range(I.shape[1]))
    for i in range(1, iterMax):
        error = J2 - I
        # Sauvegarde de l'erreur :
        SSD.append(np.sum(error**2))
        # Calcul des dérivés "rotatés"
        J2_derivate_xp = rotation_scipy(J_derivate_x, theta)
        J2_derivate_yp = rotation_scipy(J_derivate_y, theta)
        # Calcul des élèments "sortant de la dérivée de l'image par théta"
        res1 = J2_derivate_xp * ((- x * np.sin(theta)) - (y * np.cos(theta)))
        res2 = J2_derivate_yp * ((x * np.cos(theta)) - (y * np.sin(theta)))
        # Calcul finale de la dérivée par theta de l'erreur
        ssd_d = 2 * np.sum((error*(res1 + res2)))
        theta = theta - (lamb * ssd_d)
        J2 = rotation_scipy(J, theta)
        print(np.rad2deg(theta))
    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2, SSD


def iconique_recalage(I, J, iterMax, lamb, seuil=0.001):
    """
    Méthode de recalage par rotation ET translation utilisant la descente de gradient.
    :param I:
    :param J:
    :param iterMax:
    :param lamb:
    :return:
    """
    SSD = [0, 0]
    u = np.array([0, 0])
    theta = 0
    J_derivate_x = np.gradient(J, axis=0)
    J_derivate_y = np.gradient(J, axis=1)
    x, y = np.meshgrid(range(I.shape[0]), range(I.shape[1]))
    J2 = rotation_scipy(J, theta)
    J2 = translation_scipy(J2, u)
    # Les "coefficients d'apprentissage" différent, on pourrait les fixer indépendament les uns des autres
    # Mais la méthode suivante fonctionne aussi:
    lamb_trans = lamb * 1000000
    for i in range(1, iterMax):
        error = J2 - I
        # Sauvegarde de l'erreur:
        SSD.append(np.sum(error**2))
        #Calcul des dérivés pour la rotation
        J2_derivate_xp_rotation = rotation_scipy(J_derivate_x, theta)
        J2_derivate_yp_rotation = rotation_scipy(J_derivate_y, theta)
        res1 = J2_derivate_xp_rotation * ((- x * np.sin(theta)) - (y * np.cos(theta)))
        res2 = J2_derivate_yp_rotation * ((x * np.cos(theta)) - (y * np.sin(theta)))
        ssd_d = 2 * np.sum((error*(res1 + res2)))
        # Mise à jour de l'angle de rotation
        theta = theta - (lamb * ssd_d)
        # Calcul des dérivés pour la translation
        J2_derivate_xp_translation = translation_scipy(J_derivate_x, u)
        J2_derivate_yp_translation = translation_scipy(J_derivate_y, u)
        ssd_p = 2 * np.sum(error*J2_derivate_xp_translation)
        ssd_q = 2 * np.sum(error*J2_derivate_yp_translation)
        # Mise à jour du vecteur de translation:
        u = u + [(lamb_trans) * ssd_p, (lamb_trans) * ssd_q]
        print(theta, u)
        # Transformation selon u et theta de l'image:
        J2 = rotation_scipy(J, theta)
        J2 = translation_scipy(J2, u)
        # Utilisation d'un critère
        if (abs(SSD[-1]-SSD[-3])/2) < seuil:
            # Si l'approximation de la dérivée est en dessous du seuil fixé
            # On arrete la descente de gradient
            plt.figure()
            plt.plot(SSD)
            plt.show()
            return J2, SSD[2:]

    plt.figure()
    plt.plot(SSD)
    plt.show()
    return J2, SSD[2:]


def afficher_resultats(img_init, img_to_move, img_recale, SSD_curve):
    """
    Méthode permettant d'afficher les résultats apres recalage
    :param img_init:
    :param img_to_move:
    :param img_recale:
    :param SSD_curve:
    :return:
    """
    ax1 = plt.subplot2grid((2, 4), (0, 0), colspan=1)
    ax1.axis('off')
    ax1.set_title('Image de base')
    ax1.imshow(img_init)

    ax2 = plt.subplot2grid((2, 4), (0, 1), colspan=1)
    ax2.axis('off')
    ax2.set_title('Image à recaler')
    ax2.imshow(img_to_move)

    ax3 = plt.subplot2grid((2, 4), (0, 2), colspan=1)
    ax3.axis('off')
    ax3.set_title('Image recalée')
    ax3.imshow(img_recale)

    ax4 = plt.subplot2grid((2, 4), (0, 3), colspan=1)
    ax4.axis('off')
    ax4.set_title('Différence des images')
    ax4.imshow(img_init-img_recale)

    ax5 = plt.subplot2grid((2, 4), (1, 0), colspan=4)
    ax5.set_title('Courbe SSD')
    ax5.plot(SSD_curve)

    plt.show()


def test_lucas_kanade_recalage(itermax=1000):
    I = np.array(Image.open('Data/BrainMRI_1.jpg'))
    I = ndimage.gaussian_filter((I / np.amax(I)), sigma=1)
    J = np.array(Image.open('Data/BrainMRI_2.jpg'))
    J = ndimage.gaussian_filter((J / np.amax(J)), sigma=1)
    lucas_kanade, ssd = lucas_kanade_recalage(I, J, itermax)
    afficher_resultats(I, J, lucas_kanade, ssd)


def test_translation_recalage(itermax=10000, lamb=0.0001):
    I = np.array(Image.open('Data/BrainMRI_1.jpg'))
    J = translation_scipy(I, [-5, 12])
    I = ndimage.gaussian_filter((I / np.amax(I)), sigma=1)
    J = ndimage.gaussian_filter((J / np.amax(J)), sigma=1)
    translated, ssd = translation_recalage(I, J, itermax, lamb=lamb)
    afficher_resultats(I, J, translated, ssd)


def test_rotation_recalage(itermax=10000, lamb=0.00000001):
    I = np.array(Image.open('Data/BrainMRI_3.jpg'))
    J = rotation_scipy(I, np.deg2rad(12))
    I = ndimage.gaussian_filter((I / np.amax(I)), sigma=1)
    J = ndimage.gaussian_filter((J / np.amax(J)), sigma=1)
    translated, ssd = rotation_recalage(I, J, itermax, lamb=lamb)
    afficher_resultats(I, J, translated, ssd)


def test_iconique_recalage(itermax=10000, lamb=0.0000000001):
    I = np.array(Image.open('Data/BrainMRI_1.jpg'))
    I = ndimage.gaussian_filter((I / np.amax(I)), sigma=1)
    J = np.array(Image.open('Data/BrainMRI_4.jpg'))
    J = ndimage.gaussian_filter((J / np.amax(J)), sigma=1)
    iconique, ssd = iconique_recalage(I, J, itermax, lamb=lamb)
    afficher_resultats(I, J, iconique, ssd)


if __name__ == '__main__':
    pass
    # test_lucas_kanade_recalage()
    # test_translation_recalage()
    # test_rotation_recalage()
    # test_iconique_recalage(10000, 0.0000000001)



