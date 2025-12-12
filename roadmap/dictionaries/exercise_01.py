# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = {"Euro": "€", "Dollar": "$", "Yen": "¥"} # Diccionario con los símbolos de las divisas

while True:
    input_divisa = input('>>> INGRESE UNA DIVISA:\n>>> ').strip().capitalize() # Solicitud al usuario de una divisa

    # Se valida que la entrada sea correcta y se busca en el diccionario la divisa ingresada, de lo contrario se notifica al usuario
    if input_divisa.isalpha():
        if input_divisa in divisas:
            print(f'>>> SÍMBOLO DE LA DIVISA: {divisas[input_divisa]}')
        else:
            print('>>> LA DIVISA NO ESTÁ EN EL DICCIONARIO')
    else:
        print('>>> ERROR: INGRESE EL NOMBRE DE UNA DIVISA PARA CONTINUAR')


    # Se evalúa si el usuario desea continuar con el programa o finalizar
    continue_program = input('>>> ¿DESEA CONTINUAR [Y/n]?').strip().lower()

    if continue_program == 'n':
        break