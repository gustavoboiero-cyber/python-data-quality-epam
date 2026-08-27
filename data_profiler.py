import random

# Generación de datos simulados - Creamos 100 números aleatorios para simular un dataset real
print("Generando datos simulados...")
data_list = [random.randint(0, 1000) for _ in range(100)]
print(f"Se generaron {len(data_list)} números aleatorios")

# Ordenamos los datos para facilitar el análisis de min/max y mejorar la visualización
data_list.sort()
print("Datos ordenados exitosamente")

# Métricas básicas - Usamos funciones integradas para cálculos confiables y optimizados
min_value = min(data_list)
max_value = max(data_list)

# Filtramos números pares e impares por separado para calcular promedios independientes según requerimiento
even_numbers = [num for num in data_list if num % 2 == 0]
odd_numbers = [num for num in data_list if num % 2 != 0]

# Implementamos programación defensiva para prevenir errores en casos extremos
# Esto asegura que el script no falle si el dataset contiene solo números pares o solo impares
if even_numbers:
    avg_even = sum(even_numbers) / len(even_numbers)
else:
    avg_even = 0

if odd_numbers:
    avg_odd = sum(odd_numbers) / len(odd_numbers)
else:
    avg_odd = 0

# Generamos salida estructurada para cumplir con estándares de reportes de Calidad de Datos
print("\n--- Reporte de Perfilado de Datos ---")
print(f"Total de registros: {len(data_list)}")
print(f"Valor mínimo: {min_value}")
print(f"Valor máximo: {max_value}")
print(f"Promedio de números PARES: {avg_even:.1f}")
print(f"Promedio de números IMPARES: {avg_odd:.1f}")
print("-------------------------------------")

# BONUS CHALLENGE - Implementamos min/max manual para demostrar pensamiento algorítmico
print("\n--- Desafío Bonus: Cálculo Manual ---")
manual_min = data_list[0]
manual_max = data_list[0]

# Usamos enfoque iterativo para entender la lógica subyacente de las funciones min/max
for number in data_list:
    if number < manual_min:
        manual_min = number
    if number > manual_max:
        manual_max = number

print(f"Mínimo calculado manualmente: {manual_min}")
print(f"Máximo calculado manualmente: {manual_max}")
# Validamos que ambos enfoques produzcan resultados idénticos para aseguramiento de calidad
print(f"Verificación: ¿Coinciden con funciones integradas? Min: {min_value == manual_min}, Max: {max_value == manual_max}")
print("--------------------------------------------")