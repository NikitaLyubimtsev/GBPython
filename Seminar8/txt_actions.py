file_dir = 'seminar8/tel.txt'
field = ["Имя контактактк: ", "Номер телефона: ", "Коментарий: "]

def contact_format(contact):
    return ' '.join(contact.split(';'))

def show_all():
    with open(file_dir, 'r', encoding="UTF-8") as f:
        data = f.readlines()
    [print(f"{p + 1}. {contact_format(data[p])}") for p in range(len(data))]


def add_new_record():
    new_entry = ';'.join([input(f"Введите {field[i].lower()}") for i in range(len(field))])
    with open(file_dir, 'a', encoding='UTF-8') as f:
        f.write(f'\n{new_entry}')



def search(data):
    search_request = input("Введите поисковый запрос: ").lower()
    if search_request == "":
        print("Запрос не введён!")
    else:
        count = 0
        index = None
        for idx, s in enumerate(data):
            if s.lower().find(search_request) > -1:
                index = idx
                count += 1

    return [count, search_request, index]

def delete_record():
        with open(file_dir, 'r', encoding='UTF-8') as f:
            data = f.readlines()
        res_search = search(data)
        if res_search[0] == 1:
            old_text = data[res_search[2]]
            replacment = data[res_search[2]].replace(old_text, '')
            with open(file_dir, 'w', encoding='UTF-8') as f:
                f.truncate(0)
                f.writelines(data)
            print("Поле записи удачно удалено!")
        elif res_search[0] > 1:
            print("Пожалуйста, уточните запрос: ")
            [print(f"{str + 1}. {contact_format(data[str])}") for str in range(len(data)) if data[str].lower().find(res_search[1]) > -1]
            delete_record()
        else:
            print("По запросу ничего не найдено")

def edit_record():
    with open(file_dir, 'r', encoding="UTF-8") as f:
        data = f.readlines()
    res_search = search(data)
    if res_search[0] == 1:
        [print(f"{i + 1}. {field[i]} {data[res_search[2]].split(';')[i]}") for i in range(len(field))]
        rep_field = int(input("Введите номер поля для изменения: "))
        old_text = data[res_search[2]].split(';')[rep_field - 1]
        new_text = input("Введите текст для замены: ") + ("" if res_search[2] < 2 else "\n")
        replacement = data[res_search[2]].replace(old_text, new_text)
        data[res_search[2]] = replacement
        with open(file_dir, 'w', encoding='UTF-8') as f:
            f.truncate(0)
            f.writelines(data)
        print("Поле записи удачно изменено!")
    elif res_search[0] > 1:
        print("Пожалуйста, уточните запрос: ")
        [print(f"{str + 1}. {contact_format(data[str])}") for str in range(len(data)) if data[str].lower().find(res_search[1]) > -1]
        edit_record()
    else:
        print("По запросу ничего не найдено")



def search_record():
    with open(file_dir, 'r', encoding='UTF-8') as f:
        data = f.readlines()

    res_search = search(data)
    if res_search[0] > 0:
        find_text = res_search[1]
        [print(f"{str + 1}. {contact_format(data[str])}") for str in range(len(data)) if data[str].lower().find(res_search[1]) > -1]
    else:
        print(f"Записей по запросу: '{res_search[1]}' не обнаруженно")
