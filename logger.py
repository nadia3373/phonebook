from datetime import datetime
import os.path


def get_timestamp():
    return str(datetime.now())


def log(action, entry, book_type):
    if not os.path.isfile('log.csv'):
        with open("log.csv", "a") as f:
            f.write(",".join(["date", "phone number", "action", "format"]))
            f.write("\n")
            f.write(",".join([get_timestamp(), entry.phone, action, str(book_type)]))
            f.write("\n")
    else:
        with open("log.csv", "a") as f:
            f.write(",".join([get_timestamp(), entry.phone, action, str(book_type)]))
            f.write("\n")