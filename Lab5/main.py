from queens import Board, solve_n_queens
import time


def run_tests():
    print("=== TESTY JEDNOSTKOWE (zgodne z wymaganiami) ===")

    test_cases = [
        (1, 1),  # 1 rozwiązanie
        (2, 0),  # 0 rozwiązań
        (3, 0),  # 0 rozwiązań
        (4, 2),  # 2 rozwiązania
        (8, 92)  # 92 rozwiązania
    ]

    for n, expected in test_cases:
        count, _ = solve_n_queens(n)
        status = "✅ OK" if count == expected else f"❌ BŁĄD (oczekiwano {expected})"
        print(f"solve({n}) -> znaleziono: {count} | {status}")


def show_example_visualization():
    print("\n=== WIZUALIZACJA (Metody magiczne) ===")

    board = Board(4)
    board.solve()

    if board.solutions:
        board.queens = board.solutions[0]

        print(f"1. Reprezentacja tekstowa (__str__):\n{board}")

        print(f"\n2. Iteracja (__iter__):")
        for pos in board:
            print(f" - Królowa na pozycji: {pos}")

        print(f"\n3. Sprawdzenie obecności (__contains__):")
        test_pos = (0, 1)  # Przykładowa pozycja (wiersz 0, kol 1)
        if test_pos in board:
            print(f" - Czy pozycja {test_pos} jest zajęta? TAK")
        else:
            print(f" - Czy pozycja {test_pos} jest zajęta? NIE")

        print(f"\n4. Liczba królowych (__len__): {len(board)}")


def main():
    start_time = time.time()

    run_tests()
    show_example_visualization()

    end_time = time.time()
    print(f"\nCzas wykonania: {end_time - start_time:.4f} sek")


if __name__ == "__main__":
    main()