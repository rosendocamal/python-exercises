'''
Encuentra el conjunto de verdad de Q(n) si el dominio de n es Z.
Sea Q(n) el predicado "n² <= 30"
'''

# Primer intento:
# Se halla n a través de Q(n)

# Debido a que cualquier n < 0 su cuadrado es positivo
# Nos limitamos a los positivos y hallamos su valor opuesto

start = 0
end = 10 ** 2

conjunto_verdad = list()

for i in range(start, end + 1):
    if i ** 2 <= 30:
        conjunto_verdad.append(i)
    if -i ** 2 <= 30:
        conjunto_verdad.append(-i)

conjunto_verdad.sort()
print(f'Conjunto de verdad para Q(n) y el dominio de n es Z: {conjunto_verdad}')
