"""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://www.python.org/static/img/python-logo.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
"""

import math
import requests as req
from PIL import Image
from io import BytesIO

# URL de la imagen.
img_src = "https://www.python.org/static/img/python-logo.png"

# Imagen obtenida para ser manipulada.
response = req.get(img_src)
img = Image.open(BytesIO(response.content))

# Obtener el valor del ancho y alto de la imagen.
width, height = img.width, img.height

print(width, height)
# Calculando el aspect ratio

def is_prime_num(num):
    if num < 2:
        return False

    sqrt_num = int(math.sqrt(num))
    
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            return False

    return True

def get_nums(function, t_min, t_max):
    nums = [num for num in range(t_min, t_max + 1) if function(num)]

    return nums

def mcd(w, h):  
    prime_nums = get_nums(is_prime_num, 1, w)

    temp = w
    divider = prime_nums[0]
    dividers_w = list()
    
    while temp != 1:
        if temp % divider == 0:
            temp = temp / divider
            dividers_w.append(divider)
            divider = prime_nums[0]
        elif temp % divider != 0:
            for i in range(1, len(prime_nums)):
                divider = prime_nums[i]
                if temp % divider == 0:
                    temp = temp / divider
                    dividers_w.append(divider)
                    divider = prime_nums[0]
                    break

    prime_nums = get_nums(is_prime_num, 1, h)

    temp = h
    divider = prime_nums[0]
    dividers_h = list()
    
    while temp != 1:
        if temp % divider == 0:
            temp = temp / divider
            dividers_h.append(divider)
            divider = prime_nums[0]
        elif temp % divider != 0:
            for i in range(1, len(prime_nums)):
                divider = prime_nums[i]
                if temp % divider == 0:
                    temp = temp / divider
                    dividers_h.append(divider)
                    divider = prime_nums[0]
                    break 

    dividers_w.sort()
    dividers_h.sort()

    dividers = set(dividers_w + dividers_h)
    
    total_factors = dict()

    for i in dividers:
        total_factors[i] = min(dividers_w.count(i), dividers_h.count(i))

    mcd = 1
    for i in total_factors.keys():
        mcd *= i ** total_factors[i]


    return mcd

def aspect_ratio(w, h, mcd):
    weigth = int(w / mcd)
    height = int(h / mcd)

    print(f"The aspect ratio is {weigth}:{height}.")


aspect_ratio(width, height, mcd(width, height))
