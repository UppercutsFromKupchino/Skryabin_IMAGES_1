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
    mask = ((0, 1, 0), (1, -4, 1), (0, 1, 0))
    k = 1
    result_image = image.copy().astype(np.int32)

    for i in range(1, image.shape[0] - 2):
        for j in range(1, image.shape[1] - 2):

            z_x = 0

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    z_x += image[i + di][j + dj] * mask[1 + di][1 + dj]

            result_image[i][j] = image[i][j] - k * z_x

    for i in range(1, result_image.shape[0] - 2):
        for j in range(1, result_image.shape[1] - 2):
            result_image[i][j] += 553
            result_image[i][j] = int(result_image[i][j] / 5.5)

    print(min(result_image.ravel()))
    print(max(result_image.ravel()))

    result_image = result_image.astype(np.uint8)
    imshow('result-laplas', result_image)
    waitKey(0)
    imwrite(f'{text}-laplas.jpg', result_image)
    return result_image


if __name__ == '__main__':
    text_biba = 'photo'
    image_biba = load_image(text_biba)
    result = increase_sharpness_laplas(image_biba, text_biba)
    make_plots(image_biba, result)
