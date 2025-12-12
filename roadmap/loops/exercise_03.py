# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

while True:
    try:
        int_num = int(input('>>> INTRODUZCA UN NÚMERO ENTERO POSITIVO:\n>>> '))
        if int_num > 0:
            print(f'>>>\n>>> SE LISTARÁ TODOS LOS NÚMEROS IMPARES DESDE 1 HASTA {int_num}:\n>>>')
            print('>>> ', end=' ')
            for i in range(1, int_num + 1, 2):
                if i + 2 > int_num:
                    print(i)
                else:
                    print(f'{i}', end=', ')
            break
        else:
            print('>>> ERROR: INGRESA SOLO CANTIDADES POSITIVAS')
    except ValueError:
        print('>>> ERROR: INGRESA SOLO NÚMEROS ENTEROS POSITIVOS')

