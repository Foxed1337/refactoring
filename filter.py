import math

import numpy as np
from PIL import Image


def get_size_from_input(input_parameters: str, img_width: int, img_height: int):
    input_parameters = input_parameters.split()
    if len(input_parameters) == 1 and input_parameters[0].endswith('px'):
        pixels_count = int(input_parameters[0][0:-2])

        if pixels_count < 1:
            raise ValueError('Количество пикселей меньше 1.')

        pixel_side = int(math.sqrt((img_width * img_height) / pixels_count))
        return [pixel_side, pixel_side]

    if len(input_parameters) > 0:
        if input_parameters[0].endswith('%'):
            first_side = int(img_width / 100 * int(input_parameters[0][0:-1]))
        else:
            first_side = int(input_parameters[0])

        if first_side < 1:
            raise ValueError('Ширина пикселя меньше 1.')

        second_side = first_side
        if len(input_parameters) > 1:
            if input_parameters[1].endswith('%'):
                first_side = int(img_height / 100 * int(input_parameters[1][0:-1]))
            else:
                first_side = int(input_parameters[1])
            if second_side < 1:
                raise ValueError('Высота пикселя меньше 1.')
        return [first_side, second_side]

    raise ValueError('Ошибка ввода')


def get_filtered_array(array: np.ndarray, arr_height: int, arr_width: int, pixel_height, pixel_width, gray_step):
    for i in range(0, arr_height, pixel_height):
        for j in range(0, arr_width, pixel_width):
            if j + pixel_width > arr_width:
                dx = arr_width - j
            else:
                dx = pixel_width

            if i + pixel_height > arr_height:
                dy = arr_height - i
            else:
                dy = pixel_height
           
            array[i:i + dy, j:j + dx] = int(array[i:i + dy, j:j + dx].sum() / 3 // (dy * dx)) // gray_step * gray_step
    return array


img = Image.open("img2.jpg")
arr = np.array(img)
arr_height = len(arr)
arr_width = len(arr[1])

pixel_height, pixel_width = get_size_from_input(input("Введите ширину и высоту пикселей: "), arr_width, arr_height)
grad_step = 256 // int(input("Введите шаг : "))
extension = input("Введите расширение выходного файла: ")

res = Image.fromarray(get_filtered_array(arr, arr_height, arr_width, pixel_height, pixel_width, grad_step))
res.save(f'res.{extension}')
