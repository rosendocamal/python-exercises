# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

import math

while True:
    try:
        num = int(input('>>> ESCRIBA UN NÚMERO ENTERO POSITIVO:\n>>> '))

        if num > 1:
            k = math.isqrt(num)
            is_prime_num = True

            for i in range(2, k + 1):
                if num % i == 0:
                    is_prime_num = False
                    break # Al detectar un divisor adicional se considera no primo

            if is_prime_num:
                print(f'>>> EL NÚMERO {num} ES UN NÚMERO PRIMO')
            else:
                print(f'>>> EL NÚMERO {num} NO ES UN NÚMERO PRIMO')
            break
        else:
            print('>>> ERROR: INTRODUZCA UN NÚMERO ENTERO POSITIVO MAYOR A 1')
    except ValueError:
        print('>>> ERROR: INTRODUZCA UN NÚMERO ENTERO POSITIVO')