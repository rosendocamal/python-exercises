# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

'''
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

try:
    int_num = int(input('>>> INTRODUZCA UN NÚMERO ENTERO POSITIVO:\n>>> '))
    print('>>>')
    if int_num > 0:
        for i in range(1, int_num + 1, 2):
            print('>>> ', end='')
            for j in range(i, 0, -2):
                print(j, end=' ')
            print()
    else:
        print('>>> ERROR: INGRESE UNA CANTIDAD POSITIVA')
except ValueError:
    print('>>> ERROR: INGRESE UNA CANTIDAD POSITIVA ENTERA')
