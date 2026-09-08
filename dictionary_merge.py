import random
import string
from typing import List, Dict


def generate_mock_data() -> List[Dict[str, int]]:
    """
    Genera una lista aleatoria de diccionarios con claves y valores aleatorios.
    (Encapsula el original Paso 1).
    """
    print("=== Generación de Datos Mock ===")
    dict_list = []
    num_dicts = random.randint(2, 10)
    print(f"Generando {num_dicts} diccionarios aleatorios...")

    # Generamos cada diccionario con claves y valores aleatorios
    for i in range(num_dicts):
        current_dict = {}
        num_keys = random.randint(2, 5)  # Entre 2 y 5 claves por diccionario

        for _ in range(num_keys):
            key = random.choice(string.ascii_lowercase)
            value = random.randint(0, 100)
            current_dict[key] = value

        dict_list.append(current_dict)
        print(f"Diccionario {i + 1}: {current_dict}")

    print(f"\nLista completa de diccionarios generados:")
    for i, d in enumerate(dict_list, 1):
        print(f"Dict {i}: {d}")

    return dict_list


def merge_dictionaries(dict_list: List[Dict[str, int]]) -> Dict[str, int]:
    """
    Combina una lista de diccionarios resolviendo conflictos por valor máximo
    y renombrando las claves duplicadas.
    (Encapsula el original Paso 2 y Paso 3).
    """
    # --- Paso 2: Análisis de conflictos ---
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

    # --- Paso 3: Merge con resolución de conflictos ---
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

    return common_dict


# ==========================================
# 🖥️ BLOQUE DE EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # 1. Generamos los datos y los guardamos en una variable
    input_data = generate_mock_data()

    # 2. Pasamos esos datos a la función de merge y obtenemos el resultado
    output_merged = merge_dictionaries(input_data)

    # 3. Paso 4: Resultados finales y Estadísticas
    print("\n" + "=" * 50)
    print("RESULTADOS FINALES")
    print("=" * 50)

    print("\n📥 INPUT - Lista de diccionarios originales:")
    for i, d in enumerate(input_data, 1):
        print(f"  Dict {i}: {d}")

    print("\n📤 OUTPUT - Diccionario común merged:")
    print(f"  {output_merged}")

    print(f"\n📊 ESTADÍSTICAS:")
    print(f"  - Diccionarios procesados: {len(input_data)}")
    print(f"  - Claves únicas en resultado: {len(output_merged)}")
    print(f"  - Conflictos resueltos: {sum(1 for k in output_merged.keys() if '_' in k)}")