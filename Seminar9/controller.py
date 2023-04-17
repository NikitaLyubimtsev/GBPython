import view
import model
import text_fields as txt


def start_pd():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)
            case 2:
                model.save_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = model.get_pb()
                view.show_contact(pb, txt.no_contact_or_file)
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                model.save_file()
                model.load_file()
                view.print_info(txt.new_contact_successful)
            case 5:
                request = view.search_request(txt.search_request)
                search_result = model.search_contact(request)
                view.show_contact(search_result[0], txt.no_contact_or_file)
            case 6:
                request = view.search_request(txt.search_edit_contact)
                search_result = model.search_contact(request)
                while len(search_result[0]) != 1:
                    view.print_info(txt.overflow_search)
                    view.show_contact(search_result[0], txt.no_contact_or_file)
                    request = view.search_request(txt.repeat_search)
                    search_result = model.search_contact(request)
                view.show_contact(search_result[0], txt.no_contact_or_file)
                edit_contact = view.edit_contact(search_result[0], txt.edit_field_coich)
                model.edit_contact(search_result[1], edit_contact)
                model.save_file()
                model.load_file()
                view.print_info(txt.edit_contact_successful)
            case 7:
                request = view.search_request(txt.search_delete_contact)
                search_result = model.search_contact(request)
                while len(search_result[0]) != 1:
                    view.print_info(txt.overflow_search)
                    view.show_contact(search_result[0], txt.no_contact_or_file)
                    request = view.search_request(txt.repeat_search)
                    search_result = model.search_contact(request)
                view.show_contact(search_result[0], txt.no_contact_or_file)
                model.delete_contact(search_result[1])
                model.save_file()
                model.load_file()
                view.print_info(txt.delete_contact_successful)
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_change):
                        model.save_file()
                    view.print_info(txt.bye)
                    exit()
