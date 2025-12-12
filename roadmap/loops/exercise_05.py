# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

while True:
    try:
        initial_capital = float(input('>>> INTRODUZCA EL MONTO A INVERTIR:\n>>> $'))
        if initial_capital >= 0:
            break
        else:
            print('>>> ERROR: INGRESE UNA CANTIDAD A INVERTIR MAYOR O IGUAL A 0')
    except ValueError:
        print('>>> ERROR: INGRESE UN NÚMERO POSITIVO')

while True:
    try:
        annual_interest = float(input('>>> INTRODUZCA LA TASA DE INTERÉS ANUAL(%):\n>>> '))
        break
    except ValueError:
        print('>>> ERROR: INGRESE ÚNICAMENTE UN NÚMERO')

while True:
    try:
        years_investment = int(input('>>> INTRODUZCA EL NÚMERO DE AÑOS DE TENENCIA:\n>>> '))
        if years_investment >= 0:
            break
        else:
            print('>>> ERROR: INGRESE UN NÚMERO ENTERO POSITIVO COMO PERIOD DE AÑOS')
    except ValueError:
        print('>>> ERROR: INGRESE UN NÚMERO ENTERO POSITIVO')

print(f'>>> RESULTADOS DE LA INVERSIÓN DURANTE {years_investment} AÑOS:\n>>>')

for i in range(1, years_investment + 1):
    final_capital = initial_capital * (1 + annual_interest / 100) ** i
    print(f'>>> AÑO {i}: ${final_capital:,.2f}')