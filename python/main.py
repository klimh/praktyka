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

    print("\n" + "=" * 30)
    print(f"TWOJE HASŁO: {new_password}")
    print("=" * 30)

main()