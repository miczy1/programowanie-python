from stats_engine import StatsEngine
from file_manager import FileManager
from visualizer import DataVisualizer


def get_input_data():
    raw_input = input("Wprowadź liczby całkowite oddzielone spacją: ")
    if not raw_input.strip():
        return []

    try:
        return [int(x) for x in raw_input.split()]
    except ValueError:
        print("❌ Błąd: Wprowadzono niedozwolone znaki. Używaj tylko liczb całkowitych.")
        return None


def main():
    while True:
        print("\n" + "=" * 40)
        print(" ANALIZATOR LICZB v2.0")
        print("=" * 40)

        data = get_input_data()

        if data is None:
            continue

        if not data:
            print("⚠️ Nie wprowadzono żadnych danych.")
        else:
            engine = StatsEngine(data)

            stats = engine.get_basic_stats()
            counts = engine.get_pos_neg_zeros()
            var_stats = engine.get_variance_std_dev()
            reversed_data = engine.get_reversed_data()

            print("\n--- WYNIKI ---")
            print(f"Liczb: {stats['total_count']}")
            print(f"Suma: {stats['sum']} | Średnia: {stats['average']:.2f}")
            print(f"Min: {stats['min']} | Max: {stats['max']}")
            print(f"Dodatnie: {counts['positive']} | Ujemne: {counts['negative']} | Zera: {counts['zeros']}")
            print(f"Wariancja: {var_stats['variance']:.2f}")
            print(f"Odchylenie std: {var_stats['std_dev']:.2f}")
            print(f"Odwrócona lista: {reversed_data}")

            save_decision = input("\nCzy zapisać wyniki do pliku? (t/n): ").lower()
            if save_decision == 't':
                FileManager.save_report("wyniki_analizy.txt", stats, counts, var_stats, reversed_data)

            chart_decision = input("Czy wyświetlić wykresy? (t/n): ").lower()
            if chart_decision == 't':
                print("Generowanie wykresów...")
                DataVisualizer.show_charts(data, counts)

        restart = input("\nCzy chcesz wprowadzić nowe dane? (t/n): ").lower()
        if restart != 't':
            print("Zamykanie programu...")
            break


if __name__ == "__main__":
    main()