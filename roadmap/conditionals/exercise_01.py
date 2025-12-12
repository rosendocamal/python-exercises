LEGAL_AGE = 18
try:
    age_user = int(input('INTRODUZCA SU EDAD: \n'))
except ValueError:
    print('REINTENTE DE NUEVO')
    print('INGRESE UNA EDAD VÁLIDA PARA CONTINUAR')
else:
    if age_user >= LEGAL_AGE:
        print('USTED ES MAYOR DE EDAD')
    else:
        print('USTED NO ES MAYOR DE EDAD')