# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

import string

alphabet = list(string.ascii_lowercase)

for i in range(len(alphabet)):
    if (i + 1) % 3 == 0:
        alphabet[i] = str()

for letter in alphabet:
    if letter == str():
        alphabet.remove(str())

print(alphabet)