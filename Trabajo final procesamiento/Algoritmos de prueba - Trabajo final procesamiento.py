from typing import List
import time
import random

class Solution1:
    def hasDuplicateN2(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            time.sleep(0.5)  # Delay por iteración exterior
            for j in range(i + 1, len(nums)):
                time.sleep(0.5)  # Delay por iteración interior
                if nums[i] == nums[j]:
                    return True
        return False

class Solution2:
    def hasDuplicateLogN(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            time.sleep(0.5)  # Delay por comparación
            if nums[i] == nums[i - 1]:
                return True
        return False

class Solution3:
    def hasDuplicateN(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            time.sleep(0.5)  # Delay por elemento
            if num in seen:
                return True
            seen.add(num)
        return False

def generar_lista(longitud, con_duplicados=True):
    if con_duplicados:
        unicos = random.sample(range(1, 1000), int(longitud * 0.8))
        duplicados = random.choices(unicos, k=longitud - len(unicos))
        lista = unicos + duplicados
        random.shuffle(lista)
        return lista
    else:
        return random.sample(range(1, 1000), longitud)

def mostrar_menu():
    print("\n" + "="*50)
    print("MENÚ DE ALGORITMOS DE DETECCIÓN DE DUPLICADOS")
    print("="*50)
    print("1. Algoritmo O(n²) - Comparación por pares")
    print("2. Algoritmo O(n log n) - Ordenar y comparar adyacentes")
    print("3. Algoritmo O(n) - Usando conjunto (HashSet)")
    print("4. Probar todos los algoritmos")
    print("5. Configurar lista de prueba")
    print("6. Salir")
    print("="*50)

def probar_algoritmo(algoritmo, nums, nombre):
    print(f"\nProbando {nombre}...")
    print(f"Elementos: {len(nums)}")
    inicio = time.time()
    resultado = algoritmo(nums)
    tiempo_total = time.time() - inicio
    print(f"¿Duplicados? {'Sí' if resultado else 'No'}")
    print(f"Tiempo total (con delays): {tiempo_total:.2f}s")

def main():
    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()
    
    lista_prueba = generar_lista(5)  # Lista pequeña para pruebas
    print("NOTA: Lista reducida a 5 elementos por tiempos de ejecución")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "6":
            print("¡Hasta luego!")
            break
        elif opcion == "5":
            print("\nConfiguración de lista:")
            print("1. 5 elementos (rápido)")
            print("2. 10 elementos (lento)")
            sub_op = input("Seleccione: ")
            lista_prueba = generar_lista(5 if sub_op == "1" else 10)
            continue
            
        if opcion in ["1", "2", "3", "4"]:
            print("\nADVERTENCIA: Cada iteración tiene 0.5s de delay")
            print(f"Lista: {lista_prueba}")
            
        if opcion == "1":
            probar_algoritmo(sol1.hasDuplicateN2, lista_prueba, "algoritmo O(n²)")
        elif opcion == "2":
            probar_algoritmo(sol2.hasDuplicateLogN, lista_prueba, "algoritmo O(n log n)")
        elif opcion == "3":
            probar_algoritmo(sol3.hasDuplicateN, lista_prueba, "algoritmo O(n)")
        elif opcion == "4":
            print("\n=== Probando todos ===")
            probar_algoritmo(sol1.hasDuplicateN2, lista_prueba, "O(n²)")
            probar_algoritmo(sol2.hasDuplicateLogN, lista_prueba, "O(n log n)")
            probar_algoritmo(sol3.hasDuplicateN, lista_prueba, "O(n)")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()