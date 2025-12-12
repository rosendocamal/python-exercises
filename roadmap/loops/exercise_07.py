# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def show_multiplication_table(multiplicand):
    print(f'>>> TABLA DE MULTIPLICAR DEL {multiplicand}\n>>>')
    for multiplier in range(1, 11):
        print(f'>>> {multiplicand:2} X {multiplier:2} = {multiplicand * multiplier:3}')
    print('>>> ' + '-' * 25)

for i in range(1, 11):
    show_multiplication_table(i)