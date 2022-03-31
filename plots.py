import matplotlib.pyplot as plt
import numpy as np


def make_plots(image, image_laplas, image_mask):

    image_srez = [i for i in image[int(image.shape[0] / 2)]]
    laplas_srez = [i for i in image_laplas[int(image_laplas.shape[0] / 2)]]
    mask_srez = [i for i in image_mask[int(image_mask.shape[0] / 2)]]

    plt.subplot(111)
    x = np.arange(0, image.shape[1], 1)
    plt.plot(x, image_srez)

    plt.show()

    plt.subplot(111)
    x = np.arange(0, image_laplas.shape[1], 1)
    plt.plot(x, laplas_srez)

    plt.show()

    plt.subplot(111)
    x = np.arange(0, image_mask.shape[1], 1)
    plt.plot(x, mask_srez)

    plt.show()
