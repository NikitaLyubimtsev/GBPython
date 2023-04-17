raw_data = []
phone_book = []
start_phone_book = []
PATH = 'phone_book.txt'


def get_pb():
    return phone_book


def load_file():
    with open(PATH, 'r', encoding="UTF-8") as file:
        data = file.readlines()
    raw_data.clear()
    [raw_data.append(c) for c in data]
    phone_book.clear()
    [phone_book.append(c) for c in pb_serialise(raw_data)]
    start_phone_book.append(phone_book)


def save_file():
    data = raw_data
    with open(PATH, 'w', encoding="UTF-8") as file:
        file.truncate(0)
        file.writelines(data)


def add_contact(contact: dict):
    raw_data.append(";".join(contact.values()) + '\n')


def search_contact(request: str) -> list:
    data = []
    index = None
    for idx, contact in enumerate(raw_data):
        if request.lower() in contact.lower():
            data.append(contact)
            index = idx

    return [pb_serialise(data), index]


def edit_contact(index_field: int, edit_field: list):
    new_txt = edit_field[1]
    old_txt = raw_data[index_field].split(';')[edit_field[0] - 1]
    replacement = raw_data[index_field].replace(old_txt, new_txt)
    raw_data[index_field] = replacement


def delete_contact(index: int):
    delete_cont = raw_data[index].replace(raw_data[index], '')
    raw_data[index] = delete_cont


def exit_pb() -> bool:
    if phone_book == start_phone_book:
        return False
    else:
        return True


# -------------------------------------------------
# Service methods

def pb_serialise(data: list) -> list[dict]:
    result = []
    for contact in data:
        contact = contact.strip().split(';')
        result.append({'name': contact[0],
                       'phone': contact[1],
                       'comment': contact[2]})
    return result
