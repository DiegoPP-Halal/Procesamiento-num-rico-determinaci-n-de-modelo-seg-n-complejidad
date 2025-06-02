from typing import List, Dict, Tuple
import time
import matplotlib.pyplot as plt
import numpy as np
import math

# Estructura para guardar estadísticas
estadisticas: List[Dict] = []

class SolutionN:
    def hasDuplicateN(self, nums: List[int]) -> Tuple[bool, int]:
        seen = set()
        iteraciones = 0
        for num in nums:
            iteraciones += 1
            time.sleep(0.001)
            if num in seen:
                return True, iteraciones
            seen.add(num)
        return False, iteraciones

class SolutionN2:
    def hasDuplicateN2(self, nums: List[int]) -> Tuple[bool, int]:
        iteraciones = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                iteraciones += 1
                time.sleep(0.001)
                if nums[i] == nums[j]:
                    return True, iteraciones
        return False, iteraciones

class SolutionNLogN:
    def hasDuplicateNLogN(self, nums: List[int]) -> Tuple[bool, int]:
        nums.sort()
        iteraciones = 0
        for i in range(1, len(nums)):
            iteraciones += 1
            time.sleep(0.001)
            if nums[i] == nums[i - 1]:
                return True, iteraciones
        return False, iteraciones

def mostrar_menu_principal():
    print("\n" + "="*50)
    print("Estimación de tiempo de ejecución de algoritmos")
    print("="*50)
    print("Probando algoritmo de encontrar duplicados")
    print("-"*50)
    print("1. Solución O(n)")
    print("2. Solución O(n²)")
    print("3. Solución O(n log n)")
    print("4. Salir")
    print("="*50)

def mostrar_menu_secundario(nombre_algoritmo):
    print("\n" + "="*50)
    print(f"Menú para: {nombre_algoritmo}")
    print("="*50)
    print("1. Tomar datos automáticos")
    print("2. Mostrar diagrama de dispersión")
    print("3. Determinar mínimos cuadrados")
    print("4. Gráfico con curva de mínimos cuadrados")
    print("5. Volver al menú principal")
    
    print("="*50)

def generar_lista_ordenada(n):
    return list(range(1, n+1))

def tomar_datos_automaticos(algoritmo, nombre_algoritmo):
    tamanios = range(6, 20, 2)
    
    for n in tamanios:
        lista = generar_lista_ordenada(n)
        
        inicio = time.time()
        resultado, iteraciones = algoritmo(lista)
        tiempo_ejecucion = time.time() - inicio
        
        estadisticas.append({
            'algoritmo': nombre_algoritmo,
            'n_elementos': n,
            'iteraciones': iteraciones,
            'tiempo': tiempo_ejecucion,
            'fecha': time.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        print(f"Prueba con {n} elementos: {iteraciones} iteraciones, {tiempo_ejecucion:.6f} segundos")

def mostrar_diagrama_dispersion():
    if not estadisticas:
        print("\nNo hay datos para mostrar. Ejecute primero 'Tomar datos automáticos'.")
        return
    
    plt.figure(figsize=(12, 7))
    
    estilos = {
        'O(n)': {'color': 'green', 'marker': 'o'},
        'O(n²)': {'color': 'red', 'marker': 's'},
        'O(n log n)': {'color': 'blue', 'marker': '^'}
    }
    
    for nombre, estilo in estilos.items():
        datos_algo = [d for d in estadisticas if d['algoritmo'] == nombre]
        if datos_algo:
            x = [d['n_elementos'] for d in datos_algo]
            y = [d['tiempo'] for d in datos_algo]
            plt.plot(x, y, label=nombre, 
                    linestyle='--', marker=estilo['marker'],
                    color=estilo['color'], alpha=0.7)
    
    plt.title('Tiempo de ejecución vs Tamaño de lista')
    plt.xlabel('Número de elementos en la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(6, 20, 2))
    plt.show()

def calcular_minimos_cuadrados(algoritmo_nombre):
    # Filtrar datos para el algoritmo seleccionado
    datos_algo = [d for d in estadisticas if d['algoritmo'] == algoritmo_nombre]
    
    if not datos_algo:
        print(f"No hay datos para el algoritmo {algoritmo_nombre}")
        return
    
    # Preparar datos
    x = np.array([d['n_elementos'] for d in datos_algo])
    y = np.array([d['tiempo'] for d in datos_algo])
    n = len(x)
    
    # Calcular sumatorias necesarias
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x*y)
    sum_x2 = sum(x**2)
    sum_ln_x = sum(np.log(x))
    sum_ln_y = sum(np.log(y))
    sum_lnx_lny = sum(np.log(x)*np.log(y))
    sum_lnx2 = sum(np.log(x)**2)
    
    print("\nResultados de mínimos cuadrados:")
    
    # Aplicar el modelo correspondiente según el algoritmo
    if algoritmo_nombre == 'O(n)':
        # Modelo lineal para O(n)
        try:
            a, b = resolver_lineal(sum_x, sum_y, sum_xy, sum_x2, n)
            print(f"Modelo Lineal (y = a*x + b):")
            print(f"a = {a:.6f}, b = {b:.6f}")
        except Exception as e:
            print("No se pudo calcular el modelo lineal:", str(e))
    
    elif algoritmo_nombre == 'O(n²)':
        # Modelo cuadrático para O(n²)
        try:
            sum_x3 = sum(x**3)
            sum_x4 = sum(x**4)
            sum_x2y = sum((x**2)*y)
            a, b, c = resolver_cuadratico(sum_x, sum_y, sum_xy, sum_x2, sum_x2y, sum_x3, sum_x4, n)
            print(f"Modelo Cuadrático (y = a*x² + b*x + c):")
            print(f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}")
        except Exception as e:
            print("No se pudo calcular el modelo cuadrático:", str(e))
    
    elif algoritmo_nombre == 'O(n log n)':
        # Modelo logarítmico para O(n log n)
        try:
            a, b = resolver_logaritmico(sum_ln_x, sum_y, sum_xy, sum_lnx2, n)
            print(f"Modelo Logarítmico (y = a*ln(x) + b):")
            print(f"a = {a:.6f}, b = {b:.6f}")
        except Exception as e:
            print("No se pudo calcular el modelo logarítmico:", str(e))

def mostrar_grafico_minimos_cuadrados(algoritmo_nombre):
    # Filtrar datos para el algoritmo seleccionado
    datos_algo = [d for d in estadisticas if d['algoritmo'] == algoritmo_nombre]
    
    if not datos_algo:
        print(f"No hay datos para el algoritmo {algoritmo_nombre}")
        return
    
    # Preparar datos
    x = np.array([d['n_elementos'] for d in datos_algo])
    y = np.array([d['tiempo'] for d in datos_algo])
    n = len(x)
    
    # Calcular sumatorias necesarias
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x*y)
    sum_x2 = sum(x**2)
    sum_ln_x = sum(np.log(x))
    sum_lnx2 = sum(np.log(x)**2)
    
    plt.figure(figsize=(12, 7))
    plt.scatter(x, y, color='red', label='Datos reales')
    
    # Generar puntos para la curva
    x_vals = np.linspace(min(x), max(x), 100)
    
    # Aplicar el modelo correspondiente según el algoritmo
    if algoritmo_nombre == 'O(n)':
        # Modelo lineal para O(n)
        try:
            a, b = resolver_lineal(sum_x, sum_y, sum_xy, sum_x2, n)
            y_vals = a*x_vals + b
            plt.plot(x_vals, y_vals, 'g-', label=f'Lineal: y={a:.4f}x+{b:.4f}')
        except:
            print("No se pudo calcular el modelo lineal")
    
    elif algoritmo_nombre == 'O(n²)':
        # Modelo cuadrático para O(n²)
        try:
            sum_x3 = sum(x**3)
            sum_x4 = sum(x**4)
            sum_x2y = sum((x**2)*y)
            a, b, c = resolver_cuadratico(sum_x, sum_y, sum_xy, sum_x2, sum_x2y, sum_x3, sum_x4, n)
            y_vals = a*(x_vals**2) + b*x_vals + c
            plt.plot(x_vals, y_vals, 'b-', label=f'Cuadrático: y={a:.4f}x²+{b:.4f}x+{c:.4f}')
        except:
            print("No se pudo calcular el modelo cuadrático")
    
    elif algoritmo_nombre == 'O(n log n)':
        # Modelo logarítmico para O(n log n)
        try:
            a, b = resolver_logaritmico(sum_ln_x, sum_y, sum_xy, sum_lnx2, n)
            y_vals = a*np.log(x_vals) + b
            plt.plot(x_vals, y_vals, 'm-', label=f'Logarítmico: y={a:.4f}ln(x)+{b:.4f}')
        except:
            print("No se pudo calcular el modelo logarítmico")
    
    plt.title(f'Modelo de mínimos cuadrados para {algoritmo_nombre}')
    plt.xlabel('Número de elementos')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.show()

def resolver_lineal(sum_x, sum_y, sum_xy, sum_x2, n):
    """
    Resuelve el sistema para el modelo lineal: y = a*x + b
    """
    A = np.array([[sum_x2, sum_x],
                  [sum_x, n]])
    B = np.array([sum_xy, sum_y])
    a, b = np.linalg.solve(A, B)
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

def main():
    sol_n = SolutionN()
    sol_n2 = SolutionN2()
    sol_nlogn = SolutionNLogN()
    
    algoritmos = {
        '1': {'obj': sol_n, 'nombre': 'O(n)', 'metodo': sol_n.hasDuplicateN},
        '2': {'obj': sol_n2, 'nombre': 'O(n²)', 'metodo': sol_n2.hasDuplicateN2},
        '3': {'obj': sol_nlogn, 'nombre': 'O(n log n)', 'metodo': sol_nlogn.hasDuplicateNLogN}
    }
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "4":
            print("¡Hasta luego!")
            break
            
        elif opcion in algoritmos:
            algoritmo_actual = algoritmos[opcion]
            
            while True:
                mostrar_menu_secundario(algoritmo_actual['nombre'])
                sub_op = input("Seleccione opción (1-5): ")
                
                if sub_op == "1":
                    print(f"\nTomando datos automáticos para {algoritmo_actual['nombre']}...")
                    tomar_datos_automaticos(
                        algoritmo_actual['metodo'],
                        algoritmo_actual['nombre']
                    )
                    
                elif sub_op == "2":
                    mostrar_diagrama_dispersion()
                    
                elif sub_op == "5":
                    break
                    
                elif sub_op == "3":
                    calcular_minimos_cuadrados(algoritmo_actual['nombre'])
                    
                elif sub_op == "4":
                    mostrar_grafico_minimos_cuadrados(algoritmo_actual['nombre'])
                    
                else:
                    print("Opción no válida")
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
