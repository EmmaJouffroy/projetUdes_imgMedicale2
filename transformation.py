import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import axes3d, Axes3D


def trans_rigide(theta, omega, phi, p, q, r, mesh):
    """
    Méthode permettant une tranlation et une rotation d'un volume 3D
    :param theta: rotation d'axe x
    :param omega: rotation d'axe y
    :param phi: rotation d'axe z
    :param p: translation selon x
    :param q: translation selon y
    :param r: translation selon z
    :param mesh: volume translaté et rotaté
    :return: Le volume resultant de l'opération
    """
    theta = (theta*math.pi)/180
    omega = (omega * math.pi) / 180
    phi = (phi * math.pi) / 180
    t = np.array((p, q, r, 1))
    rotation_x = np.array(([1, 0, 0, 0], [0, math.cos(theta), -math.sin(theta), 0],
                           [0, math.sin(theta), math.cos(theta), 0], [0, 0, 0, 1]))

    rotation_y = np.array(([math.cos(omega), 0, -math.sin(omega), 0], [0, 1, 0, 0],
                           [math.sin(omega), 0, math.cos(omega), 0], [0, 0, 0, 1]))
    rotation_z = np.array(([math.cos(phi),  -math.sin(phi), 0, 0], [math.sin(phi), math.cos(phi), 0, 0],
                           [0, 0, 1, 0], [0, 0, 0, 1]))
    trans_rot_x_y = np.dot(rotation_x, rotation_y)
    trans_rot_x_y_z = np.dot(trans_rot_x_y, rotation_z)
    transformed1 = np.dot(trans_rot_x_y_z, mesh)
    transformed1 = transformed1 + t.T
    return transformed1


def similitude(s, theta, omega, phi, p, q, r, mesh):
    """
    Méthode permettant une tranlation, une rotation et un scaling (redimensionnement) d'un volume 3D
    :param s: magnitude du redimensionnement
    :param theta: rotation d'axe x
    :param omega: rotation d'axe y
    :param phi: rotation d'axe z
    :param p: translation selon x
    :param q: translation selon y
    :param r: translation selon z
    :param mesh: volume translaté et rotaté
    :return: Le volume resultant de l'opération
    """
    rotation_matrix = trans_rigide(theta, omega, phi, 0, 0, 0, mesh)
    t = np.array((p, q, r, 1))
    transformed1 = s * rotation_matrix + t.T
    return transformed1


if __name__ == '__main__':

    M1 = np.array([[0.9045, -0.3847, -0.1840, 10.0000],
                  [0.2939, 0.8750, -0.3847, 10.0000],
                  [0.3090, 0.2939, 0.9045, 10.0000],
                  [0, 0,  0, 1.0000]])
    M2 = np.array([[-0.0000, -0.2598, 0.1500, -3.0000],
                   [0.0000, -0.1500, -0.2598, 1.5000],
                   [0.3000, -0.0000, 0.0000, 0],
                   [0, 0, 0, 1.0000]])
    M3 = np.array([[0.7182, -1.3727, -0.5660, 1.8115],
                   [-1.9236, -4.6556, -2.5512, 0.2873],
                   [-0.6426, -1.7985, -1.6285, 0.7404],
                   [0, 0, 0, 1.0000]])
    print(M1.shape)

    def test_transrigide(theta, omega, phi, p, q, r):
        x = np.linspace(0, 20, 20)
        y = np.linspace(0, 10, 10)
        z = np.linspace(0, 2, 2)
        xm, ym, zm = np.meshgrid(x, y, z)
        mesh = np.array((xm, ym, zm, 1))
        transformed1 = trans_rigide(theta, omega, phi, p, q, r, mesh)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        X, Y, Z = mesh[0], mesh[1], mesh[2]
        Xt, Yt, Zt = transformed1[0], transformed1[1], transformed1[2]
        ax.scatter3D(X, Y, Z, cmap='binary')
        ax.scatter3D(Xt, Yt, Zt, cmap='binary')
        ax.set(xlim=(-100, 100), ylim=(-100, 100), zlim=(-100, 100))
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.title("rotation et translation")
        plt.show()
    # test_transrigide(0, 90, 90, 2, 20, 20)

    def test_similitude(s, theta, omega, phi, p, q, r, m = np.array([])):
        x = np.linspace(0, 20, 20)
        y = np.linspace(0, 10, 10)
        z = np.linspace(0, 2, 2)
        xm, ym, zm = np.meshgrid(x, y, z)
        mesh = np.array((xm, ym, zm, 1))
        if m.shape[0] == 0:
            transformed1 = similitude(s, theta, omega, phi, p, q, r, mesh)
        else:
            transformed1 = np.dot(m, mesh)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        X, Y, Z = mesh[0], mesh[1], mesh[2]
        Xt, Yt, Zt = transformed1[0], transformed1[1], transformed1[2]
        ax.scatter3D(X, Y, Z, cmap='binary')
        ax.scatter3D(Xt, Yt, Zt, cmap='binary')
        ax.set(xlim=(0, 50), ylim=(0, 50), zlim=(0, 50))
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.title("mise à l'échelle, rotation et translation")
        plt.show()

    # test_similitude(1.5, 0, 90, 90, 2, 20, 20)
    # test_similitude(0, 0, 0, 0, 0, 0, 0, M1)
    # test_similitude(0, 0, 0, 0, 0, 0, 0, M2)
    # test_similitude(0, 0, 0, 0, 0, 0, 0, M3)




