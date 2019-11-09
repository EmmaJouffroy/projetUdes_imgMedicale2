import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import axes3d, Axes3D

def trans_rigide(theta, omega, phi, p, q, r, mesh):
    """

    :param theta:
    :param omega:
    :param phi:
    :param p:
    :param q:
    :param r:
    :param mesh:
    :return:
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

    :param s:
    :param theta:
    :param omega:
    :param phi:
    :param p:
    :param q:
    :param r:
    :param mesh:
    :return:
    """
    rotation_matrix = trans_rigide(theta, omega, phi, 0, 0, 0, mesh)
    t = np.array((p, q, r, 1))
    transformed1 = s * rotation_matrix + t.T
    return transformed1


if __name__ == '__main__':

    def test_transrigide():
        x = np.linspace(0, 20, 20)
        y = np.linspace(0, 10, 10)
        z = np.linspace(0, 2, 2)
        xm, ym, zm = np.meshgrid(x, y, z)
        mesh = np.array((xm, ym, zm, 1))
        transformed1 = trans_rigide(0, 90, 90, 2, 20, 8, mesh)
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
        plt.title("rotation et translation")
        plt.show()

    # test_transrigide()

    def test_similitude():
        x = np.linspace(0, 20, 20)
        y = np.linspace(0, 10, 10)
        z = np.linspace(0, 2, 2)
        xm, ym, zm = np.meshgrid(x, y, z)
        mesh = np.array((xm, ym, zm, 1))
        transformed1 = similitude(0.5, 0, 90, 90, 2, 20, 20, mesh)
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

    # test_similitude()



