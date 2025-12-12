# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

'''
*
**
***
****
*****
'''

try:
    num = int(input('>>> INTRODUZCA UN NÚMERO ENTERO POSITIVO:\n>>> '))
    if num >= 0:
        print('>>>')
        for i in range(1, num + 1):
            print('>>> ', end=" ")
            print('*' * i)
        print('>>>')
except ValueError:
    print('>>> ERROR: INGRESE UNA CANTIDAD ENTERA POSITIVA')