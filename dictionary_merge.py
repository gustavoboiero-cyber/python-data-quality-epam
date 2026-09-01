import random
import string

# Paso 1: Generación de datos mock - Creamos lista de diccionarios aleatorios
print("=== Generación de Datos Mock ===")
# Creamos la lista vacia
dict_list = []
# Creamos el diccionario con números aleatorios del 2 al 10
num_dicts = random.randint(2, 10)
print(f"Generando {num_dicts} diccionarios aleatorios...")

# Generamos cada diccionario con claves y valores aleatorios
# Iteramos la secuencia con un ciclo for para el crear los diccionarios segun num_dicts
for i in range(num_dicts):
    # Creamos diccionario individual con número aleatorio de claves
    current_dict = {}
    num_keys = random.randint(2, 5)  # Entre 2 y 5 claves por diccionario

    # Generamos claves aleatorias (letras minúsculas) y valores (0-100)
    for _ in range(num_keys):
        key = random.choice(string.ascii_lowercase)
        value = random.randint(0, 100)
        current_dict[key] = value

    # Agregamos los valores creados a la lista
    dict_list.append(current_dict)
    print(f"Diccionario {i + 1}: {current_dict}")

print(f"\nLista completa de diccionarios generados:")
for i, d in enumerate(dict_list, 1):
    print(f"Dict {i}: {d}")

# Paso 2: Análisis de conflictos - Identificamos claves duplicadas y sus valores máximos
print("\n=== Análisis de Conflictos ===")
key_tracker = {}  # Rastrea: {clave: [(valor, dict_num), ...]}

# Recorremos todos los diccionarios para mapear claves y sus fuentes
for dict_num, dictionary in enumerate(dict_list, 1):
    for key, value in dictionary.items():
        if key not in key_tracker:
            key_tracker[key] = []
        key_tracker[key].append((value, dict_num))

# Mostramos análisis de conflictos
for key, occurrences in key_tracker.items():
    if len(occurrences) > 1:
        print(f"Conflicto en clave '{key}': {occurrences}")
    else:
        print(f"Clave única '{key}': {occurrences[0]}")

# Paso 3: Merge con resolución de conflictos - Aplicamos reglas de negocio
print("\n=== Proceso de Merge ===")
common_dict = {}

# Procesamos cada clave según las reglas establecidas
for key, occurrences in key_tracker.items():
    if len(occurrences) == 1:
        # Clave única: mantener tal como está
        value, dict_num = occurrences[0]
        common_dict[key] = value
        print(f"Clave única '{key}': valor {value} mantenido")
    else:
        # Clave duplicada: encontrar valor máximo y renombrar
        max_value = max(occurrences, key=lambda x: x[0])
        value, dict_num = max_value
        new_key = f"{key}_{dict_num}"
        common_dict[new_key] = value
        print(f"Conflicto resuelto '{key}' → '{new_key}': valor máximo {value} del diccionario {dict_num}")

# Paso 4: Resultados finales - Mostramos input y output claramente
print("\n" + "=" * 50)
print("RESULTADOS FINALES")

print("=" * 50)

print("\n📥 INPUT - Lista de diccionarios originales:")
for i, d in enumerate(dict_list, 1):
    print(f"  Dict {i}: {d}")

print("\n📤 OUTPUT - Diccionario común merged:")
print(f"  {common_dict}")

print(f"\n📊 ESTADÍSTICAS:")
print(f"  - Diccionarios procesados: {len(dict_list)}")
print(f"  - Claves únicas en resultado: {len(common_dict)}")
print(f"  - Conflictos resueltos: {sum(1 for k in common_dict.keys() if '_' in k)}")