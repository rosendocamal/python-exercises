# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

month_and_days = {
    1:  ["enero", 31],
    2:  ["febrero", 28],  # O 29 en años bisiestos
    3:  ["marzo", 31],
    4:  ["abril", 30],
    5:  ["mayo", 31],
    6:  ["junio", 30],
    7:  ["julio", 31],
    8:  ["agosto", 31],
    9:  ["septiembre", 30],
    10: ["octubre", 31],
    11: ["noviembre", 30],
    12: ["diciembre", 31],
}
date = input('>>> Introduzca la fecha (dd/mm/aaaa):\n>>> ').strip()

if len(date) == 10:
    try:
        day, month, year = int(date[:2]), int(date[3:5]), int(date[6:])

        # Validación del año
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            is_leap_year = True
        else:
            is_leap_year = False

        # Validación del mes
        if 1 <= month <= 12:

            # Validación del día:
            if month == 2 and is_leap_year:
                if 1 <= day <= (month_and_days[month][1] + 1):
                    print(f'>>> {day} de {month_and_days[month][0]} de {year}')
                else:
                    print('>>> ERROR: El número del día es inválido, la fecha introducida es incorrecta')
            else:
                if 1 <= day <= month_and_days[month][1]:
                    print(f'>>> {day} de {month_and_days[month][0]} de {year}')
                else:
                    print('>>> ERROR: El número del día es inválido, la fecha introducida es incorrecta')

        else:
            print('>>> ERROR: El mes es inválido, la fecha introducida es incorrecta')

    except ValueError:
        print('>>> ERROR: La fecha es inválida o no cumple con el formato dd/mm/aaaa')
else:
    print('>>> ERROR: La fecha es inválida o no cumple con el formato dd/mm/aaaa')

    