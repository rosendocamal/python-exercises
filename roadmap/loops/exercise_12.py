# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

while True:
    phrase = input('>>> ESCRIBA UNA FRASE:\n>>> ').strip()
    if bool(phrase):
        break
    else:
        print('>>> ERROR: INGRESE UNA FRASE PARA CONTINUAR')

while True:
    letter = input('>>> ESCRIBA UNA LETRA:\n>>> ').strip()
    if letter.isalpha() and len(letter) == 1:
        break
    else:
        print('ERROR: INGRESE UNA LETRA PARA CONTINUAR')

letter_in_phrase = phrase.count(letter)

print(f'>>> {letter_in_phrase}')