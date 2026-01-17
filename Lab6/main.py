from models.product import Product
from logic.cart import Cart

def main():
    products = [
        Product("Laptop", 3500, "electronics"),
        Product("Telefon", 2500, "electronics"),
        Product("Jabłko", 2.5, "food"),
        Product("Gruszka", 3.0, "food")
    ]

    cart = Cart()

    while True:
        print("\n--- WIRTUALNY SKLEP ---")
        print("1. Wyświetl produkty")
        print("2. Dodaj produkt do koszyka")
        print("3. Wyświetl koszyk")
        print("4. Wyświetl sumę")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            print("\nDostępne produkty:")
            for i, product in enumerate(products):
                print(f"{i + 1}. {product}")

        elif choice == "2":
            print("\nKtóry produkt dodać?")
            for i, product in enumerate(products):
                print(f"{i + 1}. {product}")

            try:
                index = int(input("Numer produktu: ")) - 1
                cart.add_product(products[index])
                print("Produkt dodany do koszyka.")
            except (ValueError, IndexError):
                print("Nieprawidłowy wybór.")

        elif choice == "3":
            print()
            print(cart)

        elif choice == "4":
            print(f"\nŁączna cena: {cart.total_price():.2f} zł")

        elif choice == "0":
            print("Koniec programu.")
            break

        else:
            print("Nieznana opcja.")

if __name__ == "__main__":
    main()
