# =====================================================================
# publication.py (Módulo de Clases)
# =====================================================================
import datetime
import random


class Publication:
    """Clase base para cualquier tipo de publicación."""

    def __init__(self, text: str):
        self.text = text

    def get_formatted_text(self) -> str:
        raise NotImplementedError("Las subclases deben implementar 'get_formatted_text'.")

    def publish(self, filepath: str = "newsfeed.txt") -> None:
        """Guarda la publicación al final del archivo acumulativo."""
        formatted_content = self.get_formatted_text()
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(formatted_content + "\n\n")


class News(Publication):
    """Clase para Noticias."""

    def __init__(self, text: str, city: str):
        super().__init__(text)
        self.city = city
        self.pub_datetime = datetime.datetime.now()

    def get_formatted_text(self) -> str:
        date_str = self.pub_datetime.strftime("%d/%m/%Y %H:%M")
        border = "-" * 30
        return f"News {border}\n{self.text}\n{self.city.title()}, {date_str}\n{border}"


class PrivateAd(Publication):
    """Clase para Anuncios Privados con cálculo de expiración."""

    def __init__(self, text: str, expiration_date_str: str):
        super().__init__(text)
        self.expiration_date = datetime.datetime.strptime(expiration_date_str.strip(), "%Y-%m-%d").date()

    def get_formatted_text(self) -> str:
        today = datetime.date.today()
        days_left = (self.expiration_date - today).days

        if days_left < 0:
            days_status = f"Expired {-days_left} days ago"
        elif days_left == 0:
            days_status = "Expires today"
        else:
            days_status = f"{days_left} days left"

        date_formatted = self.expiration_date.strftime("%d/%m/%Y")
        border = "-" * 30
        return f"Private Ad {border}\n{self.text}\nActual until: {date_formatted}, {days_status}\n{border}"


class JokeOfTheDay(Publication):
    """Clase para Chistes (Tu clase única)."""

    def __init__(self, setup: str, punchline: str):
        super().__init__(setup)
        self.punchline = punchline
        self.funny_rating = random.randint(1, 10)

    def get_formatted_text(self) -> str:
        border = "-" * 30
        return f"Joke of the Day {border}\nWhy: {self.text}\nBecause: {self.punchline}\nFunny Rating: {self.funny_rating}/10\n{border}"