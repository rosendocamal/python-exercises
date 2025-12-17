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

# Determinar si un número es primo o no
def is_prime_num(num):
    if num < 2:
        return False

    sqrt_num = int(math.sqrt(num))
    
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            return False

    return True

# Obtener una serie de números primos
def get_nums(function, t_min, t_max):
    nums = [num for num in range(t_min, t_max + 1) if function(num)]

    return nums

# Obtener el mcd del alto y ancho de una imagen
def mcd(width, height):  
    # Obtener los factores (divisores) de un número
    def get_factors(num):
        prime_nums = get_nums(is_prime_num, 1, num)

        divider = prime_nums[0]
        factors_num = list()

        while num != 1:
            if num % divider == 0:
                num = num / divider
                factors_num.append(divider)
            else:
                for i in range(1, len(prime_nums)):
                    divider = prime_nums[i]
                    
                    if num % divider == 0:
                        num = num / divider
                        factors_num.append(divider)
                        divider = prime_nums[0]
                        break

        factors_num.sort()
        return factors_num

    factors_width = get_factors(width) # Divisores de width
    factors_height = get_factors(height) # Divisores de height

    factors = set(factors_width + factors_height) # Todos los divisores únicos de width más los de height
    
    # Diccionario con todos los divisores de width y height con el formato "divisor":"exponente"
    num_factors = { i:min(factors_width.count(i), factors_height.count(i)) for i in factors }

    # Mínimo común divisor
    mcd = 1
    for i in num_factors.keys():
        mcd *= i ** num_factors[i]

    return mcd


# Obtener el aspect ratio de una imagen
def aspect_ratio(width, height, mcd):
    width = int(width / mcd)
    height = int(height / mcd)

    print(f"The aspect ratio is {width}:{height}.")

def main():
    # URL de la imagen.
    img_src = "https://www.python.org/static/img/python-logo.png"

    # Imagen obtenida para ser manipulada.
    response = req.get(img_src)
    img = Image.open(BytesIO(response.content))

    # Obtener el valor del ancho y alto de la imagen.
    width, height = img.width, img.height

    aspect_ratio(width, height, mcd(width, height))


if __name__ == "__main__":
    main()
