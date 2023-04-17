import controller
from classes import Contact
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


def show_contact(book: list[Contact], message: str):
    print('\n' + '-' * 68)
    if book:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact}')
       # [formatter_contact(idx, contact) for idx, contact in enumerate(book, 1)]
    else:
        print(message)
    print('-' * 68 + '\n')


def new_contact() -> Contact:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return Contact(name, phone, comment)


def search_request(message: str):
    return input(message)


def input_index(phone_book: list[Contact], message: str) -> int:
    index = input(message)
    if index.isdigit() & 0 < int(index) < len(phone_book) - 1:
        return int(index)
    else:
        print(txt.failed_input)
        input_index(phone_book, message)


def edit_contact(book: list, message: str) -> tuple[int, Contact]:
    index = 0
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) + 1:
            index = int(choice)
            break
    print(txt.enter_or_empty)
    contact = new_contact()
    return index, contact


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
