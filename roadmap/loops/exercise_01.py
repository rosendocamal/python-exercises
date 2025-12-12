def repeat_word(num):
    while True:
        user_word = input('>>> INTRODUZCA UNA PALABRA:\n>>> ').strip()

        if user_word.isalpha():
            print(f'>>> "{user_word}" SE REPETIRÁ {num} VECES:\n')
            for i in range(num):
                print(f'>>> {i + 1}. {user_word}')
            
            break
        else:
            print('>>> ERROR: INGRESE SOLO LETRAS (SIN NÚMEROS NI SÍMBOLOS).')

repeat_word(10)