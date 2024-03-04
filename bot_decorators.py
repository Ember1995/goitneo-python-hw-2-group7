def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"{str(e).capitalize()}"
    return inner

import re

def validate_phone_format(func):
    def inner(args, contacts):
        name, phone = args
        if not re.match(r'^\+\d[\d ()-]{7,14}$', phone):
            raise ValueError("Invalid phone number format.")
        return func(args, contacts)
    return inner

def check_existing_contact(func):
    def inner(args, contacts):
        name, phone = args
        if name in contacts:
            raise ValueError("Contact with this name already exists.")
        return func(args, contacts)
    return inner

if __name__ == "__main__":
    pass