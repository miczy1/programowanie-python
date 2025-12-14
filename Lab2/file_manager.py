import datetime


class FileManager:
    @staticmethod
    def save_report(filename, stats, counts, var_stats, reversed_data):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("--- RAPORT ANALIZY DANYCH ---\n")
                f.write(f"Data generowania: {datetime.datetime.now()}\n\n")

                f.write("1. PODSTAWOWE STATYSTYKI:\n")
                f.write(f"- Liczba elementów: {stats['total_count']}\n")
                f.write(f"- Suma: {stats['sum']}\n")
                f.write(f"- Średnia: {stats['average']:.2f}\n")
                f.write(f"- Max: {stats['max']}\n")
                f.write(f"- Min: {stats['min']}\n\n")

                f.write("2. STRUKTURA DANYCH:\n")
                f.write(f"- Dodatnie: {counts['positive']}\n")
                f.write(f"- Ujemne: {counts['negative']}\n")
                f.write(f"- Zera: {counts['zeros']}\n\n")

                f.write("3. ZAAWANSOWANE:\n")
                f.write(f"- Wariancja: {var_stats['variance']:.2f}\n")
                f.write(f"- Odchylenie standardowe: {var_stats['std_dev']:.2f}\n\n")

                f.write("4. ODWRÓCONA KOLEJNOŚĆ:\n")
                f.write(str(reversed_data))

            print(f"✅ Wyniki zapisano pomyślnie do pliku: {filename}")
        except IOError as e:
            print(f"❌ Błąd zapisu do pliku: {e}")