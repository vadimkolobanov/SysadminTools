def display_menu():
    print("Меню:")
    print("1. Пункт меню 1")
    print("2. Пункт меню 2")
    print("3. Пункт меню 3")
    print("4. Выход")


def process_choice(choice):
    if choice == "1":
        print("Вы выбрали пункт меню 1")
    elif choice == "2":
        print("Вы выбрали пункт меню 2")
    elif choice == "3":
        print("Вы выбрали пункт меню 3")
    elif choice == "4":
        print("Выход из меню")
    else:
        print("Неверный выбор")


def main():
    while True:
        display_menu()
        choice = input("Выберите пункт меню: ")
        process_choice(choice)
        if choice == "4":
            break


if __name__ == "__main__":
    main()
