# =====================================================================
# batch_processor.py (Módulo de Procesamiento por Lotes)
# =====================================================================
import os
# Importamos las clases necesarias desde nuestro nuevo módulo publication
from publication import News, PrivateAd, JokeOfTheDay


class MalformedRecordError(Exception):
    """Excepción personalizada para detectar registros con formato incorrecto."""
    pass


class BatchProcessor:
    """Clase para leer, procesar y eliminar archivos de lote."""

    @staticmethod
    def process_file(filepath: str) -> None:
        # Validación de Data Quality: Comprobamos si el archivo existe
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Sorry, file not found at '{filepath}'. Please try again.")

        print(f"📖 Leyendo y procesando archivo: {filepath}...")

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Separamos los registros por el delimitador '---'
        raw_records = content.split("---")
        processed_count = 0

        for idx, raw_record in enumerate(raw_records, 1):
            # Limpiamos líneas vacías
            lines = [line.strip() for line in raw_record.strip().split("\n") if line.strip()]
            if not lines:
                continue

            try:
                # Cada registro debe tener al menos: Tipo, Contenido, Argumento extra
                if len(lines) < 3:
                    raise MalformedRecordError(
                        f"Faltan campos. Se esperaban al menos 3 líneas, se encontraron {len(lines)}."
                    )

                pub_type = lines[0].lower()
                text = lines[1]
                extra_arg = lines[2]

                # Instanciamos la clase correcta según el tipo de registro
                if pub_type == "news":
                    pub = News(text, extra_arg)
                elif pub_type in ["private ad", "ad"]:
                    pub = PrivateAd(text, extra_arg)
                elif pub_type in ["joke", "joke of the day"]:
                    pub = JokeOfTheDay(text, extra_arg)
                else:
                    raise MalformedRecordError(f"Tipo de publicación desconocido: '{lines[0]}'")

                pub.publish()
                processed_count += 1
                print(f"✔️ Registro {idx} ({pub_type.upper()}) procesado y publicado.")

            except MalformedRecordError as e:
                print(f"⚠️ Error de formato en registro {idx}: {e}. Omitiendo registro...")
            except ValueError as e:
                print(f"⚠️ Error de fecha en registro {idx} (debe ser YYYY-MM-DD): {e}. Omitiendo...")
            except Exception as e:
                print(f"⚠️ Error inesperado en registro {idx}: {e}. Omitiendo...")

        # Eliminación física del archivo para evitar duplicados
        if processed_count > 0:
            print(f"🧹 Limpieza: Eliminando archivo procesado...")
            os.remove(filepath)
            print("🗑️ Archivo de entrada eliminado con éxito.")
        else:
            print("⚠️ No se procesaron registros válidos. El archivo de entrada NO fue eliminado.")