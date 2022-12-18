from datetime import datetime


def get_book_type():
    while True:
        try:
            type = int(input("С каким форматом будете работать? (1 – csv, 2 – txt): "))
            if type == 1 or type == 2: return type
        except: print("Некорректный ввод!")


def get_choice():
    while True:
        try:
            return int(input("1 – отобразить все контакты,\
                            \n2 – добавить контакт в телефонную книгу,\
                            \n3 – найти контакт в телефонной книге,\
                            \n4 – редактировать запись,\
                            \n5 – удалить запись,\
                            \n6 – отобразить всех сегодняшних именинников,\
                            \n7 – выход\
                            \nВыберите действие: "))
        except: print("Некорректный выбор!")


def get_contact_data(entry, action = None):
    if action is None:
        while True:
            entry.surname = input("Фамилия: ")
            if entry.surname.isalpha(): break
        while True:
            entry.name = input("Имя: ")
            if entry.name.isalpha(): break
        while True:
            entry.birthday = input("День рождения (формат – dd.mm.yyyy): ")
            try:
                if datetime.strptime(entry.birthday, '%d.%m.%Y'): break
            except: print("Некорректный ввод!")
        while True:
            entry.phone = input("Номер телефона (формат – только цифры): ")
            if entry.phone.isdigit(): break
    else:
        while True:
            surname = input("Новая фамилия (Enter, чтобы пропустить): ")
            if surname.isalpha(): entry.surname = surname
            if entry.surname == surname or len(surname) == 0: break
        while True:
            name = input("Новое имя (Enter, чтобы пропустить): ")
            if name.isalpha(): entry.name = name
            if entry.name == name or len(name) == 0: break
        while True:
            birthday = input("Новый день рождения (формат – dd.mm.yyyy, Enter, чтобы пропустить): ")
            try:
                if datetime.strptime(birthday, '%d.%m.%Y'): entry.birthday = birthday
                if entry.birthday == birthday: break
            except:
                if len(birthday) == 0: break
                else: print("Некорректный ввод!")
        while True:
            phone = input("Новый номер телефона (формат – только цифры, Enter, чтобы пропустить): ")
            if phone.isdigit(): entry.phone = phone
            if entry.phone == phone or len(phone) == 0: break
    return entry


def get_surname():
    return input("Введите фамилию для поиска: ")