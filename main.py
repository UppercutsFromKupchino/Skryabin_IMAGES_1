from cv2 import imread, imshow, imwrite, waitKey, IMREAD_GRAYSCALE, resize
import numpy as np
from plots import make_plots


# Загрузка изображения
def load_image(text):
    text += '.jpg'
    image = imread(f'{text}', IMREAD_GRAYSCALE)
    return image


# Лаплас 3x3
def increase_sharpness_laplas(image, text):
    mask_laplas = ((0, 1, 0), (1, -4, 1), (0, 1, 0))
    k = 1
    result_image = image.copy().astype(np.int32)

    for i in range(1, image.shape[0] - 2):
        for j in range(1, image.shape[1] - 2):

            z_x = 0

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    z_x += image[i + di][j + dj] * mask_laplas[1 + di][1 + dj]

            result_image[i][j] = image[i][j] - k * z_x
    min_result_image = min(result_image.ravel())
    coeff = (max(result_image.ravel()) + abs(min_result_image)) / 256

    for i in range(1, result_image.shape[0] - 2):
        for j in range(1, result_image.shape[1] - 2):
            result_image[i][j] += abs(min_result_image)
            result_image[i][j] = int(result_image[i][j] / coeff)

    result_image = result_image.astype(np.uint8)
    imshow('result-laplas', result_image)
    waitKey(0)
    imwrite(f'{text}-laplas.jpg', result_image)
    return result_image


# Обработка изображения методом нечёткого маскирования
def mask(image, text):
    result_image = image.copy()
    result_image = result_image.astype(np.int32)
    mask_gauss = ((1, 2, 1), (2, 4, 2), (1, 2, 1))
    k = 9

    for i in range(1, image.shape[0] - 2):
        for j in range(1, image.shape[1] - 2):

            z_gaussian = 0

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    z_gaussian += image[i + di][j + dj] * mask_gauss[1 + di][1 + dj]
            result_image[i][j] = z_gaussian + 2 * (image[i][j] - z_gaussian)

    min_result_image = min(result_image.ravel())
    coeff = (max(result_image.ravel()) + abs(min_result_image)) / 256

    for i in range(1, result_image.shape[0] - 2):
        for j in range(1, result_image.shape[1] - 2):
            result_image[i][j] += abs(min_result_image)
            result_image[i][j] = int(result_image[i][j] / coeff)

    result_image = result_image.astype(np.uint8)
    imshow('result-mask', result_image)
    waitKey(0)
    imwrite(f'{text}-mask.jpg', result_image)
    return result_image


if __name__ == '__main__':
    text_biba = 'polyana'
    image_biba = load_image(text_biba)
    result_laplas = increase_sharpness_laplas(image_biba, text_biba)
    result_mask = mask(image_biba, text_biba)
    make_plots(image_biba, result_laplas, result_mask)
