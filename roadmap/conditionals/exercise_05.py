MIN_AGE = 16
MIN_INCOME = 1000

while True:
    try:
        age_user = int(input('INTRODUZCA SU EDAD:\n')) 
        if age_user > 0 and age_user < 130:
            break
        else:
            print('INTRODUZCA UNA EDAD MAYOR A 0 Y MENOR A 130')
    except ValueError:
        print('INGRESE UNA EDAD VÁLIDA PARA CONTINUAR')
    
while True:
    try:
        monthly_income = float(input('INTRODUZCA SUS INGRESOS MENSUALES:\n$'))
        if monthly_income >= 0:
            break
        else:
            print('EL MONTO DE LOS INGRESOS MENSUALES NO PUEDEN SER NEGATIVOS')
    except ValueError:
        print('INGRESE UNA CANTIDAD VÁLIDA PARA CONTINUAR')

if age_user >= MIN_AGE and monthly_income >= MIN_INCOME:
    print('USTED ESTÁ SUJETO A TRIBUTACIÓN')
else:
    print('USTED NO ESTÁ SUJETO A TRIBUTACIÓN')