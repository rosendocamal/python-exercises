# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

courses = {
        'Matemáticas': 6,
        'Física': 4,
        'Química': 5
        }

total_score = 0

for subject in courses.keys():
    total_score += courses[subject]
    print(f'{subject} tiene {courses[subject]} créditos.')

print(f'{total_score} créditos totales del curso.')
