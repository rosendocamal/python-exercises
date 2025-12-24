# Cálculo de distancias entre puntos (pares ordenados)

import math
import matplotlib.pyplot as plt

def read_ordered_pair(point):
    # Leer y guardar las coordenadas de un punto
    while True:
        user_input = input(f'Escriba las coordenadas del punto {point}.\n(a,b): ')
        try:
            point = user_input.strip("()").split(",")
            ordered_pair = (float(point[0]), float(point[1]))
            return ordered_pair
        except (ValueError, IndexError):
            print(f'Error: "{user_input}" es inválido. Utilice el formato (a,b)')

def get_distances(pointA, pointB):
    """
    Ingresar primero el pointA y luego el pointB si:
    - Pertenece a un segmento horizontal y pointA es el par ordenado que está a la izquierda
    - Pertenece a un segmento vertical y pointA es el par ordenado inferior
    - Es indistinto si se trata de un segmento inclinado
    """
    x1, y1 = pointA
    x2, y2 = pointB

    # Cálculo de distancia de segmento horizontal
    if y2 == y1: # Si las ordenadas de los puntos son iguales
        return abs(x2 - x1)

    # Cálculo de distancia de segmento vertical
    if x2 == x1: # Si las abscisas de los puntos son iguales
        return abs(y2 - y1)

    # Cálculo de distancia de segmento inclinado
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def show_graphic(pointA, pointB, distance):
    x1, y1 = pointA
    x2, y2 = pointB

    fig, ax = plt.subplots()

    # Ubicación gráfica de los pares ordenados
    ax.scatter(x = [x1, x2], y = [y1, y2], color='blue', s=50)

    # Segmento de los pares ordenados
    ax.plot([x1, x2], [y1, y2], label=f'Distancia: {distance:.2f}')

    # Nombrar cada par ordenado
    ax.annotate(
            f'A = ({x1}, {y1})',
            (x1, y1),
            textcoords='offset points',
            xytext=(5,5),
            ha='center',
            fontsize=9
            )
    ax.annotate(
            f'B = ({x2}, {y2})',
            (x2, y2),
            textcoords='offset points',
            xytext=(5,5),
            ha='center',
            fontsize=9
            )
    
    # Personalización del gráfico
    margin = 2
    ax.set_xlim(min(x1, x2, 0) - margin, max(x1, x2, 0) + margin)
    ax.set_ylim(min(y1, y2, 0) - margin, max(y1, y2, 0) + margin)
    ax.axhline(0, color='black', linewidth=0.8, zorder=0) # Eje X
    ax.axvline(0, color='black', linewidth=0.8, zorder=0) # Eje Y
    ax.grid(True, linestyle=':', alpha=0.6) # Añade rejilla

    # Etiqueta y título
    ax.set_title('Distancia entre 2 puntos')
    ax.legend()

    # Mostrar gráfico
    plt.show()
    

def main():
    # Pares ordenados
    point_A = read_ordered_pair("A")
    point_B = read_ordered_pair("B")

    distance_AB = get_distances(point_A, point_B)
    print(f"La distancia de los puntos es: {distance_AB:.2f}")

    show_graphic(point_A, point_B, distance_AB)

if __name__ == "__main__":
    main()
