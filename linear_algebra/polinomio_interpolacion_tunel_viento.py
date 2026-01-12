"""
Ejercicio 34 de la sección 1.2 de
Álgebra Lineal y sus aplicaciones
Tercera Edición
del autor David C. Lay
"""

# Polinomio de interpolación
# Sugerido: p(t) = a0 + a1t + a2t²+ a3t³ + a4t⁴ + a5t⁵

import numpy as np

datos = [
        (0, 0),
        (2, 2.9),
        (4, 14.8),
        (6, 39.6),
        (8, 74.3),
        (10, 119)
        ]

def ecuacion(point):
    t, c = point
    equation = [t ** i for i in range(6)]
    equation.append(c)
    return equation

def matriz_aumentada(puntos):
    """
    return [
            eq1,
            eq2,
            eq3,
            eq4,
            eq5,
            eq6
            ]
    """
    return [ecuacion(p) for p in puntos]

def matriz_coeficiente(matriz_aumentada):
    """
    c = 5
    return [eq.pop(c) for eq in matriz_aumentada]
    """
    """
    return [fila[:6] for fila in matriz_aumentada]
    """
    return [list(fila[:6]) for fila in matriz_aumentada]

def vector_constantes(matriz_aumentada):
    """
    c = 5
    return [eq[5] for eq in matriz_aumentada]
    """
    return [fila[6] for fila in matriz_aumentada]


def determinante(matriz_coeficiente):
    return np.linalg.det(matriz_coeficiente)

def main(datos):
    A = matriz_aumentada(datos)
    C = vector_constantes(A)

    denominador = determinante(matriz_coeficiente(A))

    numeradores = []

    for i in range(6):
        B = matriz_coeficiente(A)
        for j in range(6):
            B[j][i] = C[j]

        numeradores.append(determinante(B))
        
    for i in range(6):
        numeradores[i] = numeradores[i] / denominador

    print(numeradores)
    

if __name__ == "__main__":
    main(datos)
