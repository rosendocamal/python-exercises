# Dados los extremos p1, p2 y la razón dada, encuentra las coordenadas del punto de división de p del Segmento(p1, p2)

# Estructura [p1, p2, r]
datos = [[(4,1), (5,-2), -2],
         [(0,5), (6,-1), 5],
         [(-2,3), (4,5), 2/3],
         [(-2/3,0), (0,4), 1/2],
         [(5,-6), (1,0), 1/3]]

def par_ordered(p1, p2, r):
    # ADVERTENCIA: No tolera edge cases
    x1, y1 = p1
    x2, y2 = p2

    x = round((x1 + x2 * r) / (1 + r), 2)
    y = round((y1 + y2 * r) / (1 + r), 2)

    return (x, y)

def main():
    for dato in datos:
        p = par_ordered(*dato)
        print(p)

if __name__ == '__main__':
    main()
