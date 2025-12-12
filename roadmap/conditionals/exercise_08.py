try:
    score_employee = float(input('INGRESE LA PUNTUACIÓN DEL EMPLEADO:\n'))
    if score_employee == 0 or score_employee == 0.4 or score_employee == 0.6 or score_employee > 0.6:
        BONUS = 2400
        if score_employee == 0:
            performance_employee = 'INACEPTABLE'
        elif score_employee == 0.4:
            performance_employee = 'ACEPTABLE'
        elif score_employee >= 0.6:
            performance_employee = 'MERITORIO'
        print(f'EL EMPLEADO MANTIENE UN REDIMIENTO {performance_employee}\nEL EMPLEADO OBTIENE UN BONO DE ${BONUS * score_employee}')
    else:
        print('REINTENTE DE NUEVO. VALORES INCORRECTOS')
except ValueError:
    print('REINTENTE DE NUEVO. INGRESE VALORES NÚMERICOS')