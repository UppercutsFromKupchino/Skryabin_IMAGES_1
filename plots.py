import matplotlib.pyplot as plt
import numpy as np


def make_plots(image, result_image):

    image_srez = [i for i in image[int(image.shape[0] / 2)]]
    res_srez = [i for i in result_image[int(result_image.shape[0] / 2)]]

    plt.subplot(211)
    x = np.arange(0, image.shape[1], 1)
    plt.plot(x, image_srez)

    plt.subplot(212)
    x = np.arange(0, image.shape[1], 1)
    plt.plot(x, res_srez)

    plt.show()
