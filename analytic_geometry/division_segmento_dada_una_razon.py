# Determina la razón r = [distance(p1, p) / distance(p, p2)] en que p divide el segmento de recta de extremos p1 y p2

# Estructura [p1, p2, p]
datos = [[(0,2), (-2,4), (2,0)],
        [(-1,4), (0,3), (3,0)],
        [(3,-4), (0,2), (2,-2)],
        [(3,5), (-1, 4), (-5,3)],
        [(0.5,0.75), (2,1), (1/3,13/18)],
        [(-5,1), (4,3), (-3,13/19)]]

def ratio(p1, p2, p, axis):
    """
        Los puntos p1, p2 son los extremos de la recta
        El punto p divide la recta en una razón dada
        El parámetro axis indica si la coordenada x o y a evaluar
        La función retorna la razón en la que p divide la recta de p1 a p2
        La función retorna 0 si los parámetros son incorrectos
    """  

    if axis == 0 or axis == 1:
        try:
            r = (p[axis] - p1[axis]) / (p2[axis] - p[axis])
            return round(r, 3)
        except ZeroDivisionError:
            return None
    return None

def main():
    for dato in datos:
        r_x = ratio(*dato, 0)
        r_y = ratio(*dato, 1)
        
        if r_x is not None and r_y is not None:
            if r_x == r_y:
                print(r_x)
            else:
                print(f'ADVERTENCIA: Los datos p1{dato[0]}, p2{dato[1]} y p{dato[2]} indica que no son colineales.')
        elif r_x is not None:
            print(r_x)
        elif r_y is not None:
            print(r_y)
        else:
            print(f'ADVERTENCIA: Los datos p1{dato[0]}, p2{dato[1]} y p{dato[2]} causan conflictos.')

if __name__ == '__main__':
    main()
