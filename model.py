from datetime import datetime
import logger, os.path, view


class Entry():
    def __init__(self):
        self.surname = ""
        self.name = ""
        self.birthday = ""
        self.phone = ""
        
    def get_keys(self):
        return list(vars(self).keys())
    
    def get_values(self):
        return list(vars(self).values())
    
    def get_translation(self, key):
        if key == "surname": return "Фамилия"
        elif key == "name": return "Имя"
        elif key == "birthday": return "Дата рождения"
        elif key == "phone": return "Номер телефона"
    
    def print(self):
        for key in self.get_keys(): print(f"| {self.get_translation(key)}: {getattr(self, key)} ", end = "")
        print("|\n")


def add_contact(book_type, entry):
    br, extension, delimiter = get_format(book_type)
    if not os.path.isfile(f'book{extension}'):
        with open(f"book{extension}", "a") as f:
            f.write(delimiter.join(entry.get_keys()))
            f.write(br)
            f.write(delimiter.join(entry.get_values()))
            f.write(br)
    else:
        with open(f"book{extension}", "a") as f:
            f.write(delimiter.join(entry.get_values()))
            f.write(br)
    logger.log("add", entry, book_type)
    print("\nКонтакт успешно добавлен.\n")


def contact_from_source(entry, source):
    index = 0
    for key in entry.get_keys():
        setattr(entry, key, source[index])
        index += 1
    return entry


def get_contacts(book_type, action = None, contact = None):
    br, extension, delimiter = get_format(book_type)
    entry = None
    if os.path.isfile(f'book{extension}'):
        with open(f'book{extension}', "r") as f: reader = [x.split(delimiter) for x in f.read().split(br) if x != ""]
        if action in("edit", "delete", "search"): print("Результаты поиска:\n")
        elif action == "birthday": print("Все сегодняшие именинники:\n")
        else: print("Все контакты:\n")
        i = 0
        while i < len(reader):
            to_remove = None
            if reader[i][0] == "surname": to_remove = reader[i]
            elif contact is not None:
                if reader[i][0] != contact: to_remove = reader[i]
            elif contact is None:
                if action == "birthday":
                    if reader[i][2][:-5] != datetime.now().date().strftime('%d.%m'): to_remove = reader[i]
            if to_remove is not None:
                reader.remove(reader[i])
                i -= 1
            i += 1
        entries = []
        for row in reader:
            entry = contact_from_source(Entry(), row)
            entry.print()
            if action in("edit", "delete") and entry is not None: entries.append(entry)
        if len(entries) > 0: return entries
    if entry is None: print("Ваша телефонная книга пуста или в ней нет запрошенного контакта.\n")


def get_format(type):
    return ("\n", ".csv", ",") if type == 1 else ("\n\n", ".txt", "\n")


def manage_contact(action, entries, book_type):
    br, extension, delimiter = get_format(book_type)
    count = 0
    if entries is not None:
        for entry in entries:
            with open(f'book{extension}', "r") as f: reader = [x.split(delimiter) for x in f.read().split(br) if x != ""]
            with open(f'temp{extension}', "w") as f:
                for row in reader:
                    if row[0] != entry.surname or row[1] != entry.name or row[2] != entry.birthday or row[3] != entry.phone:
                        f.write(delimiter.join(row))
                        f.write(br)
                    else:
                        if action == "edit":
                            print(f"Редактирование контакта")
                            entry.print()
                            entry = view.get_contact_data(entry, "edit")
                            f.write(delimiter.join(entry.get_values()))
                            f.write(br)
                        count += 1
            os.rename(f"temp{extension}", f"book{extension}")
            logger.log(action, entry, book_type)
        if action == "edit": print(f"Контакт успешно обновлён.\n")
        else: print(f"Успешно удалено {count} записей.\n")
