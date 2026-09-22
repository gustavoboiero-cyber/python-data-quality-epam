import datetime
import random
from typing import NoReturn


# ==========================================
# 🏛️ CLASES (ARQUITECTURA DE OBJETOS)
# ==========================================

class Publication:
    """
    Clase Base (Parent Class).
    Representa una publicación genérica en el feed de noticias.
    """

    def __init__(self, text: str):
        self.text = text

    def get_formatted_text(self) -> str:
        """
        Método plantilla que será sobrescrito por cada clase hija
        para retornar su formato de texto específico.
        """
        raise NotImplementedError("Las subclases deben implementar el método 'get_formatted_text'.")

    def publish(self, filepath: str = "newsfeed.txt") -> None:
        """
        Guarda la publicación en el archivo de texto.
        Este comportamiento es idéntico para todas las clases hijas,
        por lo que se define una sola vez aquí (Herencia).
        """
        formatted_content = self.get_formatted_text()

        # Abrimos en modo 'a' (append) para añadir al final sin sobreescribir el archivo.
        # Definimos encoding='utf-8' para evitar problemas con caracteres especiales (acentos, ñ, emojis).
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(formatted_content + "\n\n")

        print(f"✅ ¡Publicado con éxito en '{filepath}'!")


class News(Publication):
    """
    Clase Hija para Noticias.
    Calcula la fecha y hora de publicación de forma automática.
    """

    def __init__(self, text: str, city: str):
        super().__init__(text)  # Llama al constructor de la clase base
        self.city = city
        self.pub_datetime = datetime.datetime.now()

    def get_formatted_text(self) -> str:
        # Formateamos la fecha y hora: "DD/MM/YYYY HH:MM"
        date_str = self.pub_datetime.strftime("%d/%m/%Y %H:%M")
        border = "-" * 30

        return (
            f"News {border}\n"
            f"{self.text}\n"
            f"{self.city.title()}, {date_str}\n"
            f"{border}"
        )


class PrivateAd(Publication):
    """
    Clase Hija para Anuncios Privados.
    Calcula cuántos días faltan para que el anuncio expire.
    """

    def __init__(self, text: str, expiration_date_str: str):
        super().__init__(text)
        # Convertimos el string de la fecha (YYYY-MM-DD) a un objeto 'date' real para hacer cálculos
        self.expiration_date = datetime.datetime.strptime(expiration_date_str, "%Y-%m-%d").date()

    def get_formatted_text(self) -> str:
        today = datetime.date.today()
        # Restamos las fechas para obtener la diferencia de días
        days_left = (self.expiration_date - today).days

        # Formateamos el mensaje de vencimiento
        if days_left < 0:
            days_status = f"Expired {-days_left} days ago"
        elif days_left == 0:
            days_status = "Expires today"
        else:
            days_status = f"{days_left} days left"

        date_formatted = self.expiration_date.strftime("%d/%m/%Y")
        border = "-" * 30

        return (
            f"Private Ad {border}\n"
            f"{self.text}\n"
            f"Actual until: {date_formatted}, {days_status}\n"
            f"{border}"
        )


class JokeOfTheDay(Publication):
    """
    Clase Hija Única (Joke).
    Utiliza el setup del chiste como texto base, requiere un remate (punchline)
    y genera una calificación aleatoria de gracia.
    """

    def __init__(self, setup: str, punchline: str):
        super().__init__(setup)  # El setup actúa como el texto de la publicación
        self.punchline = punchline
        # Lógica de cálculo aleatorio
        self.funny_rating = random.randint(1, 10)

    def get_formatted_text(self) -> str:
        border = "-" * 30
        return (
            f"Joke of the Day {border}\n"
            f"Why: {self.text}\n"
            f"Because: {self.punchline}\n"
            f"Funny Rating: {self.funny_rating}/10\n"
            f"{border}"
        )


# ==========================================
# 🛠️ FUNCIONES DE VALIDACIÓN (DATA QUALITY)
# ==========================================

def get_non_empty_input(prompt: str) -> str:
    """Valida que el usuario ingrese un texto que no sea puramente espacios vacíos."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❌ El campo no puede estar vacío. Por favor, intenta de nuevo.")


def get_validated_date(prompt: str) -> str:
    """Valida que la fecha ingresada tenga el formato correcto YYYY-MM-DD."""
    while True:
        date_str = input(prompt).strip()
        try:
            # Intentamos parsear la fecha para verificar que exista y tenga el formato correcto
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Formato de fecha inválido. Debe ser YYYY-MM-DD (ejemplo: 2026-12-31).")


# ==========================================
# 🖥️ MENÚ INTERACTIVO (MAIN LOOP)
# ==========================================

def run_menu() -> NoReturn:
    print("=========================================")
    print("📰 BIENVENIDO AL GENERADOR DE NEWS FEED 📰")
    print("=========================================")

    while True:
        print("\n¿Qué tipo de registro te gustaría añadir?")
        print("1 - Añadir una Noticia (News)")
        print("2 - Añadir un Anuncio Privado (Private Ad)")
        print("3 - Añadir un Chiste del Día (Joke of the Day)")
        print("0 - Salir del programa")

        choice = input("👉 Selecciona una opción: ").strip()

        if choice == "1":
            print("\n[Añadir Noticia]")
            text = get_non_empty_input("Ingresa el cuerpo de la noticia: ")
            city = get_non_empty_input("Ingresa la ciudad de la noticia: ")

            # Instanciamos el objeto y llamamos al método heredar publish
            news_item = News(text, city)
            news_item.publish()

        elif choice == "2":
            print("\n[Añadir Anuncio Privado]")
            text = get_non_empty_input("Ingresa el texto del anuncio: ")
            exp_date = get_validated_date("Ingresa la fecha de expiración (YYYY-MM-DD): ")

            ad_item = PrivateAd(text, exp_date)
            ad_item.publish()

        elif choice == "3":
            print("\n[Añadir Chiste del Día]")
            setup = get_non_empty_input("Premisa del chiste (Setup): ")
            punchline = get_non_empty_input("Remate del chiste (Punchline): ")

            joke_item = JokeOfTheDay(setup, punchline)
            joke_item.publish()

        elif choice == "0":
            print("\n¡Gracias por utilizar el News Feed Generator! ¡Hasta luego! 👋")
            break

        else:
            print("❌ Opción inválida. Por favor, selecciona 1, 2, 3 o 0.")


if __name__ == "__main__":
    run_menu()