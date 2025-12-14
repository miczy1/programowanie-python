def generate_logs():
    lines = [
        "2023-10-27 10:00:01 [INFO] Uruchomienie serwera",
        "2023-10-27 10:05:23 [ERROR] Nieudane połączenie z bazą danych",
        "2023-10-27 10:06:00 [INFO] Próba ponownego połączenia...",
        "2023-10-27 10:06:05 [INFO] Połączenie udane",
        "2023-10-27 10:15:00 [WARNING] Wysokie zużycie pamięci RAM",
        "2023-10-27 10:20:00 [ERROR] Timeout zapytania API",
        "2023-10-27 10:30:00 [INFO] Zamknięcie serwera"
    ]

    with open("server_logs.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print("Utworzono plik testowy: server_logs.txt")


if __name__ == "__main__":
    generate_logs()