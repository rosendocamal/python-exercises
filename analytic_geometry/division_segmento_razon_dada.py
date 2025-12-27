# Calcular las coordenadas que divide a un segmento en una razón dada

# Leer las coordenadas

def read_coordinates(name_point):
    while True:
        point = input(f'Escriba las coordenadas del punto {name_point}:\n{name_point} = ').replace('(', '').replace(')', '').replace(' ', '')

        try:
            coordinates = [str(name_point), [float(point[:point.index(',')]), float(point[point.index(',') + 1:])]]
            return coordinates
        except (ValueError, IndexError):
            print(f'ERROR: El punto {name_point} es inválido. Ingrese las coordenadas con el formato (a, b).')

# Coordenadas del punto medio

def get_midpoint(pointA, pointB):
    x1, y1 = pointA[1]
    x2, y2 = pointB[1]

    r = 1 / 2
    
    x_midpoint = r * (x1 + x2)
    y_midpoint = r * (y1 + y2)

    midpoint = ['Pm', [x_midpoint, y_midpoint]]

    return midpoint

# Coordenadas del punto que divide al segmento en una razón r

def get_point_ratio(pointA, pointB, r):
    x1, y1 = pointA[1]
    x2, y2 = pointB[1]

    x_point = r * (x2 - x1) + x1
    y_point = r * (y2 - y1) + y1

    point_r = ['P', [x_point, y_point]]

    return point_r

# Función principal
def main():
    while True:
        print('>>>>> DIVISIÓN DE UN SEGMENTO MEDIANTE UNA RAZÓN DADA')
        print('ELIGE UNA OPCIÓN:')
        print('[1] PUNTO MEDIO\n[2] PUNTO MEDIANTE UNA RAZÓN DADA\n[3] AYUDA\n[4] SALIR')

        while True:
            try:
                option = int(input('OPCIÓN: '))
                if 1 <= option <= 4:
                    break
                else:
                    print('ERROR: OPCIÓN INVÁLIDA. REINTENTE DE NUEVO\n')
            except ValueError:
                print('ERROR: OPCIÓN INVÁLIDAD. REINTENTE DE NUEVO\n')
            finally:
                print()
        
        if option == 1:
            point_a = read_coordinates('A')
            print(f'Has ingresado el punto {point_a[0]}({point_a[1][0]}, {point_a[1][1]}).')

            point_b = read_coordinates('B')
            print(f'Has ingresado el punto {point_b[0]}({point_b[1][0]}, {point_b[1][1]}).')

            midpoint = get_midpoint(point_a, point_b)

            print(f'El punto medio es {midpoint[0]} = ({midpoint[1][0]}, {midpoint[1][1]}).\n')

        elif option == 2:
            point_a = read_coordinates('A')
            print(f'Has ingresado el punto {point_a[0]}({point_a[1][0]}, {point_a[1][1]}).')

            point_b = read_coordinates('B')
            print(f'Has ingresado el punto {point_b[0]}({point_b[1][0]}, {point_b[1][1]}).')

            while True:
                try:
                    ratio = float(input('Ingrese la razón: '))
                    break
                except ValueError:
                    print('ERROR: El valor de la razón ingresada es incorrecta. Reintente de nuevo')

            point_ratio = get_point_ratio(point_a, point_b, ratio)

            print(f'El punto que divide al segmento {point_a[0], point_b[0]} en una razón de {ratio:.2f} es\n{point_ratio[0]}({point_ratio[1][0]}, {point_ratio[1][1]}).\n')
        elif option == 3:
            # Menú de Ayuda
            print('>>>>> MENÚ DE AYUDA')
            print('[1] PUNTO MEDIO\nSe solicita el ingreso de dos puntos (pares ordenados) con el formato (x, y). Donde x es el valor positivo/negativo/origen de la abscisa e y el valor positivo/negativo/origen de la ordenada. Una vez ingresado el punto o par ordenado, se mostrará por pantalla el valor del punto. Posteriormente se hace el cálculo de las coordenadas del punto medio.')
            print('[2] PUNTO MEDIANTE UNA RAZÓN DADA\nSe solicita el ingreso de dos puntos (pares ordenados) con el formato (x, y). Donde x es el valor positivo/negativo/origen de la abscisa e y el valor positivo/negativo(origen de la ordenada. Una vez ingresado el punto o par ordenado, se mostrará por pantall el valor del punto ingresado.. Inmediatamente se solicitará el ingreso de una razón dada para calcular el punto que divide al segmento que conforman los dos puntos ingresados mediante dicha razón. Posteriormente se calcula el valor de las coordenads de ese punto.')
            print('[3] AYUDA\nSe muestra el menú de ayuda.')
            print('[4] SALIR\nSe solicita cerrar el programa y se finaliza el programa.\n')
        elif option == 4:
            print('Cerrando programa...')
            break

if __name__ == '__main__':
    main()
