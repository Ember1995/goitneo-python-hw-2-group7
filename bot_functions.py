from bot_decorators import *

@input_error
@check_existing_contact
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError()

@input_error    
def show_phone(args, contacts):
    name, = args
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError()
    
def show_all(contacts):
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

if __name__ == "__main__":
    from main import main
    main()


    
