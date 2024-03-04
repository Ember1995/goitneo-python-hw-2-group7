def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"{str(e).capitalize()}"
    return inner

def validate_phone_format(func):
    def inner(args, contacts):
        name, phone = args
        if not (8 <= len(phone) <= 15) or not phone.startswith('+'):
            raise ValueError("The phone number must be between 8 and 15 characters long and start with '+'")
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