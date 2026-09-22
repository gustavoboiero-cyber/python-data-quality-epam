# =====================================================================
# news_feed_generator.py (Menú interactivo y punto de entrada)
# =====================================================================
import os
import datetime
# Importamos las clases e importamos el procesador desde los otros módulos
from publication import News, PrivateAd, JokeOfTheDay
from batch_processor import BatchProcessor

def get_non_empty_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❌ El campo no puede estar vacío. Intenta de nuevo.")

def get_validated_date(prompt: str) -> str:
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Formato inválido. Debe ser YYYY-MM-DD (ejemplo: 2026-12-31).")

def run_menu() -> None:
    print("=========================================")
    print("📰 GENERADOR DE NEWS FEED v2.0 (BATCH)  📰")
    print("=========================================")

    while True:
        print("\nSelecciona una opción del menú:")
        print("1 - Añadir Noticia manualmente")
        print("2 - Añadir Anuncio Privado manualmente")
        print("3 - Añadir Chiste del Día manualmente")
        print("4 - Procesar registros desde un archivo (.txt) 🚀")
        print("0 - Salir")

        choice = input("👉 Opción: ").strip()

        if choice == "1":
            text = get_non_empty_input("Texto de la noticia: ")
            city = get_non_empty_input("Ciudad: ")
            News(text, city).publish()
            print("✅ Noticia publicada con éxito.")

        elif choice == "2":
            text = get_non_empty_input("Texto del anuncio: ")
            exp_date = get_validated_date("Fecha de expiración (YYYY-MM-DD): ")
            PrivateAd(text, exp_date).publish()
            print("✅ Anuncio publicado con éxito.")

        elif choice == "3":
            setup = get_non_empty_input("Premisa del chiste: ")
            punchline = get_non_empty_input("Remate del chiste: ")
            JokeOfTheDay(setup, punchline).publish()
            print("✅ Chiste publicado con éxito.")

        elif choice == "4":
            print("\n[Procesar desde Archivo]")
            filepath = input("Ruta del archivo (o Enter para usar './records/default_input.txt'): ").strip()

            # Ruta por defecto
            if not filepath:
                os.makedirs("records", exist_ok=True)
                filepath = os.path.join("records", "default_input.txt")
                print(f"ℹ️ Usando archivo por defecto: {filepath}")

            # Captura de Excepciones para evitar crasheos (Requisito 4)
            try:
                BatchProcessor.process_file(filepath)
            except FileNotFoundError as e:
                print(f"\n❌ Error: {e}")
                print("Por favor, asegúrate de que el archivo exista en la ruta indicada.")
            except Exception as e:
                print(f"\n❌ Error crítico inesperado: {e}")

        elif choice == "0":
            print("\n¡Gracias por utilizar el News Feed Generator! ¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción inválida. Selecciona una opción del menú.")


if __name__ == "__main__":
    run_menu()