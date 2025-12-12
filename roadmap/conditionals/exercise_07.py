try:
    while True:
        income_user = float(input('INTRODUZCA EL MONTO DE SUS INGRESOS:\n$'))
        if income_user >= 0:
            if income_user < 10000:
                tax_rate = 0.05
            elif income_user <= 20000:
                tax_rate = 0.15
            elif income_user <= 35000:
                tax_rate = 0.20
            elif income_user <= 60000:
                tax_rate = 0.30
            elif income_user > 60000:
                tax_rate = 0.45
            
            print(f'LE CORRESPONDE EL {tax_rate * 100}% DE TIPO IMPOSITVO')
            
            break
        else:
            print('EL MONTO DE LOS INGRESOS NO PUEDEN SER NEGATIVOS')
except ValueError:
    print('REINTENTE DE NUEVO')

