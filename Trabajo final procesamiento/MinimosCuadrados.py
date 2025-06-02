import numpy as np

def resolver_lineal(sum_x, sum_y, sum_xy, sum_x2, n):
    """
    Resuelve el sistema para el modelo lineal: y = a*x + b
    """
    A = np.array([[sum_x2, sum_x],
                  [sum_x, n]])
    B = np.array([sum_xy, sum_y])
    a, b = np.linalg.solve(A, B)
    return a, b

def resolver_exponencial(sum_x, sum_ln_y, sum_x_ln_y, sum_x2, n):
    """
    Resuelve el sistema para el modelo exponencial: y = a*e^(b*x) (transformado a ln(y) = ln(a) + b*x)
    """
    A = np.array([[sum_x2, sum_x],
                  [sum_x, n]])
    B = np.array([sum_x_ln_y, sum_ln_y])
    b, ln_a = np.linalg.solve(A, B)
    a = np.exp(ln_a)
    return a, b

def resolver_potencial(sum_ln_x, sum_ln_y, sum_lnx_lny, sum_lnx2, n):
    """
    Resuelve el sistema para el modelo potencial: y = a*x^b (transformado a ln(y) = ln(a) + b*ln(x))
    """
    A = np.array([[sum_lnx2, sum_ln_x],
                  [sum_ln_x, n]])
    B = np.array([sum_lnx_lny, sum_ln_y])
    b, ln_a = np.linalg.solve(A, B)
    a = np.exp(ln_a)
    return a, b

def resolver_logaritmico(sum_ln_x, sum_y, sum_lnx_y, sum_lnx2, n):
    """
    Resuelve el sistema para el modelo logarítmico: y = a*ln(x) + b
    """
    A = np.array([[sum_lnx2, sum_ln_x],
                  [sum_ln_x, n]])
    B = np.array([sum_lnx_y, sum_y])
    a, b = np.linalg.solve(A, B)
    return a, b

def resolver_cuadratico(sum_x, sum_y, sum_xy, sum_x2, sum_x2y, sum_x3, sum_x4, n):
    """
    Resuelve el sistema para el modelo cuadrático: y = a*x^2 + b*x + c
    """
    A = np.array([[sum_x4, sum_x3, sum_x2],
                  [sum_x3, sum_x2, sum_x],
                  [sum_x2, sum_x, n]])
    B = np.array([sum_x2y, sum_xy, sum_y])
    a, b, c = np.linalg.solve(A, B)
    return a, b, c
