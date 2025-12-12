# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

prices = [50, 75, 46, 22, 80, 65, 8]

'''
prices.sort()

print(f'>>> EL PRECIO MENOR ES ${prices[0]}\n>>> EL PRECIO MAYOR ES ${prices[len(prices) - 1]}')
'''

print(f'>>> EL PRECIO MENOR ES ${min(prices)}\n>>> EL PRECIO MAYOR ES ${max(prices)}')