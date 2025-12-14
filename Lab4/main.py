from library import Library


def get_int_input(prompt):
    """Pomocnicza funkcja do bezpiecznego pobierania liczb."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Błąd: Wprowadź liczbę całkowitą.")


def main():
    library = Library()  # Tu nastąpi automatyczne wczytanie danych z JSON

    while True:
        print("\n=== SYSTEM BIBLIOTECZNY ===")
        print("1. Wyświetl wszystkie książki")
        print("2. Dodaj nową książkę")
        print("3. Wypożycz książkę")
        print("4. Zwróć książkę")
        print("5. Szukaj książki (Autor/Tytuł)")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            library.list_books()

        elif choice == '2':
            title = input("Podaj tytuł: ")
            author = input("Podaj autora: ")
            year = get_int_input("Podaj rok wydania: ")
            library.add_book(title, author, year)

        elif choice == '3':
            library.list_books()
            if library.books:
                idx = get_int_input("Podaj numer książki do wypożyczenia: ")
                library.borrow_book_by_index(idx - 1)

        elif choice == '4':
            library.list_books()
            if library.books:
                idx = get_int_input("Podaj numer książki do zwrotu: ")
                library.return_book_by_index(idx - 1)

        elif choice == '5':
            query = input("Wpisz frazę do wyszukania: ")
            library.search_books(query)

        elif choice == '0':
            print("Zamykanie systemu. Dane są bezpieczne w pliku JSON.")
            break

        else:
            print("Nieznana opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main()