# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

while True:
    word = input('>>> INGRESE UNA PALABRA:\n>>> ').strip()

    if word.isalpha():
        print(f'>>> SE IMPRIMIRÁ LETRA POR LETRA LA PALABRA "{word}":\n>>>')
        for letter in word[::-1]:
            print(f'>>> {letter}')
        break
    else:
        print('>>> ERROR: ESCRIBA UNA SOLA PALABRA')