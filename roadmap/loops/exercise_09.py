# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


# Programa que solicita una contraseña hasta que sea correcta o al agotar los intentos posibles

from getpass import getpass

passwd = 'contraseña' # Contraseña almacenada

attempts = 3 # Número máximo de intentos

while attempts > 0:
    password_entered = getpass('>>> ESCRIBE TU CONTRASEÑA:\n>>> ')
    if password_entered == passwd:
        print('>>> TE DAMOS LA BIENVENIDA')
        break
    else:
        attempts -= 1 # Reducción de intentos al fallar
        if attempts > 0:
            print('>>> LA CONTRASEÑA ES INCORRECTA. INTÉNTELO DE NUEVO')
        else:
            print('>>> VARIOS INTENTOS FALLIDOS. REINTENTE MÁS TARDE')