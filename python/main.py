import secrets
import string


def generate_password(length: int, is_complicated: bool) -> str:
    pula = string.ascii_letters + string.digits

    if is_complicated:
        pula += string.punctuation
        print("Pula została rozszerzona o znaki specjalne")

    return "".join(secrets.choice(pula) for _ in range(length))



def main():
    while True:
        try:
            password_length_wish = int(input("Podaj jak długie ma być twoje hasło (od 8 do 64 znaków) "))
            if password_length_wish in range(8,65):
                print(f"Wybrałeś hasło o długości: {password_length_wish}")
                break

            else:
                print("Wybrane hasło nie mieści się w ustalonym przedziale [8-64]! Powtórz")
        except ValueError:
            print("To nie są liczby, podaj liczbę (np. 12)!")

    while True:
        is_password_complicated = input("Czy hasło ma zawierać znaki specjalne? (t/n): ").lower()
        if is_password_complicated == "t":
            print("Dodajemy znaki!")
            break

        elif is_password_complicated == "n":
            print("Będą same litery i cyfry")
            break

        else:
            print("Wprowadziłeś złą literę, powtórz!")

    new_password = generate_password(password_length_wish, is_password_complicated == "t")
    is_password_safe = is_password_is_complicated(new_password)

    print("\n" + "=" * 30)
    print(f"TWOJE HASŁO: {new_password}")
    print(f"OCENA HASŁA: {is_password_safe} ")
    print("=" * 30)

    is_safe_password = input("Czy chcesz zapisać hasło do pliku? (t/n): ").lower()

    if is_safe_password == "t":
        password_name = input("Podaj nazwę dla tego hasła: ")

        with open("my_passwords.txt", "a", encoding = "utf8") as file:
            file.write(f"Nazwa: {password_name}, Hasło: {new_password}, Siła: {is_password_safe}\n")
        print("Pomyślnie zapisano hasło!")
    else:
        print("Hasło nie zostało zapisane.")

def is_password_is_complicated(password):
    has_special = any(char in string.punctuation for char in password)
    if len(password) < 10:
        return "Weak."
    elif len(password) > 40 and has_special:
        return "Strong."
    else:
        return "Mid."


if __name__ == "__main__":
    main()