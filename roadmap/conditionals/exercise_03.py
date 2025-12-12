msg = 'POR FAVOR, INGRESE UN NÚMERO VÁLIDO PARA CONTINUAR'

while True:
    try:
        dividend = float(input('INGRESE UN PRIMER NÚMERO:\n'))
        break
    except ValueError:
        print(msg)

while True:
    try:
        divisor = float(input('INGRESE UN SEGUNDO NÚMERO:\n'))
        if divisor != 0:
            break
        else:
            print('INGRESE UN NÚMERO DISTINTO DE CERO PARA CONTINUAR')
    except ValueError:
        print(msg)

quotient = dividend / divisor

print(f'{dividend} / {divisor} = {quotient}')