
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid command or arguments."
    return wrapper

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def find_contact(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def show_all_contacts(args, contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}

    while True:
        command = input("Enter a command: ").strip().split()
        if not command:
            continue
        if command[0] == "add":
            result = add_contact(command[1:], contacts)
        elif command[0] == "phone":
            result = find_contact(command[1:], contacts)
        elif command[0] == "all":
            result = show_all_contacts(command[1:], contacts)
        else:
            result = "Invalid command."

        print(result)

if __name__ == "__main__":
    main()
