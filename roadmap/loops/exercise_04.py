# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

while True:
    try:
        int_num = int(input('>>> INTRODUZCA UN NÚMERO ENTERO POSITIVO:\n>>> '))
        if int_num > 0:
            print(f'>>>\n>>> SE LISTARÁ TODOS LOS NÚMEROS ENTEROS DESDE {int_num} HASTA 0:\n>>>')
            for i in range(int_num, -1, -1):
                print(f'>>> {i}')
            print('>>>\n>>> PROGRAMA FINALIZADO')
            break
        else:
            print('>>> ERROR: INGRESE SOLO NÚMEROS POSITIVOS')
    except ValueError:
        print('>>> ERROR: INGRESE ÚNICAMENTE NÚMEROS ENTEROS POSITIVOS')