from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
arr_height = len(arr)
arr_width = len(arr[1])
i = 0
while i < arr_height:
    j = 0
    while j < arr_width:
        pixel_sum = 0
        for n in range(i, i + 10):
            for k in range(j, j + 10):
                r = int(arr[n][k][0])
                g = int(arr[n][k][1])
                b = int(arr[n][k][2])
                median = (r + g + b) / 3
                pixel_sum += median
        pixel_sum = int(pixel_sum // 100)
        for n in range(i, i + 10):
            for k in range(j, j + 10):
                arr[n][k][0] = int(pixel_sum // 50) * 50
                arr[n][k][1] = int(pixel_sum // 50) * 50
                arr[n][k][2] = int(pixel_sum // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
