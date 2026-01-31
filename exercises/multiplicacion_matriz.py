def are_multiplyable(matA, matB):
    # matA es u x m, matB es m x v, es matA x matB es posible
    rowsA, columnsA = len(matA), len(matA[0])
    rowsB, columnsB = len(matB), len(matB[0])

    if columnsA == rowsB:
        # Revisar primero integridad de las matrices
        for row_matA in matA:
            if columnsA != len(row_matA):
                return False
        for row_matB in matB:
            if columnsB != len(row_matB):
                return False
        return True
    else:
        return False

def create_new_matrix(num_rows, num_columns):
    # Se crea la matriz con el tamaño u x v
    matrix: list = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    return matrix

def matrix_multiplication(matA, matB, matAB):
    size_row_matA = len(matA)
    size_row_matB = len(matB)
    size_column_matA = len(matA[0])
    size_column_matB = len(matB[0])

    # Dado que matA es row i x  column k, matB es row k x column j
    for i in range(size_row_matA): # Accedo a las filas de matA
        for j in range(size_column_matB): # Accedo a las columnas de matB
            for k in range(size_row_matB):
                # Accedo al elemento en fila k en columna j de matB
                # Accedo al elemento en fila i en columna k de matA

                matAB[i][j] += matA[i][k] * matB[k][j]

    return matAB

def main():
    A = [(1, 2, 3, 4),
    (5, 6, 7, 8),
    (2, 2, 5, 0),
    (4, 0, 0, 5),
    (5, 3, 4, 0)]

    B = [(0, 0, 1, 3, 1),
     (0, 0, 3, 1, 3),
     (2, 7, 9, 0, 7),
     (3, 3, 8, 7, 9)]    

    if are_multiplyable(A, B):
        matrix = matrix_multiplication(A, B, create_new_matrix(len(A), len(B[0])))

        for i in matrix:
            print(tuple(i))
    else:
        return -1;

if __name__ == '__main__':
    main()
