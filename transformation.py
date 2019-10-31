import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x = np.linspace(0, 10, 10)
    y = np.linspace(0, 10, 10)
    z = np.linspace(0, 10, 10)
    X, Y, Z = np.meshgrid(x, y, z)
    ax.scatter3D(X, Y, Z, cmap='binary')
    ax.scatter3D(X+10, Y+20, Z+30, cmap='binary')
    ax.set(xlim=(0, 50), ylim=(0, 50), zlim=(0, 50))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    mesh = np.meshgrid(x, y, z)
