# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

keep = str()

while keep != 'salir':
    entry = input('>>> INTRODUCE UNA FRASE:\n>>> ')
    if entry != 'salir':
        print(f'>>> {entry}')
    else:
        break