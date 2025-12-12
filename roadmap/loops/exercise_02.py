while True:
    try:
        user_age = int(input('>>> INTRODUCE TU EDAD:\n>>> '))

        if 0 < user_age < 130:
            for i in range(user_age):
                print(f'>>> {i + 1}')
            break
        else:
            print('>>> ERROR: INTRODUCE UNA EDAD VÁLIDA ENTRE 1 Y 129')
    except ValueError:
        print('>>> ERROR: INTRODUCE SOLO NÚMEROS ENTEROS')