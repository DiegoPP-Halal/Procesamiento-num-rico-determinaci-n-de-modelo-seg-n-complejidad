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

class SolutionExp:
    def hasDuplicateExp(self, nums: List[int]) -> Tuple[bool, int]:
        """Algoritmo exponencial O(2^n) con delay fijo de 0.001s"""
        iteraciones = 0
        
        def generate_subsets(arr):
            nonlocal iteraciones
            if len(arr) == 0:
                return [[]]
            
            first = arr[0]
            rest = arr[1:]
            subsets = generate_subsets(rest)
            
            new_subsets = []
            for subset in subsets:
                iteraciones += 1
                time.sleep(0.001)  # Delay fijo igual que los demás algoritmos
                new_subsets.append(subset + [first])
            
            return subsets + new_subsets
        
        all_subsets = generate_subsets(nums)
        
        # Verificación de duplicados (simplificada para el ejemplo)
        seen = set()
        for num in nums:
            if num in seen:
                return True, iteraciones
            seen.add(num)
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
    print("4. Solución O(2^n) (Exponencial)")
    print("5. Salir")
    print("="*50)

def mostrar_menu_secundario(nombre_algoritmo):
    print("\n" + "="*50)
    print(f"Menú para: {nombre_algoritmo}")
    print("="*50)
    print("1. Tomar datos automáticos")
    print("2. Mostrar diagrama de dispersión")
    print("3. Determinar mínimos cuadrados")
    print("4. Gráfico con curva de mínimos cuadrados")
    print("5. Gráfico completo con todas las curvas")  # Nueva opción
    print("6. Volver al menú principal")
    print("="*50)

def generar_lista_ordenada(n):
    return list(range(1, n+1))

def tomar_datos_automaticos(algoritmo, nombre_algoritmo):
    # Ajustamos el rango según la complejidad del algoritmo
    if nombre_algoritmo == 'O(2^n)':
        tamanios = range(2, 12, 2)  # Rango más pequeño para exponencial
    else:
        tamanios = range(6, 20, 2)
    
    for n in tamanios:
        lista = generar_lista_ordenada(n)
        
        inicio = time.time()
        resultado, iteraciones = algoritmo(lista)
        tiempo_ejecucion = time.time() - inicio
        
        # Aseguramos que el tiempo nunca sea cero
        tiempo_ejecucion = max(tiempo_ejecucion, 0.000001)
        
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
        'O(n log n)': {'color': 'blue', 'marker': '^'},
        'O(2^n)': {'color': 'purple', 'marker': 'D'}
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
    plt.xticks(range(2, 20, 2))
    plt.ylim(bottom=0)
    plt.show()

def resolver_exponencial(sum_x, sum_ln_y, sum_x_ln_y, sum_x2, n):
    """
    Resuelve el sistema para el modelo exponencial: y = a*e^(b*x)
    Transformado a: ln(y) = ln(a) + b*x
    """
    A = np.array([[sum_x2, sum_x],
                  [sum_x, n]])
    B = np.array([sum_x_ln_y, sum_ln_y])
    b, ln_a = np.linalg.solve(A, B)
    a = np.exp(ln_a)
    return a, b

def calcular_minimos_cuadrados(algoritmo_nombre):
    datos_algo = [d for d in estadisticas if d['algoritmo'] == algoritmo_nombre]
    
    if not datos_algo:
        print(f"No hay datos para el algoritmo {algoritmo_nombre}")
        return
    
    x = np.array([d['n_elementos'] for d in datos_algo])
    y = np.array([max(d['tiempo'], 0.000001) for d in datos_algo])
    n = len(x)
    
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x*y)
    sum_x2 = sum(x**2)
    sum_ln_y = sum(np.log(y))
    sum_x_ln_y = sum(x*np.log(y))
    sum_ln_x = sum(np.log(x))
    sum_lnx2 = sum(np.log(x)**2)
    sum_lnx_y = sum(np.log(x)*y)
    sum_x3 = sum(x**3)
    sum_x4 = sum(x**4)
    sum_x2y = sum((x**2)*y)
    
    print("\nResultados de mínimos cuadrados:")
    
    if algoritmo_nombre == 'O(n)':
        try:
            a, b = resolver_lineal(sum_x, sum_y, sum_xy, sum_x2, n)
            print(f"Modelo Lineal (y = a*x + b):")
            print(f"a = {a:.6f}, b = {b:.6f}")
        except Exception as e:
            print("Error modelo lineal:", str(e))
    
    elif algoritmo_nombre == 'O(n²)':
        try:
            a, b, c = resolver_cuadratico(sum_x, sum_y, sum_xy, sum_x2, sum_x2y, sum_x3, sum_x4, n)
            print(f"Modelo Cuadrático (y = a*x² + b*x + c):")
            print(f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}")
        except Exception as e:
            print("Error modelo cuadrático:", str(e))
    
    elif algoritmo_nombre == 'O(n log n)':
        try:
            sum_lnx_y = sum(np.log(x)*y)
            a, b = resolver_logaritmico(sum_ln_x, sum_y, sum_lnx_y, sum_lnx2, n)
            print(f"Modelo Logarítmico (y = a*ln(x) + b):")
            print(f"a = {a:.6f}, b = {b:.6f}")
        except Exception as e:
            print("Error modelo logarítmico:", str(e))
    
    elif algoritmo_nombre == 'O(2^n)':
        try:
            a, b = resolver_exponencial(sum_x, sum_ln_y, sum_x_ln_y, sum_x2, n)
            print(f"Modelo Exponencial (y = a*e^(b*x)):")
            print(f"a = {a:.6f}, b = {b:.6f}")
            print(f"Nota: b debería ser cercano a ln(2) ≈ {math.log(2):.4f} para O(2^n)")
        except Exception as e:
            print("Error modelo exponencial:", str(e))

def mostrar_grafico_minimos_cuadrados(algoritmo_nombre):
    datos_algo = [d for d in estadisticas if d['algoritmo'] == algoritmo_nombre]
    
    if not datos_algo:
        print(f"No hay datos para el algoritmo {algoritmo_nombre}")
        return
    
    x = np.array([d['n_elementos'] for d in datos_algo])
    y = np.array([max(d['tiempo'], 0.000001) for d in datos_algo])
    n = len(x)
    
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x*y)
    sum_x2 = sum(x**2)
    sum_ln_y = sum(np.log(y))
    sum_x_ln_y = sum(x*np.log(y))
    sum_ln_x = sum(np.log(x))
    sum_lnx2 = sum(np.log(x)**2)
    sum_lnx_y = sum(np.log(x)*y)
    sum_x3 = sum(x**3)
    sum_x4 = sum(x**4)
    sum_x2y = sum((x**2)*y)
    
    plt.figure(figsize=(12, 7))
    plt.scatter(x, y, color='red', label='Datos reales')
    
    x_vals = np.linspace(min(x), max(x), 100)
    
    if algoritmo_nombre == 'O(n)':
        try:
            a, b = resolver_lineal(sum_x, sum_y, sum_xy, sum_x2, n)
            y_vals = a*x_vals + b
            plt.plot(x_vals, y_vals, 'g-', label=f'Lineal: y={a:.4f}x+{b:.4f}')
        except Exception as e:
            print("Error modelo lineal:", str(e))
    
    elif algoritmo_nombre == 'O(n²)':
        try:
            a, b, c = resolver_cuadratico(sum_x, sum_y, sum_xy, sum_x2, sum_x2y, sum_x3, sum_x4, n)
            y_vals = a*(x_vals**2) + b*x_vals + c
            plt.plot(x_vals, y_vals, 'b-', label=f'Cuadrático: y={a:.4f}x²+{b:.4f}x+{c:.4f}')
        except Exception as e:
            print("Error modelo cuadrático:", str(e))
    
    elif algoritmo_nombre == 'O(n log n)':
        try:
            sum_lnx_y = sum(np.log(x)*y)
            a, b = resolver_logaritmico(sum_ln_x, sum_y, sum_lnx_y, sum_lnx2, n)
            y_vals = a*np.log(x_vals) + b
            y_vals = np.maximum(y_vals, 0)
            plt.plot(x_vals, y_vals, 'm-', label=f'Logarítmico: y={a:.4f}ln(x)+{b:.4f}')
        except Exception as e:
            print("Error modelo logarítmico:", str(e))
    
    elif algoritmo_nombre == 'O(2^n)':
        try:
            a, b = resolver_exponencial(sum_x, sum_ln_y, sum_x_ln_y, sum_x2, n)
            y_vals = a*np.exp(b*x_vals)
            plt.plot(x_vals, y_vals, 'c-', label=f'Exponencial: y={a:.4f}e^({b:.4f}x)')
        except Exception as e:
            print("Error modelo exponencial:", str(e))
    
    plt.title(f'Modelo de mínimos cuadrados para {algoritmo_nombre}')
    plt.xlabel('Número de elementos')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.ylim(bottom=0)
    plt.show()

def mostrar_grafico_completo():
    if not estadisticas:
        print("\nNo hay datos para mostrar. Ejecute primero 'Tomar datos automáticos'.")
        return
    
    plt.figure(figsize=(14, 8))
    
    modelos = {
        'O(n)': {'color': 'green', 'func': resolver_lineal, 'style': '-'},
        'O(n²)': {'color': 'red', 'func': resolver_cuadratico, 'style': '--'},
        'O(n log n)': {'color': 'blue', 'func': resolver_logaritmico, 'style': '-.'},
        'O(2^n)': {'color': 'purple', 'func': resolver_exponencial, 'style': ':'}
    }
    
    # Dibujar puntos de datos
    for nombre, props in modelos.items():
        datos_algo = [d for d in estadisticas if d['algoritmo'] == nombre]
        if datos_algo:
            x = np.array([d['n_elementos'] for d in datos_algo])
            y = np.array([d['tiempo'] for d in datos_algo])
            plt.scatter(x, y, color=props['color'], label=f'{nombre} (datos)', alpha=0.7)
    
    # Dibujar curvas de ajuste
    x_vals = np.linspace(2, 20, 100)
    
    for nombre, props in modelos.items():
        datos_algo = [d for d in estadisticas if d['algoritmo'] == nombre]
        if datos_algo:
            x = np.array([d['n_elementos'] for d in datos_algo])
            y = np.array([d['tiempo'] for d in datos_algo])
            n = len(x)
            
            try:
                if nombre == 'O(n)':
                    sum_x = sum(x); sum_y = sum(y); sum_xy = sum(x*y); sum_x2 = sum(x**2)
                    a, b = props['func'](sum_x, sum_y, sum_xy, sum_x2, n)
                    y_vals = a*x_vals + b
                    plt.plot(x_vals, y_vals, props['style'], color=props['color'], label=f'{nombre} (ajuste)')
                
                elif nombre == 'O(n²)':
                    sum_x = sum(x); sum_y = sum(y); sum_xy = sum(x*y); sum_x2 = sum(x**2)
                    sum_x3 = sum(x**3); sum_x4 = sum(x**4); sum_x2y = sum((x**2)*y)
                    a, b, c = props['func'](sum_x, sum_y, sum_xy, sum_x2, sum_x2y, sum_x3, sum_x4, n)
                    y_vals = a*(x_vals**2) + b*x_vals + c
                    plt.plot(x_vals, y_vals, props['style'], color=props['color'], label=f'{nombre} (ajuste)')
                
                elif nombre == 'O(n log n)':
                    sum_ln_x = sum(np.log(x)); sum_y = sum(y); sum_lnx_y = sum(np.log(x)*y); sum_lnx2 = sum(np.log(x)**2)
                    a, b = props['func'](sum_ln_x, sum_y, sum_lnx_y, sum_lnx2, n)
                    y_vals = a*np.log(x_vals) + b
                    plt.plot(x_vals, y_vals, props['style'], color=props['color'], label=f'{nombre} (ajuste)')
                
                elif nombre == 'O(2^n)':
                    sum_x = sum(x); sum_ln_y = sum(np.log(y)); sum_x_ln_y = sum(x*np.log(y)); sum_x2 = sum(x**2)
                    a, b = props['func'](sum_x, sum_ln_y, sum_x_ln_y, sum_x2, n)
                    y_vals = a*np.exp(b*x_vals)
                    plt.plot(x_vals, y_vals, props['style'], color=props['color'], label=f'{nombre} (ajuste)')
            
            except Exception as e:
                print(f"Error al calcular modelo para {nombre}: {str(e)}")
    
    plt.title('Comparación Completa de Algoritmos con Curvas de Ajuste')
    plt.xlabel('Número de elementos')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.ylim(bottom=0)
    plt.show()

# Funciones de resolución (se mantienen igual)
def resolver_lineal(sum_x, sum_y, sum_xy, sum_x2, n):
    A = np.array([[sum_x2, sum_x],
                  [sum_x, n]])
    B = np.array([sum_xy, sum_y])
    return np.linalg.solve(A, B)

def resolver_logaritmico(sum_ln_x, sum_y, sum_lnx_y, sum_lnx2, n):
    A = np.array([[sum_lnx2, sum_ln_x],
                  [sum_ln_x, n]])
    B = np.array([sum_lnx_y, sum_y])
    return np.linalg.solve(A, B)

def resolver_cuadratico(sum_x, sum_y, sum_xy, sum_x2, sum_x2y, sum_x3, sum_x4, n):
    A = np.array([[sum_x4, sum_x3, sum_x2],
                  [sum_x3, sum_x2, sum_x],
                  [sum_x2, sum_x, n]])
    B = np.array([sum_x2y, sum_xy, sum_y])
    return np.linalg.solve(A, B)

def main():
    sol_n = SolutionN()
    sol_n2 = SolutionN2()
    sol_nlogn = SolutionNLogN()
    sol_exp = SolutionExp()
    
    algoritmos = {
        '1': {'obj': sol_n, 'nombre': 'O(n)', 'metodo': sol_n.hasDuplicateN},
        '2': {'obj': sol_n2, 'nombre': 'O(n²)', 'metodo': sol_n2.hasDuplicateN2},
        '3': {'obj': sol_nlogn, 'nombre': 'O(n log n)', 'metodo': sol_nlogn.hasDuplicateNLogN},
        '4': {'obj': sol_exp, 'nombre': 'O(2^n)', 'metodo': sol_exp.hasDuplicateExp}
    }
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
            
        elif opcion in algoritmos:
            algoritmo_actual = algoritmos[opcion]
            
            while True:
                mostrar_menu_secundario(algoritmo_actual['nombre'])
                sub_op = input("Seleccione opción (1-6): ")
                
                if sub_op == "1":
                    print(f"\nTomando datos automáticos para {algoritmo_actual['nombre']}...")
                    tomar_datos_automaticos(
                        algoritmo_actual['metodo'],
                        algoritmo_actual['nombre']
                    )
                    
                elif sub_op == "2":
                    mostrar_diagrama_dispersion()
                    
                elif sub_op == "3":
                    calcular_minimos_cuadrados(algoritmo_actual['nombre'])
                    
                elif sub_op == "4":
                    mostrar_grafico_minimos_cuadrados(algoritmo_actual['nombre'])
                    
                elif sub_op == "5":
                    mostrar_grafico_completo()
                    
                elif sub_op == "6":
                    break
                    
                else:
                    print("Opción no válida")
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
