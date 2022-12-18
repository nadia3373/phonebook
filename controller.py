import model, view


def start():
    type = view.get_book_type()
    while True:
        choice = view.get_choice()
        if choice == 1: model.get_contacts(type)
        elif choice == 2: model.add_contact(type, view.get_contact_data(model.Entry()))
        elif choice == 3: model.get_contacts(type, "search", view.get_surname())
        elif choice == 4: model.manage_contact("edit", model.get_contacts(type, "edit", view.get_surname()), type)
        elif choice == 5: model.manage_contact("delete", model.get_contacts(type, "delete", view.get_surname()), type)
        elif choice == 6: model.get_contacts(type, "birthday")
        elif choice == 7: break