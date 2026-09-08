import re

# 📦 Los Datos Crudos (Mantenemos exactamente el texto original)
raw_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


def count_whitespaces(text: str) -> int:
    """
    Calcula el número exacto de caracteres de espacio en blanco (Paso 4).
    Detecta espacios simples, tabulaciones y saltos de línea.
    """
    return sum(1 for char in text if char.isspace())


def _capitalize_sentence(s: str) -> str:
    """
    Función auxiliar (helper) para capitalizar una oración individual.
    Pone la primera letra en mayúscula, el resto en minúscula,
    pero mantiene el pronombre 'I' en mayúscula de forma robusta.
    """
    words_and_spaces = re.split(r'(\b\w+\b)', s)
    first_word_found = False

    for j in range(len(words_and_spaces)):
        token = words_and_spaces[j]
        if token.isalnum():
            if not first_word_found:
                words_and_spaces[j] = token.capitalize()
                first_word_found = True
            else:
                # Regla de DQ: Preservamos el pronombre 'I' en mayúscula
                if token.lower() == 'i':
                    words_and_spaces[j] = 'I'
                else:
                    words_and_spaces[j] = token.lower()

    return "".join(words_and_spaces)


def normalize_text(text: str) -> str:
    """
    Normaliza el uso de mayúsculas y minúsculas en el texto (Paso 1).
    Divide por puntos y saltos de línea para identificar correctamente
    los límites de las oraciones sin alterar la estructura original.
    """
    # Dividimos por puntos (.) o saltos de línea (\n), guardando los delimitadores
    tokens = re.split(r'(\.|\n)', text)
    normalized_tokens = []

    for token in tokens:
        if token in ('.', '\n'):
            normalized_tokens.append(token)
        else:
            if any(char.isalpha() for char in token):
                normalized_tokens.append(_capitalize_sentence(token))
            else:
                normalized_tokens.append(token)

    return "".join(normalized_tokens)


def fix_typos(text: str) -> str:
    """
    Corrige los errores de 'iz' -> 'is' utilizando expresiones regulares (Paso 2).
    Evita falsos positivos como modificar texto explicativo entre comillas.
    """
    return re.sub(r'(?<![“\"\w])iz(?![”\"\w])', 'is', text, flags=re.IGNORECASE)


def extract_last_words_and_append(text: str) -> str:
    """
    Extrae la última palabra de cada oración válida (ignorando encabezados) (Paso 3).
    Construye una nueva oración y la añade al final del párrafo.
    """
    # Dividimos por puntos (.) y saltos de línea (\n)
    tokens = re.split(r'(\.|\n)', text)
    last_words = []

    for token in tokens:
        if token in ('.', '\n'):
            continue

        stripped = token.strip()
        if not stripped:
            continue

        # Regla de DQ: Si termina en dos puntos ':', es un título/encabezado, no una oración.
        if stripped.endswith(':'):
            continue

        # Extraemos todas las palabras alfanuméricas de este segmento
        words = re.findall(r'\b\w+\b', token)
        if words:
            # Nos quedamos con la última palabra del segmento
            last_words.append(words[-1])

    # Creamos la nueva oración
    new_sentence = " ".join(last_words).capitalize() + "."

    # Buscamos si hay espacios o saltos de línea al final del texto original
    match = re.search(r'(\s*)$', text)
    trailing_whitespace = match.group(1) if match else ""

    # Limpiamos el texto al final, agregamos la oración y devolvemos la estructura
    cleaned_text = text.rstrip()
    return cleaned_text + " " + new_sentence + trailing_whitespace


# ==========================================
# 🖥️ BLOQUE DE EJECUCIÓN PRINCIPAL (PIPELINE)
# ==========================================
if __name__ == "__main__":
    print("--- EJECUCIÓN DEL SCRIPT DE DATA QUALITY (REFRACTORIZADO) ---\n")

    # 📊 Paso 4: Data Profiling (Whitespace Counter)
    # Se ejecuta primero sobre el texto crudo para no alterar la métrica original.
    total_spaces = count_whitespaces(raw_text)
    print(f"Paso 4 -> Total de caracteres de espacio en blanco: {total_spaces}")
    # Validación: Dará exactamente 87.

    # 🔠 Paso 1: Normalization (Letter Cases)
    step_1 = normalize_text(raw_text)

    # 🛠️ Paso 2: Fixing Typos
    step_2 = fix_typos(step_1)

    # 🔍 Paso 3: Extracting Data and Appending
    final_text = extract_last_words_and_append(step_2)

    print("\nTexto Limpio y Normalizado:")
    print(final_text)