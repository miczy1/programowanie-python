import json
import os


class Book:
    def __init__(self, title, author, year, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def borrow_book(self):
        """Zmienia status książki na niedostępną, jeśli to możliwe."""
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        """Zmienia status książki na dostępną."""
        self.is_available = True

    def to_dict(self):
        """Serializacja: zamienia obiekt na słownik (do zapisu JSON)."""
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_available": self.is_available
        }

    @classmethod
    def from_dict(cls, data):
        """Deserializacja: tworzy obiekt Book na podstawie słownika."""
        return cls(data["title"], data["author"], data["year"], data["is_available"])

    def __str__(self):
        status = "Dostępna" if self.is_available else "Wypożyczona"
        return f"'{self.title}' - {self.author} ({self.year}) [{status}]"


class Library:
    def __init__(self, storage_file="library_data.json"):
        self.books = []
        self.storage_file = storage_file
        self.load_books()  # Automatyczny odczyt przy starcie

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"✅ Dodano książkę: {title}")

    def list_books(self):
        if not self.books:
            print("📭 Biblioteka jest pusta.")
            return

        print("\n--- KATALOG KSIĄŻEK ---")
        for index, book in enumerate(self.books, 1):
            print(f"{index}. {book}")
        print("-" * 30)

    def search_books(self, query):
        """Wyszukiwanie po tytule lub autorze (case-insensitive)."""
        query = query.lower()
        found_books = [
            book for book in self.books
            if query in book.title.lower() or query in book.author.lower()
        ]

        if found_books:
            print(f"\n🔍 Znaleziono {len(found_books)} pasujących książek:")
            for book in found_books:
                print(f" - {book}")
        else:
            print("❌ Nie znaleziono pasujących książek.")

    def borrow_book_by_index(self, index):
        if 0 <= index < len(self.books):
            book = self.books[index]
            if book.borrow_book():
                self.save_books()
                print(f"📖 Pomyślnie wypożyczono: '{book.title}'")
            else:
                print(f"⛔ Książka '{book.title}' jest już wypożyczona.")
        else:
            print("❌ Nieprawidłowy numer książki.")

    def return_book_by_index(self, index):
        if 0 <= index < len(self.books):
            book = self.books[index]
            book.return_book()
            self.save_books()
            print(f"📥 Zwrócono książkę: '{book.title}'")
        else:
            print("❌ Nieprawidłowy numer książki.")

    def save_books(self):
        """Zapisuje stan biblioteki do pliku JSON."""
        try:
            # Konwertujemy listę obiektów na listę słowników
            data = [book.to_dict() for book in self.books]
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Błąd zapisu danych: {e}")

    def load_books(self):
        """Wczytuje stan biblioteki z pliku JSON przy starcie."""
        if not os.path.exists(self.storage_file):
            return  # Plik nie istnieje, zaczynamy z pustą biblioteką

        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Konwertujemy z powrotem słowniki na obiekty Book
                self.books = [Book.from_dict(item) for item in data]
            print(f"📂 Wczytano {len(self.books)} książek z bazy danych.")
        except (IOError, json.JSONDecodeError):
            print("⚠️ Błąd odczytu pliku danych. Rozpoczynanie z pustą bazą.")
            self.books = []