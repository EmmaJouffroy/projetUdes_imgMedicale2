import numpy as np
import matplotlib.pyplot as plt


def JointHist(I, J, bin):
    """

    :param I: np.array()
    :param J: np.array()
    :param bin: Nombre de classes
    :return:
    """
    # On trouve d'abbord la plage de valeurs conjointes
    intensiteI_min = I.amin()
    intensiteJ_min = J.amin()

