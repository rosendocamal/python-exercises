# Cálculo de inclinación y pendiente de una recta

import math

# Leer y obtener las pares ordenados de una recta
def read_ordered_pair(name_point):
    while True:
        point = input(f'Coordenadas del punto {name_point}:\n{name_point} = ').strip("( )").split(",")
        try:
            return [float(point[0]), float(point[1])]
        except (ValueError, IndexError):
            print(f'ERROR: El punto {name_point} es inválido. El formato de coordenada es: (a, b).')

# Obtener la pendiente de una recta en base a 2 puntos de la recta
def get_slope(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b

    delta_y = y2 - y1
    delta_x = x2 - x1
    
    try:
        slope = delta_y / delta_x
        return slope
    except ZeroDivisionError:
        return math.nan

# Obtener la inclinación de una recta dada su pendiente
def get_inclination(slope):
    if isinstance(slope, float):
        return math.atan(slope)
    return (math.pi / 2)

# Presentar resultados
def main():
    while True:
        print('----- INCLINACIÓN Y RECTA DE UNA PENDIENTE')
        print('----- MENÚ')
        print('Elige una opción:\n[1] Cálculo de Pendiente de una Recta\n[2] Cálculo de Inclinación dada su Pendiente\n[3] Ayuda\n[4] Salir')
        option = int(input('Opción a elegir: '))
        print()

        if option == 1:
            print('----- CÁLCULO DE PENDIENTE')
            print('Introduzca las coordenadas de 2 puntos de la recta.\n')

            p1 = read_ordered_pair('A')
            p2 = read_ordered_pair('B')
            
            m = get_slope(p1, p2) # Pendiente de la recta

            print(f'La pendiente es: {m}\n')
            
        elif option == 2:
            print('----- CÁLCULO DE INCLINACIÓN')
            print('Introduzca la pendiente de la recta para conocer su inclinación.')

            while True:
                try:
                    slope = float(input('Pendiente: '))
                    theta = get_inclination(slope)
                    print(f'El álgulo de inclinación es: {theta} rad.\n')
                    break
                except ValueError:
                    print('ERROR: Valor de la pendiente no válida.')
                
        elif option == 3:
            print('---- AYUDA')
            print('\n[1] Cálculo de Pendiente de una Recta\nSe solicita ingresar dos puntos de la recta.\nSe ingresa de manera individual un punto de la recta como par ordenado de la forma (a, b).\nLa pendiente se muestra con números decimales y no como un número racional (fracción)')
            print('\n[2] Cálculo de Inclinación dada su Pendiente\nSe solicita ingresar el valor de la pendiente y se muestra el ángulo de inclinación en radianes.')
            print('\n[3] Ayuda\nMenú de ayuda')
            print('\n[4] Salir\nSe cierra el programa.')
            print('\n')

        elif option == 4:
            print('----- SALIR')
            print('Cerrando programa...')
            break
        else:
            print('La opción es inválida')

if __name__ == '__main__':
    main()
