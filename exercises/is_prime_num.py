"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

import math

def is_prime_num(num):
    if num >= 2:
        sqrt_num = int(math.sqrt(num))
    
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                return False

        return True
    else:
        return False

def get_nums(function, t_min, t_max):
    nums = [num for num in range(t_min, t_max + 1) if function(num)]

    return nums

def main():
    prime_nums = get_nums(is_prime_num, 1, 100)

    print(f'Números primos entre 1 y 100: {prime_nums})')


if __name__ == "__main__":
    main()
