import re

# Los Datos Crudos (Mantenemos exactamente el texto con sus espacios y saltos de línea)
raw_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

print("--- EJECUCIÓN DEL SCRIPT DE DATA QUALITY ---\n")

# ==========================================
# STEP 4: Data Profiling (Whitespace Counter)
# ==========================================
# Regla de DQ: El perfilado de datos originales se hace ANTES de cualquier limpieza.
# .isspace() detecta espacios ordinarios, tabulaciones (\t) y saltos de línea (\n).
whitespace_count = sum(1 for char in raw_text if char.isspace())
print(f"Paso 4 -> Total de caracteres de espacio en blanco: {whitespace_count}")
# Validación: Debería dar exactamente 87.


# ==========================================
# STEP 1: Normalization (Letter Cases)
# ==========================================
# Dividimos el texto usando el punto (.) como fin de oración
raw_sentences = raw_text.split('.')

# Filtramos elementos vacíos (como el espacio que queda después del último punto)
sentences = [s for s in raw_sentences if s.strip()]

# Truco de DQ: Si usamos .capitalize() directamente en un texto con saltos de línea
# o espacios al inicio, Python no capitalizará la primera letra real.
# Creamos esta función para buscar la primera letra real y capitalizarla sin romper el formato.
def capitalize_sentence(s):
    for i, char in enumerate(s):
        if char.isalpha():
            # Ponemos la primera letra en mayúscula, el resto en minúscula y preservamos lo anterior
            return s[:i] + char.upper() + s[i+1:].lower()
    return s.lower()

normalized_sentences = [capitalize_sentence(s) for s in sentences]


# ==========================================
# STEP 2: Fixing Typos ("iz" -> "is")
# ==========================================
# Regla de DQ: Evitar falsos positivos. No debemos corregir "iz" si está dentro de comillas
# explicando el error (ej: fix“iZ” con correct “is”).
cleaned_sentences = []
for s in normalized_sentences:
    # Usamos Expresiones Regulares (regex) avanzadas:
    # (?<![“\"\w]) -> Asegura que 'iz' no esté precedido por letras ni comillas (evita fix“iz”)
    # (?![”\"\w]) -> Asegura que 'iz' no esté seguido por letras ni comillas
    cleaned_s = re.sub(r'(?<![“\"\w])iz(?![”\"\w])', 'is', s)
    cleaned_sentences.append(cleaned_s)


# ==========================================
# STEP 3: Extracting Data (The Last Words)
# ==========================================
last_words = []
for s in cleaned_sentences:
    words = s.split()
    if words:
        # Extraemos la última palabra de cada oración limpia
        last_words.append(words[-1])

# Creamos la nueva oración uniendo las palabras extraídas
new_sentence = " ".join(last_words).capitalize() + "."


# ==========================================
# ENSAMBLADO FINAL
# ==========================================
# Unimos las oraciones limpias con su punto original y añadimos la nueva oración al final
cleaned_paragraph = ".".join(cleaned_sentences) + ". " + new_sentence

print("\nTexto Limpio y Normalizado:")
print(cleaned_paragraph)