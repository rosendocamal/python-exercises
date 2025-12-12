def get_name_student():
    while True:
        name_student = input('INGRESE SU PRIMER NOMBRE:\n')
        if bool(name_student):
            return name_student.strip().lower()[0]
        else:
            print('INGRESE UN NOMBRE VÁLIDO PARA CONTINUAR')

def get_sex_student():
    while True:
        sex_student = input('SEXO (M/F):\n')
        if bool(sex_student):
            sex_student = sex_student.strip().lower()
            if sex_student == 'f':
                return 'MUJER'
            elif sex_student == 'm':
                return 'HOMBRE'
            else:
                print('INGRESE UN SEXO VÁLIDO')
        else:
            print('INGRESE UN SEXO VÁLIDO PARA CONTINUAR')

def get_group(name_student, sex_student):
    characters = 'aábcdeéfghiíjklmnñoópqrstuúüvwxyz'
    group_student = 'NO ESTÁ DEFINIDO'

    if sex_student == 'MUJER':  
        if name_student in characters[:15]:
            group_student = 'A'
        else:
            group_student = 'B'
    
    if sex_student == 'HOMBRE':
        if name_student in characters[16:]:
            group_student = 'A'
        else:
            group_student = 'B'

    return group_student

name = get_name_student()
sex = get_sex_student()
group = get_group(name, sex)
print(f'GRUPO: {group}')