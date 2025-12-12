# Hamiltoniano 1D por diferencias finitas
# Formato típico de cálculo de Mecánica Cuántica Numérica

import numpy as np
from scipy.linalg import eigh   # importar correctamente

N = 400
L = 10.0
dx = L / (N - 1)
x = np.linspace(-L/2, L/2, N)

# Operador cinético T = -(1/2) d^2/dx^2
main_diag = -2.0 * np.ones(N)
off_diag = 1.0 * np.ones(N-1)
Laplacian = (np.diag(main_diag) + np.diag(off_diag, 1) + np.diag(off_diag, -1)) / dx**2
T = -0.5 * Laplacian

# Operador potencial V(x) = 0.5 * k * x^2
k = 1.0
Vx = 0.5 * k * x**2
V = np.diag(Vx)

# Hamiltoniano total H = T + V
H = T + V

# Diagonalización
E, psi = eigh(H)

# Niveles de energía
print("Primeros 6 niveles:", E[:6])