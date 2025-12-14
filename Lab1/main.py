import sys

try:
    import winsound
    SYSTEM_AUDIO = True
except ImportError:
    SYSTEM_AUDIO = False


def play_sound(is_healthy):
    if SYSTEM_AUDIO:
        if is_healthy:
            winsound.Beep(1000, 200)
        else:
            winsound.Beep(300, 800)


def get_valid_input(message):
    while True:
        try:
            user_input = input(message)
            value = float(user_input.replace(',', '.'))
            if value > 0:
                return value
            else:
                print("Błąd: Wartość musi być dodatnia. Spróbuj ponownie.")
        except ValueError:
            print("Błąd: To nie jest liczba. Spróbuj ponownie.")


def main():
    print("--- KALKULATOR BMI ---")

    while True:
        height_cm = get_valid_input("Podaj wzrost (w cm): ")
        weight_kg = get_valid_input("Podaj masę ciała (w kg): ")

        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        bmi_rounded = round(bmi, 2)

        description = ""
        is_healthy = False

        if bmi < 18.5:
            description = "Niedowaga"
            is_healthy = False
        elif 18.5 <= bmi <= 24.9:
            description = "Waga prawidłowa"
            is_healthy = True
        elif 25.0 <= bmi <= 29.9:
            description = "Nadwaga"
            is_healthy = False
        else:
            description = "Otyłość"
            is_healthy = False

        print("-" * 30)
        print(f"Twój wynik BMI: {bmi_rounded}")
        print(f"Interpretacja: {description}")

        play_sound(is_healthy)
        print("-" * 30)

        decision = input("Czy chcesz obliczyć BMI dla kolejnej osoby? (t/n): ").lower()
        if decision != 't' and decision != 'tak':
            break
        print("\n")


if __name__ == "__main__":
    main()