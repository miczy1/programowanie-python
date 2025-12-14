from log_reader import LogReader
from test_data_gen import generate_logs
import os


def main():
    if not os.path.exists("server_logs.txt"):
        generate_logs()

    print("--- TEST 1: Wyszukiwanie 'ERROR' (pętla for) ---")
    error_reader = LogReader("server_logs.txt", "ERROR")

    for line in error_reader:
        print(f"Znaleziono: {line}")

    print("\n--- TEST 2: Wyszukiwanie 'INFO' (ręczne wywołanie next) ---")
    info_reader = LogReader("server_logs.txt", "INFO")
    iterator = iter(info_reader)  # Wywołanie __iter__

    try:
        print(f"1: {next(iterator)}")
        print(f"2: {next(iterator)}")
        print(f"3: {next(iterator)}")
        print("(Przerwanie ręczne...)")
    except StopIteration:
        print("Koniec pliku.")

    print("\n--- TEST 3: Słowo, którego nie ma ---")
    empty_reader = LogReader("server_logs.txt", "KRYTYCZNY_BLAD")
    found = False
    for line in empty_reader:
        print(line)
        found = True

    if not found:
        print("Nie znaleziono żadnych linii (prawidłowe zachowanie).")


if __name__ == "__main__":
    main()