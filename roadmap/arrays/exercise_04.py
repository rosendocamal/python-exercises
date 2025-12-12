# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

while True:
    word = input('>>> ESCRIBA UNA PALABRA:\n>>> ').strip()

    if word.isalpha():
        vowels = [['a', 0], ['e', 0], ['i', 0], ['o', 0], ['u', 0]]
        for letter in word.lower():
            for vowel in vowels:
                if letter == vowel[0]:
                    vowel[1] += 1

        print(f'>>> LA PALABRA "{word}" CONTIENE LA SIGUIENTE CANTIDAD DE VOCALES:\n>>>')
        for vowel in vowels:
            print(f'>>> VOCAL "{vowel[0]}": {vowel[1]}')
        
        stop_program = input('>>>\n>>> ¿DESEA SALIR DEL PROGRAMA [Y/n]? ')
        if stop_program.strip().lower() == 'y':
            print('>>> GRACIAS POR USAR EL PROGRAMA...')
            break
    else:
        print('>>> ERROR: INTRODUZCA UNA ÚNICA PALABRA')