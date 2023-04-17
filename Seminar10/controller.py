from classes import Contact, PhoneBook
import view
import text_fields as txt


def start_pd():
    phonebook = PhoneBook('phone_book.txt')
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                phonebook.open_file()
                view.print_info(txt.load_successful)
            case 2:
                phonebook.save_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = phonebook.get()
                view.show_contact(pb, txt.no_contact_or_file)
            case 4:
                new_contact = view.new_contact()
                phonebook.add(new_contact)
                view.print_info(txt.contact_saved)
            case 5:
                request = view.search_request(txt.search_request)
                search_result = phonebook.search_contact(request)
                view.show_contact(search_result, txt.no_contact_or_file)
            case 6:
                pb = phonebook.get()
                view.show_contact(pb, txt.no_contact_or_file)
                if pb:
                    edited_contact = view.edit_contact(pb, txt.input_index)
                    phonebook.edit_contact(edited_contact)
                    view.print_info(txt.edit_contact_successful)

                # request = view.search_request(txt.search_edit_contact)
                # search_result = model.search_contact(request)
                # while len(search_result[0]) != 1:
                #     view.print_info(txt.overflow_search)
                #     view.show_contact(search_result[0], txt.no_contact_or_file)
                #     request = view.search_request(txt.repeat_search)
                #     search_result = model.search_contact(request)
                # view.show_contact(search_result[0], txt.no_contact_or_file)
                # edit_contact = view.edit_contact(search_result[0], txt.edit_field_coich)
                # model.edit_contact(search_result[1], edit_contact)
                # model.save_file()
                # model.load_file()
                # view.print_info(txt.edit_contact_successful)
            case 7:
                pb = phonebook.get()
                view.show_contact(pb, txt.no_contact_or_file)
                if pb:
                    index = view.input_index(pb, txt.input_delete_index)
                    if view.confirm(txt.confirm_delete):
                        pb.remove(index - 1)
                        view.print_info(txt.delete_contact_successful)
                # request = view.search_request(txt.search_delete_contact)
                # search_result = model.search_contact(request)
                # while len(search_result[0]) != 1:
                #     view.print_info(txt.overflow_search)
                #     view.show_contact(search_result[0], txt.no_contact_or_file)
                #     request = view.search_request(txt.repeat_search)
                #     search_result = model.search_contact(request)
                # view.show_contact(search_result[0], txt.no_contact_or_file)
                # model.delete_contact(search_result[1])
                # model.save_file()
                # model.load_file()
                # view.print_info(txt.delete_contact_successful)
            case 8:
                if phonebook.save_on_exit():
                    if view.confirm(txt.is_change):
                        phonebook.save_file()
                    view.print_info(txt.bye)
                    exit()
