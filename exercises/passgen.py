import string, random

# Establecer el tamaño de la contraseña
password_length = int(input("Introduzca el tamaño de la contraseña:\n"))

# Genera los caracteres a emplear en la generación de la contraseña
characters = string.ascii_letters + string.digits + string.punctuation

# Selecciona de manera aleatoria los caracteres de la contraseña y genera la contraseña
password = "".join(random.choice(characters) for i in range(password_length))

# Muestra al usuario por consola la contraseña generada
print(f"La contraseña generada es: {password}")