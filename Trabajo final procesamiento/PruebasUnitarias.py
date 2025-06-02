# Ejemplo de uso para cada modelo
if __name__ == "__main__":
    # Datos de ejemplo (reemplazar con tus sumatorias)
    n = 10
    sum_x = 55.0
    sum_y = 81.0
    sum_xy = 572.4
    sum_x2 = 385.0
    sum_ln_y = 20.0
    sum_x_ln_y = 110.0
    sum_ln_x = 15.0
    sum_lnx_lny = 30.0
    sum_lnx2 = 25.0
    sum_lnx_y = 40.0
    sum_x2y = 3025.0
    sum_x3 = 3025.0
    sum_x4 = 25333.0

    # Resolver para cada modelo
    a_lin, b_lin = resolver_lineal(sum_x, sum_y, sum_xy, sum_x2, n)
    print(f"Modelo Lineal: y = {a_lin:.4f}x + {b_lin:.4f}")

    n = 6
    sum_x = 8.3
    sum_ln_y = 44.50348
    sum_x_ln_y = 63.75864
    sum_x2 = 14.09

    a_exp, b_exp = resolver_exponencial(sum_x, sum_ln_y, sum_x_ln_y, sum_x2, n)
    print(f"Modelo Exponencial: y = {a_exp:.4f}e^({b_exp:.4f}x)")


    a_pot, b_pot = resolver_potencial(sum_ln_x, sum_ln_y, sum_lnx_lny, sum_lnx2, n)
    print(f"Modelo Potencial: y = {a_pot:.4f}x^{b_pot:.4f}")

    a_log, b_log = resolver_logaritmico(sum_ln_x, sum_y, sum_lnx_y, sum_lnx2, n)
    print(f"Modelo Logarítmico: y = {a_log:.4f}ln(x) + {b_log:.4f}")

    sum_x = 1.8
    sum_y = 6.63
    sum_x2 = 0.51
    sum_x3 = 0.162
    sum_x4 = 0.054825
    sum_xy = 1.69825
    sum_x2y = 0.511813
    n = 8

    a_cuad, b_cuad, c_cuad = resolver_cuadratico(sum_x, sum_y, sum_xy, sum_x2, sum_x2y, sum_x3, sum_x4, n)
    print(f"Modelo Cuadrático: y = {a_cuad:.4f}x^2 + {b_cuad:.4f}x + {c_cuad:.4f}")