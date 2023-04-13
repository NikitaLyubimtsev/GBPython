import os
import txt_actions
# menu_list = {1: ["Показать всю книгу", txt_actions.action_list[0]], 2: "Добавить новую запись", 3: "Редактировать запись", 4: "Найти запись"}
menu_list = {1: "Показать всю книгу", 2: "Добавить новую запись", 3: "Найти запись", 4: "Редактировать запись", 5: "Удалить запись", 6: "Меню действий: ", 7: "Выход"}
def main_menu():
  #  print("Меню действий:")
  #  print("1. Показать всю книгу")
  #  print("2. Добавить новую запись")
  #  print("3. Редактировать запись")
  #  print("4. Найти запись")
  #  print("5. Вернуться к меню действий")
    [print(f"{menu_list[6]} {key}. {value}") for key, value in menu_list.items()]

if __name__ == "__main__":
    main_menu()

    while True:
        choose = int(input("Введите номер выбранного пункта меню: "))
        os.system('cls||clear')
        if choose == 1:
           txt_actions.show_all()
        if choose == 2: 
            txt_actions.add_new_record()
        if choose == 3:
            txt_actions.search_record()
        if choose == 4:
            txt_actions.edit_record()
        if choose == 5:
            txt_actions.delete_record()
        if choose == 6:
            main_menu()            
        if choose == 7:
            break
