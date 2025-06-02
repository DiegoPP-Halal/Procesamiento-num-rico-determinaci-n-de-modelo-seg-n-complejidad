from typing import List, Dict, Tuple
import time
import matplotlib.pyplot as plt

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
    print("3. Volver al menú principal")
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
                sub_op = input("Seleccione opción (1-3): ")
                
                if sub_op == "1":
                    print(f"\nTomando datos automáticos para {algoritmo_actual['nombre']}...")
                    tomar_datos_automaticos(
                        algoritmo_actual['metodo'],
                        algoritmo_actual['nombre']
                    )
                    
                elif sub_op == "2":
                    mostrar_diagrama_dispersion()
                    
                elif sub_op == "3":
                    break
                    
                else:
                    print("Opción no válida")
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    # Instalar dependencias si no están disponibles
    try:
        import matplotlib
    except ImportError:
        print("Instalando dependencias necesarias...")
        import subprocess
        subprocess.run(['pip', 'install', 'matplotlib'], check=True)
    
    main()
