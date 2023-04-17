import controller
import text_fields as txt


def main_menu() -> int:
    print('''Главное меню: 
          1. Открыть файл
          2. Сохоанить файл
          3. Показать все контакты
          4. Создать контакт
          5. Найти контакт
          6. Изменить контакт
          7. Удалить контакт
          8. Выход''')
    choice = ''
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print("Введите число от 1 до 8")


def show_contact(book: list[dict], message: str):
    if book:
        print('\n' + '-' * 68)
        [formatter_contact(idx, contact) for idx, contact in enumerate(book, 1)]
        print('-' * 68 + '\n')
    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def search_request(message: str):
    return input(message)


def edit_contact(book: list[dict], message: str) -> list:
    edit_field = None
    choice = None
    if book:
        choice = int(input(message))
        match choice:
            case 1:
                edit_field = input(txt.new_name)
            case 2:
                edit_field = input(txt.new_phone)
            case 3:
                edit_field = input(txt.new_comment)
            case _:
                edit_contact(book, message)
    return [choice, edit_field]


# ----------------------------------------------------------
# Service methods

def print_info(message: str):
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def confirm(message: str) -> bool:
    print()
    answer = input(message + ' (y/n) -> ')
    if answer.lower() == 'y':
        return True
    else:
        return False


def formatter_contact(idx: int, contact: dict):
    print(f'{idx:>3}. {contact.get("name"):<30}{contact.get("phone"):<15}{contact.get("comment"):<20}')
